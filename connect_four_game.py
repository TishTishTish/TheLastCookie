import sys
from connect_four_config import *
import button_class


class End:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.display = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.credits_header_font = pygame.font.Font("connect-four-fonts/Duke Charming.ttf", 80)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("connect-four-fonts/Peaberry-Mono.otf", 32)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.LILAC = (206, 157, 217)
        self.bg_image = pygame.image.load("connect-four-graphics/background-hd-crop.png").convert()
        self.bg_image_rect = self.bg_image.get_rect()
        self.background = ScrollingBackground()
        self.rectangle_x_pos = 154.5
        self.rectangle_y_pos = 100
        self.rectangle_width = 771
        self.rectangle_height = 516
        self.rectangle = pygame.rect.Rect(self.rectangle_x_pos, self.rectangle_y_pos, self.rectangle_width, self.rectangle_height)
        self.return_img = pygame.image.load("connect-four-graphics/return-button.png").convert_alpha()
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


    def TextEndScreen(self):
        self.draw_credit_heading("Cookie Mistress.", 48, self.WHITE, WIN_WIDTH//2,110)
        self.draw_text("You have proven that", 22, self.WHITE, WIN_WIDTH//2,200)
        self.draw_text("that the chocolate chip cookie", 22, self.WHITE, WIN_WIDTH//2, 250)
        self.draw_text("is superior to the jammy dodger,",22, self.WHITE, WIN_WIDTH//2, 300)
        self.draw_text("therefore I must give you my clue.",22,self.WHITE,WIN_WIDTH//2,350)
        self.draw_text("Player has gained a clue for room 3", 22, self.WHITE, WIN_WIDTH//2, 450)


    def render_rectangle(self):
        self.screen.fill(self.LILAC,self.rectangle)


    def start_end_screen(self):
        while True:

            # Event handler


            # Cycles through all occurring events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()

            self.background.update()
            self.background.render()
            self.render_rectangle()
            self.TextEndScreen()



            pygame.display.update()


class ScrollingBackground():
    def __init__(self):
        self.bgimage = pygame.image.load('connect-four-graphics/background-hd-crop.png')
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

def end_screen_loop():
    e = End()
    while e.running:
        e.start_end_screen()

if __name__ == '__main__':
    end_screen_loop()
