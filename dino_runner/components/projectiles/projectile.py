import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import PROJECTILE


class Projectile(Sprite):
    def __init__(self, player_y_position):
        self.image = PROJECTILE
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = player_y_position

    def update(self, game_speed):
        self.rect.x += game_speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))