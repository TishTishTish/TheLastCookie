import sys
from Screens.config import *
import button_class
from Screens import title_screen


class Rules():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.display = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.rules_header_font = pygame.font.Font("../Assets/Fonts/Duke Charming.ttf", 80)
        self.rules_subheader_font = pygame.font.Font("../Assets/Fonts/Duke Charming.ttf", 40)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("../Assets/Fonts/Peaberry-Mono.otf", 31)
        self.smaller_font = pygame.font.Font("../Assets/Fonts/Peaberry-Mono.otf", 28)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.LILAC = (206, 157, 217)
        self.PINK = (255, 155, 185)
        self.logo = pygame.image.load("../Assets/Graphics/Logo.png").convert_alpha()
        self.logo_rect = self.logo.get_rect()
        x_centered = WIN_WIDTH / 2 - self.logo.get_width() / 2
        y_centered = WIN_HEIGHT / 2 - self.logo.get_height() / 2
        self.logo_rect.center = (x_centered, 10)
        self.screen.blit(self.logo, self.logo_rect.center)
        self.bg_image = pygame.image.load("Assets/Background HD crop.png").convert()
        self.bg_image_rect = self.bg_image.get_rect()
        self.background = ScrollingBackground()
        self.rectangle_x_pos = 90
        self.rectangle_y_pos = 65
        self.rectangle_width = 907.2
        self.rectangle_height = 607.68
        self.rectangle = pygame.rect.Rect(self.rectangle_x_pos, self.rectangle_y_pos, self.rectangle_width, self.rectangle_height)
        self.return_img = pygame.image.load("../Assets/Graphics/Return Button.png").convert_alpha()
        self.return_button = button_class.Button(645, 610, self.return_img, 0.8)
        self.pink_rectangle_width = 558.8352
        self.pink_rectangle_height = 236.73
        self.pink_rectangle_x_pos = 90
        self.pink_rectangle_y_pos = 436
        self.pink_rectangle = pygame.rect.Rect(self.pink_rectangle_x_pos, self.pink_rectangle_y_pos,self.pink_rectangle_width,self.pink_rectangle_height)
        self.cookies = pygame.image.load("../Assets/Graphics/Chocolate chip cookie graphic.png").convert_alpha()
        self.scaled_cookie = pygame.transform.smoothscale(self.cookies,(64,64))
        self.jammy_dodgers = pygame.image.load("../Assets/Graphics/Jammy dodger graphic.png").convert_alpha()
        self.scaled_jammy_dodgers = pygame.transform.smoothscale(self.jammy_dodgers,(64,64))


    def draw_text(self, text, size, colour, x, y):
        font = self.font
        text_surface = font.render(text,True,colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def draw_smaller_text(self, text, size, colour, x, y):
        font = self.smaller_font
        text_surface = font.render(text,True,colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def draw_rules_heading(self, text, size, colour, x, y):
        font = self.rules_header_font
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_rules_subheading(self, text, size, colour, x, y):
        font = self.rules_subheader_font
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


    def text_credits_screen(self):
        self.draw_rules_heading("Rules.", 48, self.WHITE, WIN_WIDTH//2,90)
        self.draw_rules_subheading("Controls",28,self.WHITE,(self.pink_rectangle_width//2 + 90),450)
        self.draw_text("Dective Digestive! After entering the Cookie", 22, self.WHITE, WIN_WIDTH//2,190)
        self.draw_text("Mistresses’ hobby room, she challenged you to", 22, self.WHITE, WIN_WIDTH//2,230)
        self.draw_text("an intensive game of connect four, to", 15, self.WHITE, WIN_WIDTH//2, 270)
        self.draw_text("determine which biscuit is superior: jammy ", 15, self.WHITE, WIN_WIDTH//2, 310)
        self.draw_text("dodgers or chocolate chips. If you can win", 15, self.WHITE, WIN_WIDTH//2, 350)
        self.draw_text("four in a row, she will grant you a clue.", 12, self.WHITE, WIN_WIDTH//2,390)
        self.draw_smaller_text("Move the mouse to determine",12, self.WHITE, (self.pink_rectangle_width//2 + 90), 490)
        self.draw_smaller_text("where to drop the cookie.",12, self.WHITE,349,530)
        self.draw_smaller_text("Press a mouse button to", 12, self.WHITE, 328, 570)
        self.draw_smaller_text("release the cookie.", 12, self.WHITE, 290, 610)


    def render_rectangle(self):
        self.screen.fill(self.LILAC,self.rectangle)
        self.screen.fill(self.PINK, self.pink_rectangle)

    def render_chocolate_chip_cookies(self):
        self.screen.blit(self.scaled_cookie,(210,95))
        self.screen.blit(self.scaled_cookie, (850,115))
        self.screen.blit(self.scaled_cookie,(850, 500))
        self.screen.blit(self.scaled_cookie,(600,520))



    def render_jammy_dodgers(self):
        self.screen.blit(self.scaled_jammy_dodgers,(140,105))
        self.screen.blit(self.scaled_jammy_dodgers,(775,100))
        self.screen.blit(self.scaled_jammy_dodgers,(790,430))
        self.screen.blit(self.scaled_jammy_dodgers,(500,600))

    def render_buttons(self):
        self.return_button.draw(surface=self.screen)

    def start_rules_screen(self):
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
            self.render_chocolate_chip_cookies()
            self.render_jammy_dodgers()


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

def rules_screen_loop():
    r = Rules()
    while r.running:
        r.start_rules_screen()

if __name__ == '__main__':
    rules_screen_loop()
    Rules()
