import time
from pathlib import Path

from .. import lib


def main(data_path: Path):
    # Clear the terminal (works for most terminals)
    print('\033c', end='')

    # Reset the lever state to 'off'
    lib.set_leverstate(data_path, 'off')

    # Initialise the Title Art
    lib.display_art('titleart.ben')
    print()

    # Storyline sequence
    time.sleep(1)
    print('You swallow the pill, and suddenly rainbows are all around you.')
    time.sleep(4)
    print("You look down to find that you're riding a unicorn. On a rainbow.")
    time.sleep(3)
    print()
    print('A motherfucking UNICORN.')
    time.sleep(4)
    print()
    print('This is ridiculous. Surely this is some kind of dream? You pinch')
    print("yourself to try and wake up. Wait, you're feeling dizzy...")
    time.sleep(5)
    print('You blink, and are surprised to find yourself laying in bed.')
    print("You check your phone - it's 5am, and definitely Thursday. Huh.")
    print('I guess it was all a dream.')
    time.sleep(7)
    print('You go to get out of bed and suddenly spot a tiny marble figurine on')
    print("your bedside table. It's a beautifully carved kitten.")
    time.sleep(5)
    print('How the hell did that get there?')
    time.sleep(5)
    print()
    print('Unable to work out what is dream and what is reality, you shrug your')
    print("shoulders and pick up the figurine. It hasn't transported you anywhere")
    print('this time... but how did it get here? What does it mean?')
    time.sleep(7)
    print("Your phone buzzes. It's a call from a withheld number. You don't usually")
    print('answer those, but you get the feeling that this call might be important.')
    time.sleep(5)
    print()
    print('You answer the call, and an electronic voice says five words to you')
    print('before the line goes dead.')
    time.sleep(3)
    print()
    print('Just five words.')
    time.sleep(7)
    print()
    print('THE KITTEN IS WATCHING YOU.')
    time.sleep(9)

    # Final artwork
    lib.display_art('bigfinish.ben')
    print()
    input('Press [ENTER] to exit...')
    print()
    print('\033c', end='')  # Clear the terminal again

    # Reinitialize the Title Art for the ending message
    lib.display_art('titleart.ben')
    print()
    print('Thank you for playing the demo of BashVenture. '
          'Pretty random storyline, I know,')
    print('but the aim was to show off the functionality, not win a Pulitzer Prize.')
    print()
    print("Whoever you are, wherever you're from - live long and prosper. Keep smiling!")
    print()
    print('                                                                - @BenNunney')
    print()

    # That's all, folks!
