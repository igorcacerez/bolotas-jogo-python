import pygame

from scripts.obj import Obj

class Enemy(Obj):
    def __init__(self, pos, player, all_sprites, morreu):
        self.group = pygame.sprite.Group()
        self.player = player
        self.morreu = morreu
        super().__init__("assets/enemy/0.png", pos, [self.group, all_sprites])
        
    def colision(self):
        if pygame.sprite.collide_rect(self, self.player):
            self.morreu()
        
    def update(self):
        self.animation(20, 2, "assets/enemy/")
        self.colision()
        return super().update()

            