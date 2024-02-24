import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        
        self.screen = ai.screen
        self.settings = ai.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_heght)
        self.rect.midtop = ai.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)