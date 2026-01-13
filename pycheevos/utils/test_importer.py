import os
import sys
import json
import re
import requests
import getpass
import hashlib
from pycheevos.utils import import_notes

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)

CACHE_PATH_FILE = os.path.join(ROOT_DIR, '.racache_path')
LOGIN_CACHE_FILE = os.path.join(ROOT_DIR, '.login_cache')

def get_racache_path():
    return import_notes.get_racache_path()

def get_credentials():
    return import_notes.get_credentials()

def calculate_checksum(achievements_list):
    standardized = []
    for ach in achievements_list:
        id_str = str(ach.get('id', ''))
        mem = str(ach.get('mem') or '').strip()
        title = str(ach.get('title') or '').strip()
        desc = str(ach.get('desc') or '').strip()
        points = str(ach.get('points', 0))
        type_str = str(ach.get('type') or '').strip()

        entry = f"{id_str}|{mem}|{title}|{title}|{desc}|{points}|{type_str}"
        standardized.append(entry)

    standardized.sort()
    data_str = "||".join(standardized)
    return hashlib.md5(data_str.encode('utf-8')).hexdigest()

# --- LOGIC PARSER (SMART) ---

FLAG_WRAPPER_MAP = {
    "R:": "reset_if", "P:": "pause_if", "M:": "measured", "Q:": "measured_if",
    "T:": "trigger", "I:": "add_address", "A:": "add_source", "B:": "sub_source",
    "C:": "add_hits", "D:": "sub_hits", "N:": "and_next", "O:": "or_next",
    "K:": "remember", "Z:": "reset_next_if", "G:": "measured_percent"
}

MEM_TYPES = {
    "M": "bit0", "N": "bit1", "O": "bit2", "P": "bit3", "Q": "bit4", "R": "bit5",
    "S": "bit6", "T": "bit7", "H": "byte", "": "word", "W": "tbyte", "X": "dword",
    "I": "word_be", "J": "tbyte_be", "G": "dword_be", "L": "low4", "U": "high4", "K": "bitcount",
    "fF": "float32", "fB": "float32_be", "fH": "double32", "fI": "double32_be", "fM": "mbf32", "fL": "mbf32_le",
}
PREFIXES = {"d": "delta", "p": "prior", "b": "bcd", "~": "invert"}

CMP_MAP = {"!=": "!=", ">=": ">=", "<=": "<=", "=": "==", ">": ">", "<": "<"}

CMP_KEYS = sorted(CMP_MAP.keys(), key=len, reverse=True)

ADDRESS_MAP = {}

def parse_value(val_str: str) -> str:
    val_str = val_str.replace(" ", "")
    if not val_str: return "value(0)"
    
    wrap_func = ""
    if val_str[0] in PREFIXES:
        wrap_func = PREFIXES[val_str[0]]
        val_str = val_str[1:]

    # Lógica de Recall
    if "{recall}" in val_str:
        val_str = re.sub(r"0x[a-zA-Z]", "0x", val_str)
        op_match = re.search(r"(0x[a-fA-F0-9]+|[\d]+)\s*([\+\-\*\/])\s*\{recall\}", val_str)
        if op_match:
            numero = op_match.group(1)
            operador = op_match.group(2)
            val_obj = f"value({numero})" if numero.startswith("0x") else f"value({int(numero)})"
            result = f"recall() {operador} {val_obj}"
        else:
            result = val_str.replace("{recall}", "recall()")
        return f"({result}).{wrap_func}()" if wrap_func else result

    # Lógica Principal de Endereços
    if val_str.startswith("0x"):
        match = re.match(r"0x([a-zA-Z\s])?([a-fA-F0-9]+)", val_str)
        if match:
            raw_addr = match.group(2).lstrip('0')
            if not raw_addr: raw_addr = "0"
            raw_addr = "0x" + raw_addr
            
            if raw_addr in ADDRESS_MAP:
                variable_name = ADDRESS_MAP[raw_addr]
                result = variable_name
            else:
                prefix_type = match.group(1).strip() if match.group(1) else ""
                func = MEM_TYPES.get(prefix_type, "word") 
                result = f"{func}(0x{match.group(2)})"
        else:
            result = "value(0)"
            
    elif val_str.isdigit():
        result = f"value({int(val_str)})"
    elif val_str.replace('.', '', 1).isdigit():
        result = f"float({val_str})"
    else:
        result = "value(0)"

    return f"{result}.{wrap_func}()" if wrap_func else result

def parse_hits(right_str: str):
    if not right_str: return "0", ""
    right_str = right_str.strip('.')
    match = re.search(r'(\d+)\.(\d+)', right_str)
    if match:
        return match.group(1), f".with_hits({match.group(2)})"
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
    left_str, py_op, rigth_str = parse_comparison(cond_str)
    if py_op is None:
        val = parse_value(left_str)
        core_logic = f"{val}" if val and val != "0" else "value(0)"
    else:
        rigth_str, hits = parse_hits(rigth_str)
        if rigth_str.startswith("f"): rigth_str = rigth_str[1:]

        left = parse_value(left_str)
        right = parse_value(rigth_str)
        if not left: left = "value(0)"
        if not right: right = "value(0)"

        is_left_const = left.startswith('value(') or left.startswith('float(') or '(' not in left
        is_right_const = right.startswith('value(') or right.startswith('float(') or '(' not in right

        core_logic = f"({left} {py_op} {right})"

        if hits: core_logic += hits

    return f"{wrapper} ({core_logic})" if wrapper else core_logic

def parse_logic(mem_string):
    if not mem_string: return []
    groups = mem_string.split('S')
    parsed_groups = []
    for i, group in enumerate(groups):
        conditions = []
        for cond_str in group.split('_'):
            if cond_str: conditions.append(parse_condition(cond_str))
        name = "logic" if i == 0 else f"alt{i}"
        parsed_groups.append((name, conditions))
    return parsed_groups

# --- NOTE MAPPING BUILDER ---

def build_address_map(notes):
    global ADDRESS_MAP
    ADDRESS_MAP.clear()
    used_names = {}
    
    for note in notes:
        addr = note.get("Address")
        text = note.get("Note", "")
        if not text or not addr: continue
        try:
            int_addr = int(addr, 16) if str(addr).startswith("0x") else int(addr)
            norm_addr = hex(int_addr) # '0x10'
        except:
            continue

        note_lines = text.replace('\r', '').split('\n')
        clean_text = re.sub(r'^\s*\[[^\]]+\]\s*', '', note_lines[0])
        clean_text = clean_text.split('\n')[0].strip()
        var_name = import_notes.sanitize_name(clean_text)
        var_name = import_notes.prefix_region(var_name, text)
        if not var_name: var_name = f"unk_{norm_addr}"

        if var_name in used_names:
            used_names[var_name] += 1
            var_name = f"{var_name}_{used_names[var_name]}"
        else:
            used_names[var_name] = 1
        
        ADDRESS_MAP[norm_addr] = var_name

    print(f"[SMART IMPORT] Mapped {len(ADDRESS_MAP)} variables from Code Notes.")

# --- DATA PROCESSING (ACHIEVEMENTS) ---

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
                                    'points': parts[5] if len(parts)>5 else "0",
                                    'type': ""
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
        for s in content["Sets"]: source_list.extend(s.get("Achievements", []))
    elif "PatchData" in content and isinstance(content["PatchData"], list):
        for s in content["PatchData"]: source_list.extend(s.get("Achievements", []))
    
    if not source_list and "Achievements" in content:
        source_list = content["Achievements"]

    if "PatchData" in content and isinstance(content["PatchData"], dict):
        patch = content["PatchData"]
        achievements = patch.get("Achievements", [])
        source_list.extend(achievements)

    for a in source_list:
        if a.get('ID') == 101000001: continue
        data.append({
            'id': a.get('ID'),
            'title': a.get('Title', 'Sem Título') or '',
            'desc': a.get('Description', '') or '',
            'points': a.get('Points', 0),
            'mem': a.get('MemAddr', '') or '',
            'type': a.get('Type') or ''
        })
    return data

def generate_script(game_id, achievements, source_name):
    if not achievements: return False
    print(f"\n[GENERATING] Processing {len(achievements)} achievements from {source_name}...\n")
    
    lines = []
    lines.append("from pycheevos.core.helpers import *")
    lines.append("from pycheevos.core.constants import *")
    lines.append("from pycheevos.core.condition import Condition")
    lines.append("from pycheevos.models.achievement import Achievement")
    lines.append("from pycheevos.models.set import AchievementSet")
    
    # --- SEAN'S IDEA: Importa o arquivo de notas gerado ---
    lines.append(f"from notes_{game_id} import *") 
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
        
        # Parse Logic usa o ADDRESS_MAP agora
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

# --- MAIN LOOP (HYBRID SYNC) ---

def process_game(game_id):
    if not game_id: return

    racache = get_racache_path()
    
    # --- PASSO 1: CARREGAR NOTAS (Necessário para o mapeamento) ---
    print("\n--- STEP 1: Loading Notes for Variable Mapping ---")
    
    # Tenta local
    local_notes = []
    if racache:
        candidates = import_notes.find_all_candidates(racache, game_id)
        for _, file_path, file_name in candidates:
            parsed = import_notes.parse_local_file(file_path)
            if parsed:
                local_notes = parsed
                break
    
    # Tenta servidor
    server_notes = import_notes.fetch_server_notes(game_id)
    
    # Decide qual usar (mesma lógica do import_notes)
    final_notes = []
    if local_notes and not server_notes:
        final_notes = local_notes
    elif server_notes and not local_notes:
        final_notes = server_notes
    elif local_notes and server_notes:
        # Prioridade local para mapeamento também, para ser consistente
        final_notes = local_notes
    
    if final_notes:
        build_address_map(final_notes)
    else:
        print("[WARNING] No notes found. Script will use raw byte(0x...) addresses.")

    # --- PASSO 2: CARREGAR CONQUISTAS ---
    print("\n--- STEP 2: Loading Achievements ---")
    local_achs = []
    local_source = "None"
    
    if racache:
        # Reutiliza find_all_candidates do achievements (é diferente do notes)
        candidates = find_all_candidates(racache, game_id)
        for _, file_path, file_name in candidates:
            parsed = extract_achievements(file_path, is_file=True)
            if parsed:
                local_achs = parsed
                local_source = file_name
                break

    print(f"[SYNC] Checking server for updates on ID {game_id}...")
    server_data = fetch_server_data(game_id)
    server_achs = []
    if server_data:
        server_achs = extract_achievements(server_data, is_file=False)

    final_achs = []
    final_source = ""
    status_msg = ""

    if not local_achs and not server_achs:
        print("[ERROR] No achievements found locally or on server.")
        return

    if local_achs and not server_achs:
        final_achs = local_achs
        final_source = local_source
        status_msg = "Local Only (Offline)"
    
    elif server_achs and not local_achs:
        final_achs = server_achs
        final_source = "RA Server"
        status_msg = "Server Only (New Import)"

    else:
        local_hash = calculate_checksum(local_achs)
        server_hash = calculate_checksum(server_achs)

        if local_hash == server_hash:
            final_achs = server_achs
            final_source = "RA Server (Synced)"
            status_msg = "Synced with Local"
        else:
            final_achs = local_achs
            final_source = local_source
            status_msg = "Local Modifications Detected (Unsynced)"
            
            diff = len(local_achs) - len(server_achs)
            if diff != 0: status_msg += f" [Count Diff: {diff:+d}]"

    # 4. Gera o Script
    print(f"\n[RESULT] Using: {final_source}")
    print(f"[STATUS] {status_msg}")
    
    generate_script(game_id, final_achs, final_source)

# --- LOCAL SEARCH HELPER ---
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

# --- SERVER DOWNLOAD HELPER ---
def fetch_server_data(game_id):
    user, password = get_credentials()
    if not user or not password: return None
    sess = requests.Session()
    sess.headers.update({'User-Agent': f'PyCheevos_Importer/1.0 ({user})'})
    url = "https://retroachievements.org/dorequest.php"
    try:
        login = sess.post(url, data={'r': 'login', 'u': user, 'p': password}).json()
        if not login.get('Success'): return None
        token = login.get('Token')
        payload = {'r': 'patch', 'g': game_id, 'u': user, 't': token}
        resp = sess.post(url, data=payload).json()
        if resp.get('Success'): return resp
    except: pass
    return None

def main():
    print("--- PyCheevos Smart Importer ---")
    while True:
        game_id = input("\nEnter the Game ID (or 'q' to exit): ").strip()
        if game_id.lower() == 'q': break
        process_game(game_id)

if __name__ == "__main__":
    main()
