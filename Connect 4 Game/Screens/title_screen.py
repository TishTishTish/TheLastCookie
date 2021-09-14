import sys
import os
from Screens.config import *
import button_class
from Screens import credits_screen
from Screens import rules_screen
from Screens import connect_four_game


class TitleScreen():
    """The Boot Screen when you first open the game"""


    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.music_playing = True
        self.display = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("../Assets/Fonts/Peaberry-Mono.otf", 32)
        game_icon = pygame.image.load(os.path.join("../Assets/Graphics", "jammy dodger graphic.png"))
        pygame.display.set_caption("Connect Four")
        pygame.display.set_icon(game_icon)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.logo = pygame.image.load("../Assets/Graphics/Logo.png").convert_alpha()
        self.logo_rect = self.logo.get_rect()
        x_centered = WIN_WIDTH / 2 - self.logo.get_width() / 2
        y_centered = WIN_HEIGHT / 2 - self.logo.get_height() / 2
        self.logo_rect.center = (x_centered, 10)
        self.screen.blit(self.logo, self.logo_rect.center)
        self.bg_image = pygame.image.load("Assets/Background HD crop.png").convert()
        self.bg_image_rect = self.bg_image.get_rect()
        self.background = ScrollingBackground()
        self.rules_img = pygame.image.load("../Assets/Graphics/Rules Button.png").convert_alpha()
        self.play_img = pygame.image.load("../Assets/Graphics/Play Button.png").convert_alpha()
        self.credits_img = pygame.image.load("../Assets/Graphics/Credits Button.png").convert_alpha()
        self.play_rect = self.play_img.get_rect()
        x_centered = WIN_WIDTH / 2 - self.play_img.get_width() / 2
        self.rules_button = button_class.Button(50, 500, self.rules_img, 0.75)
        self.play_button = button_class.Button(390, 500, self.play_img, 0.75)
        self.credits_button = button_class.Button(730, 500, self.credits_img, 0.75)

    def play_music(self):
        self.music = pygame.mixer.music.load("../Assets/Music/breakfast.mp3")
        pygame.mixer.music.play(loops= -1)


    def draw_background(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg_image, self.bg_image_rect)

    def logo(self):
        logo = pygame.image.load("../Assets/Graphics/Logo.png").convert()
        logo_rect = self.logo.get_rect()
        self.logo_rect.center = (150, WIN_WIDTH // 2)
        self.screen.blit(self.logo, self.logo_rect.center)


    def render_logo(self):
        DISPLAYSURF.blit(self.logo, self.logo_rect.center)

    def render_buttons(self):
        self.play_button.draw(surface=DISPLAYSURF)
        self.rules_button.draw(surface=DISPLAYSURF)
        self.credits_button.draw(surface=DISPLAYSURF)


    def start_title_screen(self):
        self.play_music()
        while True:
            # Event Handler
            if self.rules_button.clicked:
                rules_screen.rules_screen_loop()
            if self.play_button.clicked:
                connect_four_game.gameplay_loop()
                #new_state = connect_four_game.Game()
                #new_state.enter_state()
            if self.credits_button.clicked:
                credits_screen.credits_screen_loop()
            if self.play_button.clicked:
                pass




            # Cycles through all occurring events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()



            self.background.update()
            self.background.render()
            self.render_buttons()
            self.render_logo()

            pygame.display.update()

    def drawtext(self, text, size, x,y):
        text_surface = self.font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)


class ScrollingBackground():
    def __init__(self):
        self.bgimage = pygame.image.load('Assets/Background HD crop.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 0.15

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))


def title_screen_loop():
    t = TitleScreen()
    while t.running:
        t.start_title_screen()

if __name__ == '__main__':
    title_screen_loop()
