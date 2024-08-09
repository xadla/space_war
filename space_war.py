import sys

import pygame

from settings import Settings
from rocket_one import RocketOne
from rocket_two import RocketTwo
from wall import Wall
from bullet import Bullet
from game_music import GameMusic
from score_board import ScoreBoard

class SpaceWar:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screenWidth, self.settings.screenHeight))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Space War")
        
        self.gameActive = True
        self.win1 = False
        self.win2 = False
        
        self.walls = []
        self.create_walls()
        
        self.rocket_one = RocketOne(self)
        self.rocket_two = RocketTwo(self)
        self.rocket_one.set_opponent(self.rocket_two)
        
        self.bullets_one = pygame.sprite.Group()
        self.bullets_two = pygame.sprite.Group()
        
        self.last_move_one = 0
        self.last_move_two = 2

        self.music = GameMusic()
        self.music.play()
        
        self.scoreBoard = ScoreBoard(self)
        
        self.heal1 = 5
        self.heal2 = 5
        
        pygame.font.init()
        my_font = pygame.font.SysFont("Comic Sans MS", 60)
        
        self.message_one_win = my_font.render("Player 1 is winner!", False, (200, 0, 0))
        self.message_one_win_rect = self.message_one_win.get_rect()
        self.message_one_win_rect.center = self.screen_rect.center
        self.message_two_win = my_font.render("Player 2 is winner!", False, (200, 0, 0))
        self.message_two_win_rect = self.message_two_win.get_rect()
        self.message_two_win_rect.center = self.screen_rect.center
        
        self.message_return = my_font.render("Press enter to play again!", False, (200, 0, 0))
        self.message_return_rect = self.message_return.get_rect()
        self.message_return_rect.midtop = self.screen_rect.midtop

    def create_walls(self):

        temp = 225
        for i in range(8):
            wall = Wall(self, 750, temp)
            self.walls.append(wall)
            temp += 75
        temp = 0
        for i in range(4):
            wall = Wall(self, temp, 100)
            self.walls.append(wall)
            temp += 75
        temp = 100
        for i in range(3):
            wall = Wall(self, 300, temp)
            self.walls.append(wall)
            temp += 75
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
            self._check_winner()
            self.clock.tick(60)

    def _update_bullets(self):  
        self.bullets_one.update()  
        self.bullets_two.update()  

        # Remove bullets outside screen bounds and check for collisions  
        for bullet in self.bullets_one.copy():  
            if (bullet.rect.bottom < 110 or  
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
                self.scoreBoard.kill_two()
                self.heal2 -= 1
                self.rocket_two.return_place()

        for bullet in self.bullets_two.copy():
            if (bullet.rect.bottom < 110 or  
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
                self.scoreBoard.kill_one()
                self.heal1 -= 1
                self.rocket_one.return_place()

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
        if self.gameActive:
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
                
            if event.key == pygame.K_SPACE:
                self._fire_bullet_one()
            if event.key == pygame.K_RCTRL:
                self._fire_bullet_two()
        else:
            if event.key == pygame.K_RETURN:
                self.gameActive = True
                self.win1 = False
                self.win2 = False
                self.heal1 = 5
                self.heal2 = 5
                self.scoreBoard.return_all()
                self.rocket_one.return_place()
                self.rocket_two.return_place()

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
    
    def _check_winner(self):
        if self.heal1 <= 0:
            self.win2 = True
            self.gameActive = False
        elif self.heal2 <= 0:
            self.win1 = True
            self.gameActive = False

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
        self.scoreBoard.blitme()
        
        if self.win1:
            self.screen.blit(self.message_one_win, self.message_one_win_rect)
            self.screen.blit(self.message_return, self.message_return_rect)
        elif self.win2:
            self.screen.blit(self.message_two_win, self.message_two_win_rect)
            self.screen.blit(self.message_return, self.message_return_rect)

        pygame.display.flip()
        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SpaceWar()
    ai.run_game()