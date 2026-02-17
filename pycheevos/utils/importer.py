from pycheevos.utils import import_notes
from pycheevos.utils import import_set
from pycheevos.utils import import_achievements
from pycheevos.utils import import_leaderboard
from pycheevos.utils import dump_notes
import sys
import os

def main():
    print("\n--- PyCheevos Unified Importer ---\n")

    game_id = input("Enter the Game ID (or 'q' to exit): ").strip()

    if not game_id or game_id.lower() == 'q':
        print("Exiting...")
        return
    
    print("\nWhat would you like to import?")
    print("[1] Code Notes (Generate Python Script)")
    print("[2] Achievements only (Raw)")
    print("[3] Leaderboards only (Raw)")
    print("[4] Unified (Notes + Smart Achievements + Leaderboards)")
    print("[5] Dump Code Notes to TXT (Documentation)")
    print("[q] Quit")

    choice = input("\nChoice: ").strip().lower()

    if choice == 'q':
        return
    
    if choice == '1':
        print("\n --- Start Notes Import (Python) ---")
        import_notes.process_game(game_id)
    
    elif choice == '2':
        print("\n --- Starting Achievements Import ---")
        import_achievements.process_game(game_id)
        
    elif choice == '3':
        print("\n --- Starting Leaderboards Import ---")
        import_leaderboard.process_game(game_id)

    elif choice == '4':
        print("\n--- Unified Import ---")
        import_set.process_game(game_id)

    elif choice == '5':
        print("\n--- Dumping Notes to TXT ---")
        dump_notes.process_dump(game_id)
    
    else:
        print("Invalid option")
    
if __name__ == "__main__":
    main()