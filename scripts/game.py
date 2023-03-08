import json
import pygame
from scripts.elements.ui import Ui

from scripts.level import Level
from scripts.settings import *
from scripts.text import Text 

class Game: 
    def __init__(self):
        aux = json.load(open("assets/maps/maps.json"))
        self.active = True
        self.stage = 0
        self.maps = aux["maps"]
        self.hub_ui = Ui()
        self.current_level = Level(self.maps[self.stage], self.hub_ui)
        self.text_level = Text("assets/fonts/airstrike.ttf", 25, str(self.stage + 1), SECONDARY_COLOR, [WIDTH / 2, 15])
        
        self.music = pygame.mixer.Sound("assets/sounds/bg.mp3")
        self.music.play(-1)
        
    def events(self, event):
        pass

    def draw(self):
        self.current_level.draw()
        self.text_level.draw_center()
    
    def update(self):
        
        if self.current_level.active == False and self.current_level.gameover == False: 
            pygame.mixer.Sound("assets/sounds/next-stage.mp3").play()
            self.stage += 1
            
            if self.stage >= len(self.maps):
                self.current_level = Level(self.maps[self.stage], self.hub_ui)
                self.text_level.update_text(str(self.stage + 1))
            else :
                self.current_level = Level(self.maps[self.stage], self.hub_ui)
                self.text_level.update_text(str(self.stage + 1))
                
        elif self.current_level.active == True and self.current_level.gameover == True:
            self.music.stop()
            pygame.mixer.Sound("assets/sounds/gameover.mp3").play()
            self.active = False
        
        self.current_level.update()