import time
from pathlib import Path

from .. import lib
from . import brown, green, red, white


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Initialise the Title Art
    lib.display_art('titleart.ben')
    print()

    # Shakespeare wrote this, honest.
    time.sleep(1)
    print('You are back in the room you first woke up in.')
    print("It's huge. You can't really fathom how large, but it took")
    print('long enough to get from that last room back to the middle of')
    print('this one. You wonder how you got here, and who is responsible.')
    print()
    print('You can just about see doors to the north, east, south, and west.')
    print()
    print('What would you like to do?')

    # Room logic loop
    while True:
        nsewuh = input('> ').strip().lower()
        if nsewuh == 'n':
            # Call the white.py script (adjust as necessary)
            print('Going to the white room...')
            white.main(data_path)
            break
        if nsewuh == 's':
            print('Going to the brown room...')
            brown.main(data_path)
            break
        if nsewuh == 'e':
            print('Going to the red room...')
            red.main(data_path)
            break
        if nsewuh == 'w':
            print('Going to the green room...')
            green.main(data_path)
            break
        if nsewuh == 'u':
            print("There's nothing you can use right here.")
        elif nsewuh == 'h':
            print("You give yourself a quick hug. It's not very satisfying.")
        else:
            print(
                "I'm sorry, I don't understand you. Commands are: n, e, s, w, u, and h.")

    print('Exiting the room...')
