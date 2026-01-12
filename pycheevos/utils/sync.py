import hashlib
import json

def calculate_checksum(notes_list):
    standardized = []
    for note in notes_list:
        addr = note.get('Address', '').lower()
        text = note.get('Note', '').strip()
        standardized.append(f"{addr}:{text}")
    standardized.sort()
    
    data_str = "|".join(standardized)
    return hashlib.md5(data_str.encode('utf-8')).hexdigest()