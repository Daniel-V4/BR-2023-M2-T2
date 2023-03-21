import random
import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):

    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = 275
    
    def draw(self, screen):
        self.type = 0 if self.step_index < 5 else 1
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0

        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))