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
        
    def events(self, event):
        pass

    def draw(self):
        self.current_level.draw()
    
    def update(self):
        
        if self.current_level.active == False and self.current_level.gameover == False: 
            self.stage += 1
            self.current_level = Level(self.maps[self.stage])
        elif self.current_level.active == True and self.current_level.gameover == True:
            self.active = False
        
        self.current_level.update()