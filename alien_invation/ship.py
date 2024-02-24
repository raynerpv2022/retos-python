
import pygame

class Ship():
    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.imagen_path = "images/ship.bmp"
        self.image = pygame.image.load(self.imagen_path)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False
        self.settings = ai.settings
        self.x = float(self.rect.x)

    def update(self):
        
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
             
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)
