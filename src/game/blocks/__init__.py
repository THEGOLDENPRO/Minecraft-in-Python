from ursina import Entity, Vec3, color
from ursina import Color

class Voxel(Entity):
    def __init__(self, position:Vec3, colour:Color):
        self.__position = position
        self.__colour = colour

        super().__init__(model='cube', position=self.__position, color=self.__colour)

    def update(self):
        #print(self.hovered)

        if self.hovered:
            self.color = color.gray
        else:
            self.color = self.__colour