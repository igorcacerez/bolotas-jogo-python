import pygame
from scripts.obj import Obj 

class Water(Obj):
    def __init__(self, pos, group): 
        super().__init__("assets/water/0.png", pos, group)
        
    def update(self):
        self.animation(1, 17, "assets/water/")
        return super().update()