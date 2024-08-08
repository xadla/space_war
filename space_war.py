import sys

import pygame

from settings import Settings
from rocket_one import RocketOne
from rocket_two import RocketTwo
from wall import Wall
from bullet import Bullet

class SpaceWar:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("Space War")
        
        self.walls = []
        self.create_walls()
        
        self.rocket_one = RocketOne(self)
        self.rocket_two = RocketTwo(self)
        self.rocket_one.set_opponent(self.rocket_two)
        
        self.bullets_one = pygame.sprite.Group()
        self.bullets_two = pygame.sprite.Group()
        
        self.last_move_one = 0
        self.last_move_two = 2

    def create_walls(self):
        
        temp = 225
        for i in range(8):
            wall = Wall(self, 750, temp)
            self.walls.append(wall)
            temp += 75
        temp = 0
        for i in range(4):
            wall = Wall(self, 300, temp)
            self.walls.append(wall)
            temp += 75
        temp = 300
        for i in range(3):
            wall = Wall(self, temp, 300)
            self.walls.append(wall)
            temp -= 75
        temp = 1020
        for i in range(4):
            wall = Wall(self, 1200, temp)
            self.walls.append(wall)
            temp -= 75
        temp = 1200
        for i in range(3):
            wall = Wall(self, temp, 720)
            self.walls.append(wall)
            temp += 75

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.rocket_one.update_location()
            self.rocket_two.update_location()
            self._check_events()
            self._update_screen()
            self._update_bullets()
            self.clock.tick(60)


    def _update_bullets(self):  
        self.bullets_one.update()  
        self.bullets_two.update()  

        # Remove bullets outside screen bounds and check for collisions  
        for bullet in self.bullets_one.copy():  
            if (bullet.rect.bottom < 0 or  
                bullet.rect.top > self.screen.get_rect().bottom or  
                bullet.rect.left < 0 or   
                bullet.rect.right > self.screen.get_rect().right):  
                self.bullets_one.remove(bullet)  
            
            # Check for wall collisions  
            for wall in self.walls:  
                if wall.image_rect.colliderect(bullet.rect):  
                    self.bullets_one.remove(bullet)  
                    break  # Bullet removed; no need to check other walls  

            # Check for collisions with rocket_two  
            if bullet.rect.colliderect(self.rocket_two.image_rect):  
                self.bullets_one.remove(bullet)  

        for bullet in self.bullets_two.copy():  
            if (bullet.rect.bottom < 0 or  
                bullet.rect.top > self.screen.get_rect().bottom or  
                bullet.rect.left < 0 or   
                bullet.rect.right > self.screen.get_rect().right):  
                self.bullets_two.remove(bullet)  
            
            # Check for wall collisions  
            for wall in self.walls:  
                if wall.image_rect.colliderect(bullet.rect):  
                    self.bullets_two.remove(bullet)  
                    break  # Bullet removed; no need to check other walls  

            # Check for collisions with rocket_one  
            if bullet.rect.colliderect(self.rocket_one.image_rect):  
                self.bullets_two.remove(bullet)

    def _fire_bullet_one(self):
        if len(self.bullets_one) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.last_move_one, self.rocket_one)
            self.bullets_one.add(new_bullet)

    def _fire_bullet_two(self):
        if len(self.bullets_two) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.last_move_two, self.rocket_two)
            self.bullets_two.add(new_bullet)

    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_w:
            self.rocket_one.moving_up = True
        elif event.key == pygame.K_a:
            self.rocket_one.moving_left = True
        elif event.key == pygame.K_s:
            self.rocket_one.moving_down = True
        elif event.key == pygame.K_d:
            self.rocket_one.moving_right = True
        
        if event.key == pygame.K_RIGHT:
            self.rocket_two.moving_right = True
        elif event.key == pygame.K_UP:
            self.rocket_two.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket_two.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket_two.moving_left = True
            
        if event.key == pygame.K_c:
            self._fire_bullet_one()
        if event.key == pygame.K_n:
            self._fire_bullet_two()

    def _keyup_events(self, event):
        if event.key == pygame.K_w:
            self.rocket_one.moving_up = False
            self.last_move_one = 1
        elif event.key == pygame.K_a:
            self.rocket_one.moving_left = False
            self.last_move_one = 2
        elif event.key == pygame.K_s:
            self.rocket_one.moving_down = False
            self.last_move_one = 3
        elif event.key == pygame.K_d:
            self.rocket_one.moving_right = False
            self.last_move_one = 0
        
        if event.key == pygame.K_RIGHT:
            self.rocket_two.moving_right = False
            self.last_move_two = 0
        elif event.key == pygame.K_UP:
            self.rocket_two.moving_up = False
            self.last_move_two = 1
        elif event.key == pygame.K_DOWN:
            self.rocket_two.moving_down = False
            self.last_move_two = 3
        elif event.key == pygame.K_LEFT:
            self.rocket_two.moving_left = False
            self.last_move_two = 2

    def _update_screen(self):
        """fill screen with elements"""
        self.screen.fill(self.settings.backgroundColor)
        self.rocket_one.blitme()
        self.rocket_two.blitme()
        for bullet in self.bullets_one.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets_two.sprites():
            bullet.draw_bullet()
        for wall in self.walls:
            wall.blitme()

        pygame.display.flip()
        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SpaceWar()
    ai.run_game()