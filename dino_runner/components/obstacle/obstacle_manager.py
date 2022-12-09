import random
import pygame
from dino_runner.components.obstacle.bird import Bird

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.cactus_large import Cactus_Large
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_siz = random.randint(0,2)
            if cactus_siz == 0:
                self.obstacles.append(Cactus_Large(LARGE_CACTUS))
            elif cactus_siz == 1:
                self.obstacles.append(Bird(BIRD))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dino.plus_heart == True:
                pygame.time.delay(100)
                game.player_heart_manager.add_heart()
            elif game.dino.dino_rect.colliderect(obstacle.rect) and game.dino.shield == False:
                pygame.time.delay(100)
                game.player_heart_manager.reduce_heart()
            

                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
                    game.dino.has_live = True
                else:
                    game.dino.has_live = False
                    pygame.time.delay(300)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

