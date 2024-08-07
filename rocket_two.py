import pygame

class RocketTwo:
    def __init__(self, ai_screen) -> None:
        """class for rocket one"""
        self.screen = ai_screen.screen
        self.screen_rect = ai_screen.screen.get_rect()
        
        self.image = pygame.image.load("images/rocket2.png").convert()
        self.image_rect = self.image.get_rect()
    
        self.image_rect.midright = self.screen_rect.midright
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        self.speed = ai_screen.settings.player_speed
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

    def update_location(self):
        if self.moving_left and self.image_rect.x > 0:  
            self.image_rect.x -= self.speed 
        elif self.moving_right and self.image_rect.x < self.screen_rect.right - 80:  
            self.image_rect.x += self.speed  

        if self.moving_up and self.image_rect.y > 0:  
            self.image_rect.y -= self.speed 
        elif self.moving_down and self.image_rect.y < self.screen_rect.bottom - 80: 
            self.image_rect.y += self.speed