from ursina import window

class Window():
    """The game window."""
    def __init__(self):
        window.title = "Minecraft.py"

        window.borderless = False