import time
from pathlib import Path

from .. import lib
from . import bigroom, gameroom, grue


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Initialise the Title Art
    lib.display_art('titleart.ben')
    print('\n')

    # Room description
    time.sleep(1)
    print('What. The. Actual. Fuck.')
    print()
    time.sleep(3)
    print('You hugged a statue of a beautiful kitten. As you do.')
    print()
    print("But you weren't expecting it to come to life and transport")
    print('you to another mystery room. This is getting a bit weird.')
    print()
    print('You now seem to find yourself in a small-ish corridor. You can')
    print('see a glow coming from the rooms to your east and west, and')
    print("there's a big, old looking door south of you.")
    print()
    print('What would you like to do?')

    # Room logic
    while True:
        nsewuh = input('> ').strip().lower()  # Read user input and normalize
        if nsewuh == 'n':
            print('You faceplant the wall. Idiot.')
        elif nsewuh == 's':
            bigroom.main(data_path)
            break
        elif nsewuh == 'e':
            gameroom.main(data_path)
            break
        elif nsewuh == 'w':
            grue.main(data_path)
            break
        elif nsewuh == 'u':
            print("There's nothing you can use right here.")
        elif nsewuh == 'h':
            print("After hugging that cat you aren't sure"
                  ' you should try to hug yourself again.')
        else:
            print(
                "I'm sorry, I don't understand you. Commands are: n, e, s, w, u and h.")

    # Exit script
