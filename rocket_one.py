import pygame

class RocketOne:
    def __init__(self, ai_screen) -> None:
        """class for rocket one"""
        self.screen = ai_screen.screen
        self.screen_rect = ai_screen.screen.get_rect()
        
        self.image = pygame.image.load("images/rocket1.png").convert()
        self.image_rect = self.image.get_rect()
        
        self.image_rect.midleft = self.screen_rect.midleft
        
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
        