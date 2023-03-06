import pygame

from scripts.obj import Obj

class Ui:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.ui_group = pygame.sprite.Group()
        
        self.lifes = 3
        self.hud1 = Obj("assets/player/life.png", [0, 5], [self.ui_group])
        self.hud2 = Obj("assets/player/life.png", [74, 5], [self.ui_group])
        self.hud3 = Obj("assets/player/life.png", [144, 5], [self.ui_group])
        
    def count_lifes(self):
        if self.lifes == 2:
            self.hud3.kill()
        elif self.lifes == 1:
            self.hud2.kill()
        elif self.lifes == 0:
            self.hud1.kill()

    def draw(self):
        self.ui_group.draw(self.display)
        
    def update(self):
        self.count_lifes()