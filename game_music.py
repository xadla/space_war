from pygame import mixer

class GameMusic:
    def __init__(self) -> None:
        mixer.init()
        
        mixer.music.load("musics/game.mp3")
        
        mixer.music.set_volume(0.7)
        
    def play(self):
        mixer.music.play()