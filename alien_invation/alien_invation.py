import pygame, sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvation():
        #  Class to manage game assets and behavior.
    def __init__(self):
        # initialize the game, and create game resourse.
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.width = self.screen.get_rect().width
        # self.settings.height = self.screen.get_rect().height
        
        pygame.display.set_caption(self.settings.caption)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  
        for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
         new_bullet = Bullet(self)
         self.bullets.add(new_bullet)

     
    def _check_key_down(self, event):
            if event.key == pygame.K_q:
                 sys.exit()
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.move_left = True
            elif event.key == pygame.K_SPACE:
                 self._fire_bullet()

    def _check_key_up(self, event):
         
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.move_left = False
         
         
    
    def _check_event(self):
        for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                         sys.exit()
                    elif event.type == pygame.KEYDOWN: 
                        self._check_key_down(event)
                    elif event.type == pygame.KEYUP  :
                        self._check_key_up(event)
                     
                         
                     
                         
                    
         
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_event()
            self.ship.update()
            self.bullets.update()
            # Make the most recently drawn screen visible.
            self._update_screen()
               

if __name__ =="__main__":
    #  make a game instance and run the game
     ai = AlienInvation()
     ai.run_game()