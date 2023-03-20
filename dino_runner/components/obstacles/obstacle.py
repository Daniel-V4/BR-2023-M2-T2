import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()

        if self.image == BIRD:
            self.type = 0 if self.step_index < 5 else 1
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))