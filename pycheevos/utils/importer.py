from pycheevos.utils import import_notes
from pycheevos.utils import import_achievements
import sys
import os

def main():
    print("\n--- PyCheevos Unified Importer ---\n")

    game_id = input("Enter the Game ID (or 'q' to exit): ").strip()

    if not game_id or game_id.lower() == 'q':
        print("Exiting...")
        return
    
    print("\nWhat would you like to import?")
    print("[1] Code Notes only")
    print("[2] Achievements only")
    print("[3] Both (Recommended)")
    print("[q] Quit")

    choice = input("\nChoice: ").strip().lower()

    if choice == 'q':
        return
    
    if choice == '1':
        print("\n --- Start Notes Import ---")
        import_notes.process_game(game_id)
    
    elif choice == '2':
        print("\n --- Starting Achievements Import ---")
        import_achievements.process_game(game_id)

    elif choice == '3':
        print("\n--- STEP 1: Notes ---")
        import_notes.process_game(game_id)

        print("\n--- STEP 2: Achievements ---")
        import_achievements.process_game(game_id)
    
    else:
        print("Invalid option")
    
if __name__ == "__main__":
    main()