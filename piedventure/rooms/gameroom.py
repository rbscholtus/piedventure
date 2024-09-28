import time
from pathlib import Path

from .. import lib
from . import kroo2, mainroom


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Initialise the Title Art
    lib.display_art('titleart.ben')

    # Room description
    print('\n')
    time.sleep(1)
    print('This room is small, but has a pretty sweet looking computer')
    print('sat on a desk in the middle of it. Is that... YES!')
    print('Steam is installed, and it looks like the entire library of')
    print('games is installed! This is one epic gaming rig.')
    print('\nThe only way out is west, back the way you came... but...')
    print("shiny. Maybe it'd be rude NOT to sit down and game a little.")
    print('\nWhat would you like to do?')

    # Actions loop
    while True:
        nsewuh = input('> ').strip().lower()
        if nsewuh == 'n':
            print('WALL EQUALS TRUE.')
        elif nsewuh == 's':
            print('Nope. Wall.')
        elif nsewuh == 'w':
            # Call kroo2.py script
            kroo2.main(data_path)
            break
        elif nsewuh == 'e':
            print('You were going to go east, then you took a wall to the face.')
        elif nsewuh == 'u':
            print('\nYou sit and game. And game. And game. You forget about time,')
            print("and food, and people. You realise that you cannot get up. You can't")
            print('move. You are stuck to the chair.')
            time.sleep(4)
            print("\nDays go by. Weeks. You've played game after game, but...")
            print(
                '\nYour body is giving up. With your final breath you come to realise that',
            )
            print('you cannot live on gamerpoints alone.'
                  ' You close your eyes for the last time.')
            time.sleep(4)
            print('\n\nYOU ARE DEAD.')
            input('Press [ENTER] to try again...')
            mainroom.main(data_path)
            break
        elif nsewuh == 'h':
            print('You hug the computer. Nerd.')
        else:
            print(
                "I'm sorry, I don't understand you. Commands are: n, e, s, w, u and h.")

    print('Exiting the game room...')
