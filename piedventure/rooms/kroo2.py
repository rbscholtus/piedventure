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
    print("You're in a corridor, but it's quite a small one. You got here")
    print('the first time by hugging a statue of a kitten. Standard.')
    print()
    print('You see a glow coming from the rooms to your east and west, and')
    print("there's a big, old looking door to the south of you.")
    print()
    print('What would you like to do?')

    # Room choices
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
