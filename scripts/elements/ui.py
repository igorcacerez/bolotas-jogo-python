import pygame

from scripts.obj import Obj
from scripts.text import Text
from scripts.settings import *

class Ui:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.ui_group = pygame.sprite.Group()
        
        self.score = 0
        self.coin = 0
        self.lifes = 3
        
        self.hud1 = Obj("assets/player/life.png", [0, 5], [self.ui_group])
        self.hud1.scale(0.5)
        
        self.hud2 = Obj("assets/player/life.png", [30, 5], [self.ui_group])
        self.hud2.scale(0.5)
        
        self.hud3 = Obj("assets/player/life.png", [60, 5], [self.ui_group])
        self.hud3.scale(0.5)
        
        # self.text = Text("assets/fonts/airstrike.ttf",25,"Pontos:", "white", [WIDTH - 200, 5])
        self.imgCoin = Obj("assets/coin/0.png", [WIDTH - 100, 5], [self.ui_group])
        self.text_coin = Text("assets/fonts/airstrike.ttf",25, str(self.coin), COIN_COLOR, [WIDTH - 70, 5])
        
    def count_lifes(self):
        if self.lifes == 2:
            self.hud3.kill()
        elif self.lifes == 1:
            self.hud2.kill()
        elif self.lifes == 0:
            self.hud1.kill()
            
    
    def remove_coin(self):
        self.coin -= 100
        self.text_coin.update_text(str(self.coin))

    def draw(self):
        self.ui_group.draw(self.display)
        self.text_coin.draw()
        
    def update(self):
        self.count_lifes()
        self.imgCoin.animation(1, 16, "assets/coin/", 0.6)