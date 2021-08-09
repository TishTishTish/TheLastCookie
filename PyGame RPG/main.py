import pygame
from pygame.sprite import Sprite
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init() # initialise Pygame
        pygame.display.set_caption('The Last Cookie')
        
        game_icon = pygame.image.load('img\cookie1.png')
        pygame.display.set_icon(game_icon)

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.character_spritesheet = Spritesheet('img/pikachu.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        
    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
    
    def new(self):
        # starts a new game
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        
        self.createTilemap()
        
    def events(self):
        # a new game starts
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def update(self):
        # a game loop updates
        self.all_sprites.update()
    
    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(Self):
        pass
    
    def intro_screen(self):
        pass
    
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()
input("Press Enter to close")