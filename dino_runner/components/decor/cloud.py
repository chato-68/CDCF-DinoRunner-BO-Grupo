from pygame.sprite import Sprite

from dino_runner.utils.constants import CLOUD, CLOUD_TYPE, SCREEN_WIDTH
class Cloud(Sprite):
    def __init__(self, image, type):
        self.image = CLOUD
        self.type = CLOUD_TYPE
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def update(self, game_speed, obstacle):
        self.rect.x -= game_speed
        

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)