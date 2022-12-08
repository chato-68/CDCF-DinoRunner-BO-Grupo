import random
from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD



class Bird(Obstacle):
    
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(235,320)
        self.steps = 0
        
    
    def draw(self, screen):
        if self.steps >= 9:
            self.steps = 0
        screen.blit(self.image[self.steps//5], self.rect)
        self.steps +=1