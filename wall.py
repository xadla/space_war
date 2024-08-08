import pygame

class Wall():
    def __init__(self, ai_screen, x, y) -> None:
        
        self.screen = ai_screen.screen
        self.screen_rect = ai_screen.screen.get_rect()
        
        self.image = pygame.image.load("images/wall.png").convert()
        self.image_rect = self.image.get_rect()

        self.image_rect.x = x
        self.image_rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)