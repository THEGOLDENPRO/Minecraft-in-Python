from ursina import Keys, Vec3
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(position=Vec3(0, 100, 0))
        #TODO: Where I left off