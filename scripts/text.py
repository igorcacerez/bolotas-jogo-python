import pygame


class Text:

    def __init__(self, font, size, text, color, pos):

        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font(font,size)
        self.text = self.font.render(text, True,color).convert_alpha()
        self.position = pos
        self.text_alpha = 255
        self.alpha_speed = 5
        self.color = color
        
        self.text_react = self.text.get_rect(center = pos)

    def draw(self):
        self.display.blit(self.text, self.position)
        
    def draw_center(self):
        self.display.blit(self.text, self.text_react)
    
    def update_text(self, text, color = None):
        color = color if color else self.color 
        self.text = self.font.render(text, True, color).convert_alpha()

    def drawFade(self):

        if self.text_alpha > 0:
            self.text_alpha -= self.alpha_speed
        else:
            self.text_alpha = 255

        self.text.set_alpha(self.text_alpha)
        self.display.blit(self.text, self.position)