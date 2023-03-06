import pygame
from scripts.settings import *

class Fade:

    def __init__(self, speed):
        
        self.display = pygame.display.get_surface()
        self.surface = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.surface.fill("black")

        self.alpha = 255
        self.speed = speed
    
    def draw(self):

        if self.alpha > 0:
            self.alpha -= self.speed

        self.surface.set_alpha(self.alpha)
        self.display.blit(self.surface, [0,0])