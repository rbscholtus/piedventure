from __future__ import annotations

import shutil
import tempfile
import time
import uuid
from pathlib import Path

from .rooms import start


def copy_game_files(newplayer: Path):
    # Copy the necessary directories for the new player instance
    logic_dir = Path(__file__).parent / 'logic'
    shutil.copytree(logic_dir, newplayer / 'logic')


def remove_game_files(newplayer: Path):
    # Remove the temporary game instance after the game ends
    shutil.rmtree(newplayer)


def load_game():
    # Simulate loading screen
    print('Loading...')
    time.sleep(4)


def start_game(newplayer: Path):
    start.main(newplayer)


def main():
    try:
        newplayer = Path(tempfile.gettempdir(), str(uuid.uuid4())).resolve()
        newplayer.mkdir()
        copy_game_files(newplayer)
        load_game()
        start_game(newplayer)
    except KeyboardInterrupt:
        print('Ctrl-C pressed by user')
    finally:
        remove_game_files(newplayer)


if __name__ == '__main__':
    main()
