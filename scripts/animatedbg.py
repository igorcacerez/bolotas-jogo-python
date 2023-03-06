import pygame
from scripts.obj import Obj
from scripts.settings import *

class AnimatedBg:

    def __init__(self, img, pos1,pos2, group):
        self.bg = Obj(img,pos1, group)
        self.bg2 = Obj(img,pos2, group)
    
    def update(self):

        self.bg.rect.x += 1
        self.bg2.rect.x += 1

        if self.bg.rect.x > WIDTH:
            self.bg.rect.x = 0
        elif self.bg2.rect.x == 0:
            self.bg2.rect.x = -WIDTH