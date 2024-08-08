class Settings:
    """class for save settings data"""
    def __init__(self) -> None:
        
        # screen settings
        self.screenWidth = 1600
        self.screenHeight = 1100
        self.backgroundColor = ((0, 0, 0))
        
        # rocket settings
        self.player_speed = 2
        
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 10
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 3