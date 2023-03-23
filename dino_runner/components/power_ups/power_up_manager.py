import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.roar import Roar


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score, player):
        power_up_list = (Hammer(),
                          Shield(),
                          Roar()
                          )
        if len(self.power_ups) == 0 and self.when_appears == score and not player.has_power_up:
            self.when_appears += random.randint(300, 500)
            self.power_ups.append(random.choice(power_up_list))
        elif self.when_appears == score and player.has_power_up:
            self.when_appears += random.randint(300, 500)

    def update(self, score, game_speed, player):
        self.generate_power_up(score, player)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if isinstance(power_up, Shield):
                    self.apply_power_up(player, power_up)
                elif isinstance(power_up, Hammer):
                    self.apply_power_up(player, power_up)
                elif isinstance(power_up, Roar):
                    player.roar_available = True
                try: self.power_ups.remove(power_up)
                except: continue
    
    def apply_power_up(self, player, power_up):
        player.has_power_up = True
        player.type = power_up.type
        player.power_up_time = power_up.start_time + (power_up.duration * 1000)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)