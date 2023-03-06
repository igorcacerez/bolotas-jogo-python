import sys
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class GameOver(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimatedBg("assets/menu/bg.png", [0, 0], [-WIDTH, 0], [self.all_sprites])
        self.title = Obj("assets/menu/gameover.png", [0, 0], [self.all_sprites])
        
        self.btn_play = Button("white", 64, 520, 250, 64, "Voltar", self.next_scene)
        self.btn_quit = Button("white", 64, 600, 250, 64, "Sair", self.quitGame)

    def next_scene(self):
        self.active = False
        
    def quitGame(self):
        pygame.quit()
        sys.exit()
    
    def events(self, event):
        self.btn_play.events(event)
        self.btn_quit.events(event)
        return super().events(event)

    def update(self):
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()