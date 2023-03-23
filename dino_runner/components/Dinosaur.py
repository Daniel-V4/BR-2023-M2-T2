import pygame
from pygame.sprite import Sprite

from dino_runner.utils.functions import Animation_loop
from dino_runner.components.projectiles.projectile_manager import ProjectileManager
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD,   RUNNING_SHIELD, HAMMER_TYPE, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False

        self.animation_loop = Animation_loop()
        self.projectile_manager = ProjectileManager()

        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.roar_available = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump(user_input)
        if self.dino_duck:
            self.duck()

        if user_input[pygame.K_RIGHT] and self.roar_available:
            self.projectile_manager.generate_projectile(self.dino_rect.y)
            self.roar_available = False

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump and user_input[pygame.K_DOWN]:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    def update_projectile(self, game_speed, obstacle_manager):
        self.projectile_manager.update(game_speed, obstacle_manager)

    def run(self):
        self.image = RUN_IMG[self.type][self.animation_loop()]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

    def jump(self, user_input):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            if user_input[pygame.K_DOWN] and self.jump_vel > 0:
                self.jump_vel = 0
            elif user_input[pygame.K_DOWN]:
                self.jump_vel -= 3.2
            else:
                self.jump_vel -= 0.8

        if self.dino_rect.y > Y_POS:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.animation_loop()]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 35
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def draw_projectile(self, screen):
        self.projectile_manager.draw(screen)


