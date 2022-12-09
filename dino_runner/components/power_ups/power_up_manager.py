from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.plus_heart import PlusHeart
import random
import pygame

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0 

    def update(self, points, game_speed, player):
        self.generate_power_up_shield(points)
        self.generate_power_up_plus_heart(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if (player.dino_rect.colliderect(power_up.rect)):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.heart = True
                player.type = power_up.type
                power_up.start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = power_up.start_time + (time_random * 1000)

                self.power_ups.remove(power_up)

    def generate_power_up_shield(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(self.when_appears + 200, self.when_appears + 500)
                self.power_ups.append(Shield())

    def generate_power_up_plus_heart(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(50, 100)
                self.power_ups.append(PlusHeart())

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reste_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points