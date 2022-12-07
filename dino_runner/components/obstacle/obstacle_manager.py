import random
import pygame
from dino_runner.components.obstacle.bird import Bird

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_siz = random.randint(0,2)
            if cactus_siz == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_siz == 1:
                self.obstacles.append(Bird(BIRD))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dino.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

