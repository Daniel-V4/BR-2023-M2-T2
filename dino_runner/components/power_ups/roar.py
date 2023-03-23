from dino_runner.utils.constants import ROAR, SHIELD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Roar(PowerUp):
    def __init__(self):
        self.image = ROAR
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)