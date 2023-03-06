import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.camera import Camera
from scripts.elements.player import Player
from scripts.elements.ui import Ui
from scripts.fade import Fade
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Level():

    def __init__(self, worldmap):
        
        self.display = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.colision_sprites = pygame.sprite.Group()
        self.bg_group = pygame.sprite.Group()
        
        Obj("assets/bg/bg.png", [0, 0], [self.bg_group])
        
        self.gameover = False
        self.worldmap = worldmap
        self.active = True
        self.fade = Fade(5)
        self.finish = Obj("assets/title/finish.png", [0, 0], [self.all_sprites])
        self.tick = 0
        self.player = Player([0, 0], [self.all_sprites], self.colision_sprites)
        
        self.generate_map()
        
        self.hud_ui = Ui()

    def generate_map(self):
        for row_index, row in enumerate(self.worldmap):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == "X":
                    Obj("assets/title/tile.png", [x, y], [self.all_sprites, self.colision_sprites])
                elif col == "B":
                    Obj("assets/title/bloco.png", [x, y], [self.all_sprites, self.colision_sprites])
                elif col == "P":
                    self.player.rect.x = x
                    self.player.rect.y = y
                elif col == "C":
                    self.finish.rect.x = x
                    self.finish.rect.y = y
    
    def events(self, event):
        pass 
    
    def draw(self):
        self.bg_group.draw(self.display)
        self.all_sprites.costum_draw(self.player)
        self.hud_ui.draw()
        self.fade.draw()
                
    def next_stage(self):
        if self.player.rect.colliderect(self.finish.rect):
            self.active = False
            
    def reset_position(self):
        if self.player.rect.y > HEIGHT:
            self.player.rect.x = 0
            self.player.rect.y = 0
            self.hud_ui.lifes -= 1
            
            if self.hud_ui.lifes < 0:
                self.gameover = True
                
    def update(self):
        self.all_sprites.update()
        self.next_stage()
        self.reset_position()
        self.hud_ui.update()
        
        
        
