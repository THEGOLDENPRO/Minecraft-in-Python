import sys

from ursina import Ursina
from ursina import held_keys, Keys
from ursina import Entity

from .player import Player
from .world_generation import WorldGeneration
from .window import Window

# Initialize before Ursina.
# ---------------------------
Window()

app = Ursina()

# Main entity
# ----------------
class Game(Entity):
    """Main game entity."""
    def __init__(self):
        super().__init__()

        WorldGeneration().start()

        Player()

    def update(self):

        # Exit game UwU
        #-----------------
        if held_keys[Keys.escape]:
            sys.exit(0)


def start():
    """Start the game."""

    # Initializing main game class.
    Game()

    app.run()