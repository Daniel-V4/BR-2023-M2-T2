import random
import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from dino_runner.utils.functions import Animation_loop


class Bird(Obstacle):

    def __init__(self):
        self.animation_loop = Animation_loop()
        super().__init__(BIRD, 0)
        places = (200, 275, 300)
        self.rect.y = random.choice(places)
    
    def draw(self, screen):
        screen.blit(self.image[self.animation_loop()], (self.rect.x, self.rect.y))