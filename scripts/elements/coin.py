import pygame
from scripts.obj import Obj 

class Coin(Obj):
    def __init__(self, pos, group, player, ui): 
        super().__init__("assets/coin/0.png", pos, group)
        
        self.music = pygame.mixer.Sound("assets/sounds/coin.mp3")
        self.ui = ui
        self.player = player
        self.speed = 1
        self.pontos = 5
       
    def colision(self):
        if pygame.sprite.collide_rect(self, self.player):
            self.kill()
            self.music.play()
            self.ui.score += self.pontos
            self.ui.coin += 1
            self.ui.text_coin.update_text(str(self.ui.coin))
            
        
    def update(self):
        self.animation(self.speed, 16, "assets/coin/")
        self.colision()
        return super().update()
        
    