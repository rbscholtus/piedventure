import time
from pathlib import Path

from .. import lib
from . import mainroom


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Initialise the Title Art
    lib.display_art('titleart.ben')

    # Room description
    print('\n')
    time.sleep(1)
    print("You're off to see the wizard. Well, maybe not - but this")
    print('room is so green you might as well be in Emerald City.')
    print("Seriously. Think of the greenest thing you've ever seen,")
    print("then add another suitcase full of green. It's that bad.")
    print("\nIt's getting to you. Such pain. Is there a door? Who knows.")
    print('\nWhat would you like to do?')

    # Actions loop
    while True:
        nsewuh = input('> ').strip().lower()
        if nsewuh == 'n':
            print('The green is a bit more intense over here. Oops.')
        elif nsewuh == 's':
            print('Such green. Much bad. Go back. SCHTAP.')
        elif nsewuh == 'e':
            # Call mainroom.py
            mainroom.main(data_path)
            break  # Exit the loop after the call
        elif nsewuh == 'w':
            print('You attempt to go west, but ALL YOU SEE IS GREEN.')
        elif nsewuh == 'u':
            print("You think about 'using' green, "
                  "but realise it's not legal in this country.")
        elif nsewuh == 'h':
            print('You curl yourself up into a ball and rock back and forth.')
        else:
            print(
                "I'm sorry, I don't understand you. Commands are: n, e, s, w, u and h.")
