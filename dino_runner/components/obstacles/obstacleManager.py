import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, SHIELD_TYPE, HAMMER_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(SMALL_CACTUS),
            Cactus(LARGE_CACTUS),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,2)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.reset_game()
                    break
                elif game.player.type == SHIELD_TYPE:
                    continue
                elif game.player.type == HAMMER_TYPE:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
    def reset_obstacles(self):
        self.obstacles = []