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

# --- LOCAL SEARCH ---

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
            return resp
        else:
            print(f"[ERROR] Server error: {resp.get('Error')}")
    
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
    
    return None

# --- LOGIC PARSER (MODERNIZED) ---

# Mapping: RA Flag -> Python Function (core.helpers)
FLAG_WRAPPER_MAP = {
    "R:": "reset_if",
    "P:": "pause_if",
    "M:": "measured",
    "Q:": "measured_if",
    "T:": "trigger",
    "I:": "add_address",
    "A:": "add_source",
    "B:": "sub_source",
    "C:": "add_hits",
    "D:": "sub_hits",
    "N:": "and_next",
    "O:": "or_next",
    "K:": "remember",
    "Z:": "reset_next_if",
    "G:": "measured_percent"
}

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
    "":   "word",
    "W":  "tbyte",
    "X":  "dword",
    "I":  "word_be",
    "J":  "tbyte_be",
    "G":  "dword_be",
    "L":  "low4",
    "U":  "high4",
    "K":  "bitcount",

    # non 0x values
    "fF": "float32",
    "fB": "float32_be",
    "fH": "double32",
    "fI": "double32_be",
    "fM": "mbf32",
    "fL": "mbf32_le",
}

MEM_TYPE_KEYS = sorted(MEM_TYPES, key=len, reverse=True)

PREFIXES = {
    "d": "delta",
    "p": "prior",
    "b": "bcd",
    "~": "invert",
}

CMP_MAP = {
    "!=": "!=",
    ">=": ">=",
    "<=": "<=",
    "=":  "==",
    ">":  ">",
    "<":  "<",
}

CMP_KEYS = sorted(CMP_MAP.keys(), key=len, reverse=True)

def parse_value(val_str: str) -> str:
    val_str = val_str.replace(" ", "")
    if not val_str:
        return "value(0)"
    
    wrap_func = ""
    if val_str[0] in PREFIXES:
        wrap_func = PREFIXES[val_str[0]]
        val_str = val_str[1:]

    # --- RECALL TREATMENT ---
    if "{recall}" in val_str:
        val_str = re.sub(r"0x[a-zA-Z]", "0x", val_str)

        op_match = re.search(r"(0x[a-fA-F0-9]+|[\d]+)\s*([\+\-\*\/])\s*\{recall\}", val_str)
        
        if op_match:
            numero = op_match.group(1)
            operador = op_match.group(2)
            
            if numero.startswith("0x"):
                val_obj = f"value({numero})"
            else:
                val_obj = f"value({int(numero)})"
            result = f"recall() {operador} {val_obj}"
        else:
            result = val_str.replace("{recall}", "recall()")

        if wrap_func:
            return f"({result}).{wrap_func}()"
        return result

    # Memory Access (0x...)
    if val_str.startswith("0x"):
        match = re.match(r"0x([a-zA-Z\s])?([a-fA-F0-9]+)", val_str)
        if match:
            prefix_type = match.group(1) if match.group(1) else ""
            prefix_type = prefix_type.strip()
            addr = match.group(2)
            
            func = MEM_TYPES.get(prefix_type, "word") 
            result = f"{func}(0x{addr})"
        else:
            result = "value(0)"
            wrap_func = ""
            
    elif val_str.isdigit():
        result = f"value({int(val_str)})"
        wrap_func = ""
    elif val_str.replace('.', '', 1).isdigit():
        result = f"float({val_str})"
        wrap_func = ""
    else:
        result = "value(0)"
        wrap_func = ""

    if wrap_func:
        return f"{result}.{wrap_func}()"
    return result

def parse_hits(right_str: str):
    if not right_str:
        return "0", ""
    
    right_str = right_str.strip('.')
    match = re.search(r'(\d+)\.(\d+)', right_str)
    if match:
        val = str(int(match.group(1)))
        hits = str(int(match.group(2)))
        return val, f".with_hits({hits})"
    
    return str(int(right_str)) if right_str.isdigit() else right_str, ""

def parse_comparison(cond_str: str):
    for op in CMP_KEYS:
        if op in cond_str:
            left, right = cond_str.split(op, 1)
            return left, CMP_MAP[op], right
    return cond_str, None, None

def parse_condition(cond_str: str):
    wrapper = None
    
    for flag_code, func_name in FLAG_WRAPPER_MAP.items():
        if cond_str.startswith(flag_code):
            wrapper = func_name
            cond_str = cond_str[len(flag_code):]
            break
    
    left_str, py_op, right_str = parse_comparison(cond_str)

    if py_op is None:
        val = parse_value(left_str)
        if not val or val == "0": 
             core_logic = "value(0)"
        else:
             core_logic = f"{val}"
    else:
        right_str, hits = parse_hits(right_str) # type: ignore

        if right_str.startswith("f"):
            right_str = right_str[1:]

        left = parse_value(left_str)
        right = parse_value(right_str)

        if not left: left = "value(0)"
        if not right: right = "value(0)"

        is_left_const = left.startswith('value(') or left.startswith('float(') or '(' not in left
        is_right_const = right.startswith('value(') or right.startswith('float(') or '(' not in right

        if is_left_const and is_right_const:
            core_logic = f"Condition({left}, '{py_op}', {right})"
        else:
            core_logic = f"({left} {py_op} {right})"
        
        if hits:
            core_logic += hits

    if wrapper:
        return f"{wrapper}({core_logic})"
    
    return core_logic

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

# --- SANITIZATION ---
def sanitize_name(note_text):
    clean = re.sub(r"[:/-]", "_", note_text)
    clean = re.sub(r'[^a-zA-Z0-9_\s]', '', clean)
    words = clean.lower().split()
    clean = "_".join(words)
    return clean[:65]

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
        for s in content["Sets"]:
            source_list.extend(s.get("Achievements", []))

    elif "PatchData" in content and isinstance(content["PatchData"], list):
        for s in content["PatchData"]:
            source_list.extend(s.get("Achievements", []))
    
    if not source_list and "Achievements" in content:
        source_list = content["Achievements"]

    if "PatchData" in content:
        patch = content["PatchData"]
        achievements = patch.get("Achievements", [])
        source_list.extend(achievements)

    for a in source_list:
        if a.get('ID') == 101000001:
            continue
        data.append({
            'id': a.get('ID'),
            'title': a.get('Title', 'Sem Título'),
            'desc': a.get('Description', ''),
            'points': a.get('Points', 0),
            'mem': a.get('MemAddr', ''),
            'type': a.get('Type', '')
        })
    return data

def generate_script(game_id, achievements, source_name):
    if not achievements: return False
    print(f"\n[GENERATING] Processing {len(achievements)} achievements of {source_name}...\n")
    
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
        title = ach['title'].replace('"', '\\"')
        desc = ach['desc'].replace('"', '\\"')
        ach_id = ach['id']
        ach_type = ach.get('type', '')

        type_str = ""
        if ach_type == "progression": type_str = ", type=AchievementType.PROGRESSION"
        elif ach_type == "win_condition": type_str = ", type=AchievementType.WIN_CONDITION"
        elif ach_type == "missable": type_str = ", type=AchievementType.MISSABLE"
        
        lines.append(f"# --- {title} ---")
        lines.append(f"# Logic: {ach['mem']}")
        
        logic_groups = parse_logic(ach['mem'])
        
        core_var = ""
        alt_vars = []
        
        for name, conds in logic_groups:
            var_name = f"ach_{ach_id}_{name}"
            if name == "logic": core_var = var_name
            else: alt_vars.append(var_name)
            
            lines.append(f"{var_name} = [")
            for c in conds:
                lines.append(f"    {c},")
            lines.append("]")
        
        lines.append(f"ach_{ach_id} = Achievement(")
        lines.append(f'    title="""{title}""",')
        lines.append(f'    description="""{desc}""",')
        lines.append(f'    points={ach["points"]}{type_str},')
        lines.append(f'    id={ach_id}')
        lines.append(")")
        
        if core_var: lines.append(f"ach_{ach_id}.add_core({core_var})")
        for alt in alt_vars: lines.append(f"ach_{ach_id}.add_alt({alt})")
        lines.append(f"my_set.add_achievement(ach_{ach_id})")
        lines.append("")

    lines.append("my_set.save()")

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
        game_id = input("\nEnter the Game ID (or 'q' to exit): ").strip()
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