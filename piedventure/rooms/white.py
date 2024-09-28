import time
from pathlib import Path

from .. import lib
from . import kroo, mainroom


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Initialise the Title Art
    lib.display_art('titleart.ben')
    print()

    # Setting up the room...
    time.sleep(1)
    print('You run north, pushing through the half-open doorway ahead.')
    print('The room you find yourself in is bright. A sign on the wall tells')
    print("you that you are in the White Room. I guess that explains why it's")
    print('so bright and all that...')
    print()

    # Check the lever state
    leverstate = Path('../logic/leverlogic.ben').read_text().strip()
    if leverstate == 'on':
        print("There's a delicately carved statue at the end of the room.")
        print("It's a kitten, hewn from beautiful white marble.")
        print('It is also emitting a strange humming noise.')
    else:
        print("There's a delicately carved statue at the end of the room.")
        print("It's a kitten, hewn from beautiful white marble.")

    print()
    print('The only exit is south, back the way you came.')
    print()
    print('What would you like to do?')

    # Capture this room's actions
    while True:
        nsewuh = input('> ').strip().lower()
        if nsewuh == 'n':
            print("Somehow you think walls don't apply to you. They do.")
        elif nsewuh == 's':
            # Call the mainroom.py script
            print('Going back to the main room...')
            mainroom.main(data_path)
            break
        elif nsewuh == 'e':
            print("No can do. There's a wall there.")
        elif nsewuh == 'w':
            print("Seriously? Through the wall? Sorry, I can't do that.")
        elif nsewuh == 'u':
            print('You try to use the statue. It feels weird, so you stop.')
        elif nsewuh == 'h':
            if leverstate == 'on':
                kroo.main(data_path)
                break
            print('You hug the statue. It seems to vibrate a little. Weird.')
        else:
            print(
                "I'm sorry, I don't understand you. Commands are: n, e, s, w, u and h.")

    print('Exiting...')
