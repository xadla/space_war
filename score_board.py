import pygame

pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)

class ScoreBoard:
    def __init__(self, ai_screen) -> None:
        
        self.screen = ai_screen.screen
        
        self.heal1 = 5
        self.heal2 = 5
        
        self.player_one = my_font.render("Player 1", False, (255, 255, 255))
        self.heal_one = my_font.render(f"Heal: {self.heal1}", False, (255, 255, 255))
    
        self.player_two = my_font.render("Player 2", False, (0, 255, 0))
        self.heal_two = my_font.render(f"Heal: {self.heal2}", False, (0, 255, 0))
        
    def blitme(self):
        self.screen.blit(self.player_one, (0, 0))
        self.screen.blit(self.heal_one, (0, 40))
        self.screen.blit(self.player_two, (1520, 0))
        self.screen.blit(self.heal_two, (1520, 40))

    def kill_one(self):
        self.heal1 -= 1
        self.heal_one = my_font.render(f"Heal: {self.heal1}", False, (255, 255, 255))
    
    def kill_two(self):
        self.heal2 -= 1
        self.heal_two = my_font.render(f"Heal: {self.heal2}", False, (0, 255, 0))
        
    def return_all(self):
        self.heal1 = 5
        self.heal2 = 5
        self.heal_one = my_font.render(f"Heal: {self.heal1}", False, (255, 255, 255))
        self.heal_two = my_font.render(f"Heal: {self.heal2}", False, (0, 255, 0))