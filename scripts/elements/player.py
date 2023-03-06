import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, colision_group):
        super().__init__(groups)
        
        self.tick = 0
        self.frame = 0
        self.image = pygame.image.load("assets/player/idle_1.png")
        self.rect = self.image.get_rect(topleft=pos)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_force = 15
        self.on_ground = False
        self.flip = False
        
        self.colision_group = colision_group
    
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.flip = True
            self.direction.x = -1
            self.animation(2, 12, "assets/player/walk/")
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.flip = False
            self.direction.x = 1
            self.animation(2, 12, "assets/player/walk/")
        else:
            self.direction.x = 0
            self.animation(2, 11, "assets/player/idle/")
            
        if key[pygame.K_SPACE] and self.on_ground:
            self.direction.y = -self.jump_force
            self.on_ground = False
    
    def move(self):
        self.rect.x += self.direction.x * self.speed
        
        if self.on_ground == False:
            self.image = pygame.image.load("assets/player/jump/0.png")
            self.image = pygame.transform.flip(self.image, self.flip, False)
    
    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def y_collision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
                    self.on_ground = True
                    
                if self.direction.y < 0:
                    self.direction.y = 0
                    self.rect.top = sprite.rect.bottom
                    
    def x_collision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                elif self.direction.x < 0:
                    self.rect.left = sprite.rect.right
         
    def animation(self, speed, n_img, path):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % n_img
            self.image = pygame.image.load(path+ str(self.frame) + ".png")
            self.image = pygame.transform.flip(self.image, self.flip, False)
        
    def update(self): 
        self.input()
        self.move()
        self.x_collision()
        self.gravity_force()
        self.y_collision()
       