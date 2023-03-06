import json
import pygame

from scripts.level import Level
from scripts.settings import * 

class Game: 
    def __init__(self):
        aux = json.load(open("assets/maps/maps.json"))
        self.active = True
        self.stage = 0
        self.maps = aux["maps"]
        self.current_level = Level(self.maps[self.stage])
        
        self.music = pygame.mixer.Sound("assets/sounds/bg.mp3")
        self.music.play(-1)
        
    def events(self, event):
        pass

    def draw(self):
        self.current_level.draw()
    
    def update(self):
        
        if self.current_level.active == False and self.current_level.gameover == False: 
            pygame.mixer.Sound("assets/sounds/next-stage.mp3").play()
            self.stage += 1
            self.current_level = Level(self.maps[self.stage])
        elif self.current_level.active == True and self.current_level.gameover == True:
            self.music.stop()
            pygame.mixer.Sound("assets/sounds/gameover.mp3").play()
            self.active = False
        
        self.current_level.update()