import time
from pathlib import Path

from .. import lib
from . import brown, green, red, white


def game_intro():
    """Game introduction logic."""
    print('Loading introduction...')
    lib.display_art('titleart.ben')
    time.sleep(5)
    lib.display_script('opening.ben')
    input('Press [ENTER] to start...')
    print('\033[H\033[J')  # Clear screen


def start_room():
    """First room logic"""
    lib.display_art('titleart.ben')
    time.sleep(1)
    print()
    print('You awake to find yourself on the floor of a large room.')
    print('You still have your pillow, but your bed and duvet are gone.')
    print('You stand up, dazed and confused. '
          "It's a Thursday, or - at least - you think it is.")
    print('You never could quite get the hang of Thursdays.')
    print()
    print('You can just about see doors to the north, east, south, and west.')
    print("It's kinda cold, and you're hungry.")
    print()


def navigate_rooms(data_path):
    """Navigate rooms based on player input"""
    while True:
        choice = input('> ').strip().lower()

        if choice == 'n':
            white.main(data_path)
            break
        if choice == 's':
            brown.main(data_path)
            break
        if choice == 'e':
            red.main(data_path)
            break
        if choice == 'w':
            green.amin(data_path)
            break
        if choice == 'u':
            print("There's nothing you can use right here.")
        elif choice == 'h':
            print("You give yourself a quick hug. It's not very satisfying.")
        else:
            print("I'm sorry, I don't understand you. "
                  'Commands are: n, e, s, w, u, and h.')


def main(data_path: Path):
    lib.reset_logic(data_path)  # Reset lever logic
    game_intro()  # Show introduction
    start_room()  # Start the first room
    navigate_rooms(data_path)  # Navigate through the rooms
