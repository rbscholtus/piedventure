from pathlib import Path

art_dir = Path(__file__).parent.parent / 'art'
script_dir = Path(__file__).parent.parent / 'script'


def reset_logic(data_path: Path) -> None:
    """Reset the game logic for lever."""
    path = data_path / 'leverlogic.ben'
    path.write_text('off')


def get_leverstate(data_path) -> str:
    path = data_path / 'leverlogic.ben'
    return path.read_text().strip()


def set_leverstate(data_path: Path, state: str) -> None:
    path = data_path / 'leverlogic.ben'
    path.write_text(state)


def display_art(file_path):
    """Display ASCII art from the file."""
    path = art_dir / file_path
    print(path.read_text())


def display_script(file_path):
    """Display script from the file."""
    print((script_dir / file_path).read_text())
