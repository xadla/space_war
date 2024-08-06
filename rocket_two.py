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
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
        