import pygame

from scripts.text import Text
from scripts.settings import *

class Button: 
    
    def __init__(self, color, x, y, width = 250, height = 64, texto = ' ', call_back = None):
        self.display = pygame.display.get_surface()
        self.color = color
        self.texto = texto
        self.text_color = SECONDARY_COLOR
        self.react = pygame.Rect(x,y,width,height)
        
        self.text = Text(
            "assets/fonts/airstrike.ttf", 
            40,
            texto, 
            self.text_color, 
            [(x + self.react.width / 2), (y + self.react.height / 2)]
        )
        
        self.call_back = call_back
    
    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.react.collidepoint(event.pos):
                self.color = SECONDARY_COLOR
                self.text.update_text(self.texto, WHITE_COLOR)
            else:
                self.color = WHITE_COLOR
                self.text.update_text(self.texto, SECONDARY_COLOR)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.react.collidepoint(event.pos):
                self.call_back()
    
    def draw(self):
        pygame.draw.rect(self.display, self.color, self.react)
        self.text.draw_center()