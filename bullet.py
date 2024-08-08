import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):  
    """A class to manage bullets fired from the rocket."""  

    def __init__(self, ai_game, arrow, shooter):  
        """Create a bullet object at the ship's current position."""  
        super().__init__()  
        self.screen = ai_game.screen  
        self.settings = ai_game.settings  
        self.color = self.settings.bullet_color  

        # Define the bullet's radius  
        self.radius = self.settings.bullet_width  # Assuming width is the diameter  
        self.arrow = arrow  
        
        # Set the initial position based on the shooter  
        if arrow == 0:  
            self.x = shooter.image_rect.right  
            self.y = shooter.image_rect.centery  
        elif arrow == 1:  
            self.x = shooter.image_rect.centerx  
            self.y = shooter.image_rect.top  
        elif arrow == 2:  
            self.x = shooter.image_rect.left  
            self.y = shooter.image_rect.centery  
        elif arrow == 3:  
            self.x = shooter.image_rect.centerx  
            self.y = shooter.image_rect.bottom  

        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)  

    def update(self):  
        if self.arrow == 0:  # Right  
            self.x += self.settings.bullet_speed  
        elif self.arrow == 1:  # Up  
            self.y -= self.settings.bullet_speed  
        elif self.arrow == 2:  # Left  
            self.x -= self.settings.bullet_speed  
        elif self.arrow == 3:  # Down  
            self.y += self.settings.bullet_speed  
        
        # Update the bullet's rectangle position  
        self.rect.topleft = (self.x, self.y)  

    def draw_bullet(self):  
        """Draw the bullet to the screen as a circle."""  
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)