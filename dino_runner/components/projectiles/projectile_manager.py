import random
import pygame

from dino_runner.components.projectiles.projectile import Projectile


class ProjectileManager:
    def __init__(self):
        self.projectiles = []

    def generate_projectile(self, player_y):
            self.projectiles.append(Projectile(player_y))

    def update(self, game_speed, obstacle_manager):
        for projectile in self.projectiles:
            projectile.update(game_speed)
            for obstacle in obstacle_manager.obstacles:
                if obstacle.rect.colliderect(projectile.rect):
                    obstacle_manager.obstacles.remove(obstacle)
                    self.projectiles.remove(projectile)

    def draw(self, screen):
        for projectile in self.projectiles:
            projectile.draw(screen)