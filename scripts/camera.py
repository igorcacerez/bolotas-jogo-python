import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0, 0)
        
    def costum_draw(self, player):
        
        self.offset.x = player.rect.centerx - self.display.get_width() / 2
        self.offset.y = player.rect.centery - self.display.get_height() / 2
        
        for sprite in self.sprites():
            off_rect = sprite.rect.copy()
            off_rect.center -= self.offset
            self.display.blit(sprite.image, off_rect)