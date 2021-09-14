# I attempted a game state machine however I found this topic too complex, in the future I will implement this. Find state file to see the layout i would have utilised, implementing thr stack data structure.

import os
from Screens.config import *
import pygame

#Load our states
from Screens.title_screen import TitleScreen

class MainGame():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        pygame.display.set_caption("Connect Four")
        game_icon = pygame.image.load(os.path.join("Assets/Graphics", "jammy dodger checker.png"))
        pygame.display.set_icon(game_icon)
        self.display = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("../Assets/Fonts/Peaberry-Mono.otf", 32)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.state_stack = []
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_events()
            self.play_music()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False



    def load_states(self):
        self.title_screen = TitleScreen()
        self.state_stack.append(self.title_screen)

    def play_music(self):
        self.music = pygame.mixer.music.load("../Assets/Music/breakfast.mp3")
        pygame.mixer.music.play(loops=-1)

if __name__ == '__main__':
    g = MainGame()
    while g.running:
        g.game_loop()
