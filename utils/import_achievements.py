import os
import sys
import json
import re
import requests
import getpass

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)

CACHE_PATH_FILE = os.path.join(ROOT_DIR, '.racache_path')
LOGIN_CACHE_FILE = os.path.join(ROOT_DIR, '.login_cache')

# --- CONFIGURATION AND CREDENTIALS ---

def get_racache_path():
    path = None
    if os.path.exists(CACHE_PATH_FILE):
        try:
            with open(CACHE_PATH_FILE, 'r') as f:
                path = f.read().strip()
        except: pass

    if path and os.path.exists(path):
        return path
    
    print("\n[CONFIG] Emulator folder not found.")
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        print("Opening selection window...")
        path = filedialog.askdirectory(title="Select the emulator's root folder.")
        root.destroy()
    except: pass

    if not path:
        print("Please enter the path manually:")
        path = input("Path: ").strip().strip('"').strip("'")

    if os.path.exists(path):
        with open(CACHE_PATH_FILE, 'w') as f: f.write(path)
        print(f"[INFO] Path saved in '{CACHE_PATH_FILE}'")
        return path
    else:
        print("[ERROR] Invalid path.")
        return None

def get_credentials():
    user, password = None, None
    if os.path.exists(LOGIN_CACHE_FILE):
        try:
            with open(LOGIN_CACHE_FILE, 'r') as f:
                data = json.load(f)
                user, password = data.get('user'), data.get('password')
        except: pass

    if user and password:
        return user, password

    print("\n[LOGIN] RetroAchievements Credentials Required")
    user = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()

    if user and password:
        if input("Save credentials locally? (y/n): ").lower() == 'y':
            with open(LOGIN_CACHE_FILE, 'w') as f:
                json.dump({'user': user, 'password': password}, f)
            print(f"[INFO] Credentials saved in '{LOGIN_CACHE_FILE}'")
    
    return user, password

# --- BUSCA LOCAL ---

def find_all_candidates(base_path, game_id):
    print(f"[DEBUG] Scanning {base_path} by ID {game_id}...")
    
    candidates = []
    target_files = [f"{game_id}-User.txt", f"{game_id}.json"]
    targets_lower = [t.lower() for t in target_files]
    
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower() in targets_lower:
                full_path = os.path.join(root, file)
                priority = 2
                if file.lower().endswith("-user.txt"): priority = 1
                
                candidates.append((priority, full_path, file))
                print(f"   File found: {file}")

    candidates.sort(key=lambda x: x[0])
    return candidates

# --- SERVER DOWNLOAD ---

def fetch_server_data(game_id):
    user, password = get_credentials()
    if not user or not password: return None

    print(f"[SERVER] Connecting as {user}...")
    sess = requests.Session()
    sess.headers.update({'User-Agent': f'PyCheevos_Importer/1.0 ({user})'})
    url = "https://retroachievements.org/dorequest.php"

    try:
        login = sess.post(url, data={'r': 'login', 'u': user, 'p': password}).json()
        if not login.get('Success'):
            print(f"[ERROR] Login failed: {login.get('Error')}")
            if os.path.exists(LOGIN_CACHE_FILE): os.remove(LOGIN_CACHE_FILE)
            return None
        
        token = login.get('Token')

        print(f"[SERVER] Downloading game data {game_id}...")
        payload = {'r': 'patch', 'g': game_id, 'u': user, 't': token}
        resp = sess.post(url, data=payload).json()
        
        if resp.get('Success'):
            resp = json.dumps(resp)
            return resp
        else:
            print(f"[ERROR] Server error: {resp.get('Error')}")
    
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
    
    return None

# --- LOGIC PARSER ---

MEM_TYPES = {
    "M":  "bit0",
    "N":  "bit1",
    "O":  "bit2",
    "P":  "bit3",
    "Q":  "bit4",
    "R":  "bit5",
    "S":  "bit6",
    "T":  "bit7",
    "H":  "byte",
    " ":  "word",
    "W":  "tbyte",
    "X":  "dword",
    "I":  "word_be",
    "J":  "tbyte_be",
    "G":  "dword_be",
    "L":  "low4",
    "U":  "high4",
    "K":  "bitcount",

    # non 0x values
    "fF": "float",
    "fB": "float_be",
    "fH": "double32",
    "fI": "double32_be",
    "fM": "mbf32",
    "fL": "mbf32_le",
}

MEM_TYPE_KEYS = sorted(MEM_TYPES, key=len, reverse=True)

PREFIXES = {
    "d": ".delta()",
    "p": ".prior()",
    "b": ".bcd()",
    "~": ".invert()",
}

PREFIX_KEYS = tuple(PREFIXES)

CMP_MAP = {
    "!=": "!=",
    ">=": ">=",
    "<=": "<=",
    "=":  "==",
    ">":  ">",
    "<":  "<",
}

CMP_KEYS = tuple(CMP_MAP)

COND_PREFIXES = {
    "":   "none",
    "P:": "pause_if",
    "R:": "reset_if",
    "Z:": "reset_next_if",
    "C:": "add_hits",
    "D:": "sub_hits",
    "A:": "add_source",
    "B:": "sub_source",
    "I:": "add_address",
    "M:": "measured",
    "T:": "trigger",
    "N:": "and_next",
    "O:": "or_next",
    "G:": "measured_percent",
    "Q:": "measured_if",
    "K:": "remember",
}

COND_KEYS = sorted(COND_PREFIXES, key=len, reverse=True)

def parse_condition_prefix(val: str):
    for key in COND_KEYS:
        if key and val.startswith(key):
            return COND_PREFIXES[key], val[len(key):]

    # no prefix
    return "none", val

def parse_value(val_str: str) -> str:
    val_str = val_str.replace(" ", "")
    suffix = ""

    if val_str and val_str[0] in PREFIXES:
        suffix = PREFIXES[val_str[0]]
        val_str = val_str[1:]

    # memory reference: must start with 0x
    if val_str.startswith('f') and not any(val_str.startswith(code) for code in MEM_TYPE_KEYS):
        # skip 'f' and parse the numeric part
        return f"float({val_str[1:]}){suffix}"

    # memory reference (0x or float memory types)
    if val_str.startswith("0x"):
        mem = val_str[2:]
        for code in MEM_TYPE_KEYS:
            if mem.startswith(code):
                addr = mem[len(code):]
                func = MEM_TYPES[code]
                return f"{func}(0x{addr}){suffix}"

    # float memory types starting with 'fF', 'fB', etc.
    for code in MEM_TYPE_KEYS:
        if val_str.startswith(code):
            addr = val_str[len(code):]
            func = MEM_TYPES[code]
            return f"{func}(0x{addr}){suffix}"

    # numeric literal
    return val_str

def parse_hits(right_str: str):
    right_str = right_str.rstrip(".")
    match = re.fullmatch(r'(\d+)\.(\d+)', right_str)
    if not match:
        return right_str, ""

    value, hits = match.groups()
    return value, f".with_hits({hits})"

def parse_flag(cond_str: str):
    flag, rest = parse_condition_prefix(cond_str)
    if flag and flag != "none":
        return f".with_flag('{flag}')", rest
    return "", rest

def parse_comparison(cond_str: str):
    for op in CMP_KEYS:
        if op in cond_str:
            left, right = cond_str.split(op, 1)
            return left, CMP_MAP[op], right
    return cond_str, None, None

def parse_condition(cond_str: str):

    # flag
    flag, cond_str = parse_flag(cond_str)

    # comparison
    left_str, py_op, right_str = parse_comparison(cond_str)

    # 
    if py_op is None:
        val = parse_value(left_str)
        return f"({val}){flag}"

    # hits
    right_str, hits = parse_hits(right_str)

    left = parse_value(left_str)
    right = parse_value(right_str)

    return f"({left} {py_op} {right}){flag}{hits}"

def parse_logic(mem_string):
    if not mem_string:
        return []

    groups = mem_string.split('S')
    parsed_groups = []

    for i, group in enumerate(groups):
        conditions = []
        for cond_str in group.split('_'):
            if cond_str:
                conditions.append(parse_condition(cond_str))
        name = "logic" if i == 0 else f"alt{i}"
        parsed_groups.append((name, conditions))

    return parsed_groups

# --- DATA PROCESSING ---

def extract_achievements(source_data, is_file=False):
    achievements = []
    
    if is_file:
        file_path = source_data
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                if file_path.endswith('.json'):
                    content = json.load(f)
                    return extract_from_json_obj(content)
                else:
                    for line in f:
                        if re.match(r'^\d+:', line):
                            parts = line.split('":')
                            print(parts)
                            if len(parts) >= 4:
                                achievements.append({
                                    'id': parts[0],
                                    'mem': parts[1].strip('"'),
                                    'title': parts[2].strip('"'),
                                    'desc': parts[3].strip('"'),
                                    'points': parts[5] if len(parts)>5 else "0"
                                })
        except Exception as e:
            print(f"[ERROR] Failed to read file: {e}")
            return []

    else:
        return extract_from_json_obj(source_data)

    return achievements

def extract_from_json_obj(content):
    data = []
    source_list = []
    
    if "Sets" in content and isinstance(content["Sets"], list):
        print("1")
        for s in content["Sets"]:
            source_list.extend(s.get("Achievements", []))

    elif "PatchData" in content and isinstance(content["PatchData"], list):
        print("2")
        for s in content["PatchData"]:
            source_list.extend(s.get("Achievements", []))
    
    if not source_list and "Achievements" in content:
        print("3")
        source_list = content["Achievements"]

    if not source_list and "PatchData" in content:
         print("4")
         pass

    for a in source_list:
        if a.get('ID') == 101000001:
            continue
        data.append({
            'id': a.get('ID'),
            'title': a.get('Title', 'Sem Título'),
            'desc': a.get('Description', ''),
            'points': a.get('Points', 0),
            'mem': a.get('MemAddr', '')
        })
    return data

def generate_script(game_id, achievements, source_name):
    if not achievements: return False
    print(f"\n[GENERATING] Processing {len(achievements)} achievements of {source_name}...")
    
    lines = []
    lines.append("from core.helpers import *")
    lines.append("from core.constants import *")
    lines.append("from core.condition import Condition")
    lines.append("from models.achievement import Achievement")
    lines.append("from models.set import AchievementSet")
    lines.append("")
    lines.append(f'my_set = AchievementSet(game_id={game_id}, title="Imported Set")')
    lines.append("")

    for ach in achievements:
        title = ach['title']
        ach_id = ach['id']
        
        lines.append(f"# --- {title} ---")
        lines.append(f"# Logic: {ach['mem']}")
        
        logic_groups = parse_logic(ach['mem'])
        
        core_var = ""
        alt_vars = []
        
        for name, conds in logic_groups:
            var_name = f"{name}_logic_{ach_id}"
            if name == "logic": core_var = var_name
            else: alt_vars.append(var_name)
            
            lines.append(f"{var_name} = [")
            for c in conds:
                lines.append(f"    {c},")
            lines.append("]")
        
        lines.append(f"ach_{ach_id} = Achievement(")
        lines.append(f'    title="{title}",')
        lines.append(f'    description="{ach["desc"]}",')
        lines.append(f'    points={ach["points"]},')
        lines.append(f'    id={ach_id}')
        lines.append(")")
        
        if core_var: lines.append(f"ach_{ach_id}.add_core({core_var})")
        for alt in alt_vars: lines.append(f"ach_{ach_id}.add_alt({alt})")
        lines.append(f"my_set.add_achievement(ach_{ach_id})")
        lines.append("")

    out_dir = os.path.join(ROOT_DIR, 'scripts')
    if not os.path.exists(out_dir): os.makedirs(out_dir)
    out_file = os.path.join(out_dir, f"achievement_{game_id}.py")
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"SUCCESS! Script generated: {out_file}")
    return True

# --- MAIN LOOP ---

def main():
    print("--- PyCheevos Achievement Importer ---")
    
    while True:
        print("\n" + "="*30)
        game_id = input("Enter the Game ID (or 'q' to exit): ").strip()
        if game_id.lower() == 'q': break
        if not game_id: continue

        # Local Search
        racache = get_racache_path()
        candidates = []
        if racache:
            candidates = find_all_candidates(racache, game_id)
        
        success = False
        
        # Attempts to process local files
        for prio, file_path, file_name in candidates:
            achievements = extract_achievements(file_path, is_file=True)
            if achievements:
                print(f"[LOCAL] Success! {len(achievements)} achievements in {file_name}")
                if generate_script(game_id, achievements, file_name):
                    success = True
                    break
            else:
                print(f"[LOCAL] Empty or invalid file: {file_name}")

        if success: break

        # Fallback Server
        print(f"\n[INFO] No local achievements found for ID {game_id}.")
        print("Options:")
        print("  [1] Try another ID")
        print("  [2] Download from RetroAchievements (Login required)")
        print("  [3] Exit")
        
        choice = input("Choice: ").strip()
        if choice == '3' or choice.lower() == 'q': break
        if choice == '1': continue
        
        if choice == '2':
            server_data = fetch_server_data(game_id)
            if server_data:
                print(type(server_data))
                achievements = extract_achievements(server_data, is_file=False)
                if achievements:
                    if generate_script(game_id, achievements, "RA Server"):
                        break
                else:
                    print("No achievements found in the server data.")
            else:
                print("\n[NOTICE] Unable to download from server.")
                input("Press Enter to try again...")

if __name__ == "__main__":
    main()