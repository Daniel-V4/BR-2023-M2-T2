import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(BIRD, self.type)
        self.rect.y = 275