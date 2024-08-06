import sys

import pygame

from settings import Settings
from rocket_one import RocketOne

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
        
        self.rocket_one = RocketOne(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_event()
            self.show_element_screen()

    def check_event(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def show_element_screen(self):
        """fill screen with elements"""
        self.screen.fill(self.settings.backgroundColor)
        self.rocket_one.blitme()
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SpaceWar()
    ai.run_game()