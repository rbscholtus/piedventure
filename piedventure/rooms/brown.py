import time
from pathlib import Path

from .. import lib
from . import mainroom


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Initialise the Title Art
    lib.display_art('titleart.ben')
    print()

    time.sleep(1)

    # Room description
    print('You run south and through an open archway into a dark, dingy place.')
    print('The carpet looks like the 70s threw up on it, and the place smells faintly')
    print('of cabbage. This could well be every retirement home ever made, combined')
    print("into one place. It's tragic.")
    print()
    print("Oddly, though, there's a lever set into the right hand wall.")

    # Check the lever state
    leverstate = lib.get_leverstate(data_path)
    if leverstate == 'on':
        print(
            "The last time you were in this room, you turned the lever on. It's still on.",
        )
    else:
        print("It looks like it's in the off position.")

    print()
    print('The only exit is north, back the way you came.')
    print()
    print('What would you like to do?')

    # Actions loop
    while True:
        nsewuh = input('> ').strip().lower()
        if nsewuh == 'n':
            # Call the mainroom.py script
            print('Going back to the main room...')
            mainroom.main(data_path)
            break
        if nsewuh == 's':
            print('You attempt to walk through the wall. You fail.')
        elif nsewuh == 'e':
            print("Right, let me explain this whole 'wall' thing to you...")
        elif nsewuh == 'w':
            print("Seriously? Through the wall? Sorry, I can't do that.")
        elif nsewuh == 'u':
            # Check the lever state again
            leverstate = Path('/logic/leverlogic.ben').read_text().strip()
            if leverstate == 'on':
                print('Having already turned it on, you try to turn it off. And fail.')
            else:
                # Change the lever state from off to on
                lib.set_leverstate(data_path, 'on')
                print("You push the lever to 'on',"
                      ' and hear a humming start elsewhere in the building.')
        elif nsewuh == 'h':
            print('You hug yourself, and hope nobody is watching.')
        else:
            print(
                "I'm sorry, I don't understand you. Commands are: n, e, s, w, u, and h.")

    print('Exiting the room...')
