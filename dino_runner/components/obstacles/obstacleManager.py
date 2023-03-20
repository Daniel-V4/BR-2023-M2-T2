import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        chosen_object = random.randint(0, 3)
        if len(self.obstacles) == 0:
            if chosen_object == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif chosen_object == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif chosen_object == 2:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)