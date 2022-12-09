import pygame

class Background():
    def __init__(self):
        self.background = pygame.image.load("fondo.jpg").convert()

    #def draw(self, screen):
        #screen.draw(self.background, [0, 0])