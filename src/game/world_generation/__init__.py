from ursina import color

from ..blocks import Voxel, Vec3

class WorldGeneration():
    def __init__(self, radius=5) -> None:
        self.__radius = (radius - 1)

    def start(self) -> bool:
        """Start generating the world."""
        Voxel(
            Vec3(0, 0, 0),
            color.blue
        )

        # North
        for num in range(self.__radius):
            Voxel(
                Vec3(0, num+1, 0),
                color.red
            )

        # East
        for num in range(self.__radius):
            Voxel(
                Vec3(num+1, 0, 0),
                color.green
            )

        # South
        for num in range(self.__radius):
            Voxel(
                Vec3(0, -(num+1), 0),
                color.yellow
            )

        # West
        for num in range(self.__radius):
            Voxel(
                Vec3(-(num+1), 0, 0),
                color.black
            )

        return True