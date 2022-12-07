import random
from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD



class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(235,320)
        self.steps = 0
    def fly(self):
        self.image = self.fly[BIRD][0] if self.steps <=1 else self.fly [BIRD][1]
        self.steps += 1
        if self.steps <= 1:
            self.steps == 0