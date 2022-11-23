from enum import Enum
from ursina import load_texture

class BlockTextures(Enum):
    """Enum class containing all the ursina minecraft block textures available."""
    DIRT_TEXTURE = load_texture('assets/dirt_block.png')
    GRASS_TEXTURE = load_texture('assets/grass_block.png')
    STONE_TEXTURE = load_texture('assets/stone_block.png')
    BRICK_TEXTURE = load_texture('assets/brick_block.png')

class OtherTextures(Enum):
    SKY_TEXTURE = load_texture('assets/skybox.png')
    ARM_TEXTURE = load_texture('assets/arm_texture.png')
        
from . import *