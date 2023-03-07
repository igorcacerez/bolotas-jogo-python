import pygame

class Obj(pygame.sprite.Sprite):

    def __init__(self, img, pos, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = pos)

        self.frame = 0
        self.tick = 0
        
    def scale(self, scale): 
        image = self.image
        width = image.get_rect().width
        height = image.get_rect().height
        
        self.image = pygame.transform.scale(image, (width*scale, height*scale))
    
    def animation(self, speed, n_img, path, scale = 1):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % n_img
            
            image = pygame.image.load(path+ str(self.frame) + ".png")
            width = image.get_rect().width
            height = image.get_rect().height
            
            self.image = pygame.transform.scale(image, (width*scale, height*scale))

