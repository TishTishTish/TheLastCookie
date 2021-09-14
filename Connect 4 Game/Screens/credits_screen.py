import sys
from Screens.config import *
import button_class
from Screens import title_screen


class Credits:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.display = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.credits_header_font = pygame.font.Font("../Assets/Fonts/Duke Charming.ttf", 80)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("../Assets/Fonts/Peaberry-Mono.otf", 32)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.LILAC = (206, 157, 217)
        self.logo = pygame.image.load("../Assets/Graphics/Logo.png").convert_alpha()
        self.logo_rect = self.logo.get_rect()
        x_centered = WIN_WIDTH / 2 - self.logo.get_width() / 2
        y_centered = WIN_HEIGHT / 2 - self.logo.get_height() / 2
        self.logo_rect.center = (x_centered, 10)
        self.screen.blit(self.logo, self.logo_rect.center)
        self.bg_image = pygame.image.load("Assets/Background HD crop.png").convert()
        self.bg_image_rect = self.bg_image.get_rect()
        self.background = ScrollingBackground()
        self.rectangle_x_pos = 154.5
        self.rectangle_y_pos = 100
        self.rectangle_width = 771
        self.rectangle_height = 516
        self.rectangle = pygame.rect.Rect(self.rectangle_x_pos, self.rectangle_y_pos, self.rectangle_width, self.rectangle_height)
        self.return_img = pygame.image.load("../Assets/Graphics/Return Button.png").convert_alpha()
        self.return_button = button_class.Button(616, 21, self.return_img, 0.75)

        # self.rectangle = pygame.Rect(,771,516)
        #     pygame.draw.rect(self.screen, self.LILAC,)


    def draw_text(self, text, size, colour, x, y):
        font = self.font
        text_surface = font.render(text,True,colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def draw_credit_heading(self, text, size, colour, x, y):
        font = self.credits_header_font
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


    def text_credits_screen(self):
        self.draw_credit_heading("Credits.", 48, self.WHITE, WIN_WIDTH//2,110)
        self.draw_text("Game and Graphics by", 22, self.WHITE, WIN_WIDTH//2,200)
        self.draw_text("Funmi Falegan", 22, self.WHITE, WIN_WIDTH//2, 250)
        self.draw_text("Fonts: Peaberry and Duke Charming", 15, self.WHITE, WIN_WIDTH//2, 320)
        self.draw_text("Background: Vecteezy", 15, self.WHITE, WIN_WIDTH//2, 390)
        self.draw_text("Music: Cafe Mix - Cat Planet Studio", 15, self.WHITE, WIN_WIDTH//2, 460)
        self.draw_text("Made for 'The Last Cookie'", 12, self.WHITE, WIN_WIDTH//2,520)
        self.draw_text("And the Code First Girls Nanodegree",12, self.WHITE, WIN_WIDTH//2, 580)


    def rendered_text(self):
        CREDITS = self.credits_header_font.render("Credits", True, self.WHITE)
        CREDITS_Rect = CREDITS.get_rect(centre=(WIN_WIDTH//2, 10))
        DISPLAYSURF.blit(CREDITS,CREDITS_Rect)

    def render_rectangle(self):
        self.screen.fill(self.LILAC,self.rectangle)

    def render_buttons(self):
        self.return_button.draw(surface=self.screen)

    def start_credits_screen(self):
        while True:

            # Event handler
            if self.return_button.clicked:
                title_screen.title_screen_loop()

            # Cycles through all occurring events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.background.update()
            self.background.render()
            self.render_rectangle()
            self.text_credits_screen()
            self.render_buttons()


            pygame.display.update()


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

def credits_screen_loop():
    c = Credits()
    while c.running:
        c.start_credits_screen()

if __name__ == '__main__':
    credits_screen_loop()
