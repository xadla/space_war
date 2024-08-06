import sys

import pygame

from settings import Settings
from rocket_one import RocketOne
from rocket_two import RocketTwo

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
        self.rocket_two = RocketTwo(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        """fill screen with elements"""
        self.screen.fill(self.settings.backgroundColor)
        self.rocket_one.blitme()
        self.rocket_two.blitme()

        pygame.display.flip()
        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SpaceWar()
    ai.run_game()