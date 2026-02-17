import os
import sys
from pycheevos.utils.sync import calculate_checksum
from pycheevos.utils.import_notes import *

def get_best_notes(game_id):
    racache = get_racache_path()
    local_notes = []
    local_source = "None"
    
    if racache:
        candidates = find_all_candidates(racache, game_id)
        for _, file_path, file_name in candidates:
            parsed = parse_local_file(file_path)
            if parsed:
                local_notes = parsed
                local_source = file_name
                break

    print(f"[SYNC] Checking server for updates on ID {game_id}...")
    server_notes = fetch_server_notes(game_id)

    if not local_notes and not server_notes:
        print("[ERROR] No data found locally or on server.")
        return [], "None"

    if local_notes and not server_notes:
        return local_notes, f"Local Only ({local_source})"
    
    elif server_notes and not local_notes:
        return server_notes, "RA Server"

    else:
        local_hash = calculate_checksum(local_notes)
        server_hash = calculate_checksum(server_notes)

        if local_hash == server_hash:
            return server_notes, "RA Server (Synced)"
        else:
            diff = len(local_notes) - len(server_notes) # type: ignore
            msg = f"Local Modifications Detected ({local_source})"
            if diff != 0: msg += f" [Diff: {diff:+d} notes]"
            return local_notes, msg

def process_dump(game_id):
    if not game_id: return

    notes, source = get_best_notes(game_id)
    if not notes: return

    print(f"\n[DUMP] Dumping notes from {source}...")
    
    try:
        notes.sort(key=lambda x: int(str(x['Address']), 16))
    except: pass

    output_dir = os.path.join(os.getcwd(), 'notes_dump')
    if not os.path.exists(output_dir): 
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, f"{game_id}-Notes.txt")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Game ID: {game_id}\n")
            f.write(f"Source: {source}\n")
            f.write(f"Total Notes: {len(notes)}\n")
            f.write("=" * 60 + "\n\n")
            for note in notes:
                addr = note.get('Address', '????')
                raw_text = str(note.get('Note', ''))
                text = raw_text.replace("\r\n", "\n").replace("\r", "\n").strip()
                f.write(f"{addr}: {text}\n")
                f.write("\n")
        print(f"Success! Notes dumped to: {filename}")
    except Exception as e:
        print(f"[ERROR] Could not write file: {e}")

if __name__ == "__main__":
    gid = input("Enter Game ID: ")
    process_dump(gid)