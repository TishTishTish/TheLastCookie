import random, sys
from Screens.config import *
import math
import os
import button_class
from Screens import rulesscreen2
from Screens import end_screen
from state import State

# How i ensured I was working with the right directory
#currentWorkDir = os.getcwd()
#print(currentWorkDir)
#path = "/Connect 4 Game"

class Game(State):
    def __init__(self):
        State.__init__(self)
        pygame.init() #Intialise Pygame
        self.font = pygame.font.Font("../Assets/Fonts/Peaberry-Mono.otf", 50)
        self.WHITE = (255,255,255)


        self.SQUARESIZE = 100 # Size of the game board pieces

        self.screen = pygame.display.set_mode((WIN_WIDTH,900))
        self.clock = pygame.time.Clock()
        self.getTicksLastFrame = 0
        self.running = True

        self.starting_bot = False

        self.gameboard = GameBoard()
        self.gui = GUI()
        self.bot = GameBot()
        self.sfx = SoundFX()
        self.bot_active = True
        self.gamerules = GameRules()
        self.game_over = False

        self.turn = 0 # 0 is players turn, 1 is AI's turn
        self.turn_count = 0 # Counts moves
        self.win = 0 # 1= player has won, 2 = AI has won
        self.mouseX = -500

    def draw_text(self, text, size, colour, x, y):
        font = self.font
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


    def render_text(self):

        if self.gameboard.allow_drop and self.win == 1: # Draw winner text
            self.playerwontext = self.draw_text("Player", 80, self.WHITE, 140, 15)
            self.playerwontext = self.draw_text("Won",80,self.WHITE,140,75)
        if self.gameboard.allow_drop and self.win == 2: # Draw loser text
            self.botwontext = self.draw_text("Computer",80,self.WHITE,140,15)
            self.botwontext1 = self.draw_text("Won",80,self.WHITE,140,75)
        if self.gameboard.allow_drop and self.win == 0 and self.gameboard.is_board_fill():
            self.botwontext = self.draw_text("It's", 80, self.WHITE, 140, 15)
            self.botwontext = self.draw_text("a", 80, self.WHITE, 140, 75)
            self.botwontext = self.draw_text("Draw", 80, self.WHITE, 140, 140)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                sys.exit()

            if self.gui.reset_button.clicked:
                self.gameboard.get_new_board()
                self.turn = 0
                self.turn_count = 0
                self.win = 0
                break

            if self.gui.return_button.clicked:
                rulesscreen2.rules_screen_loop()

            if self.gameboard.allow_drop and self.win == 1:
                pygame.time.delay(5000) #In milleseconds, 5 seconds
                end_screen.end_screen_loop()



            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] >= 300 and event.pos[0] <= 1000:
                    self.mouseX = event.pos[0] # Getting the value of the mouse for the checker dropping animation
                else:
                    self.mouseX = -500



            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.pos[0] >= 300 and event.pos[0] <= 1000 and self.gameboard.allow_drop and self.win == 0:
                    column = int(math.floor((event.pos[0] - 325) / self.SQUARESIZE))
                    if not self.starting_bot or self.starting_bot and self.turn == 0:
                        self.play_turn(column)



    def render(self):
        self.screen.fill((120,120,120))
        self.update()
        self.gameboard.draw_board(self.screen, self.turn, self.mouseX, self.win, self.bot_active)
        self.gui.render_buttons()
        self.render_text()
        pygame.display.update()



    def update(self):
        t = pygame.time.get_ticks()
        self.deltaTime = (t-self.getTicksLastFrame) / 1000.0 # explain what this does
        self.getTicksLastFrame = t

        if self.turn == 1 and self.gameboard.allow_drop and self.win == 0:
            self.bot_active = True
            self.play_turn(self.bot.bots_turn(self.gameboard.board_list))
        elif self.gameboard.allow_drop and self.turn == 0:
            self.bot_active = False
        self.gameboard.update(self.deltaTime)



    def play_turn(self,column):
        if self.gameboard.column_available(column):
            row = self.gameboard.get_open_row(column)
            self.gameboard.drop_checker(column, row, self.turn+1)
            self.sfx.play_sfx()
            if self.turn_count >= 6:
                win_data = self.gamerules.check_win(self.gameboard.board_list, (column,row))
                self.gameboard.set_highlight_rotation(self.bot.delete_multiple_coords(win_data[1]))
                self.win = win_data[0]
            self.turn_count += 1
            self.turn += 1
            self.turn %= 2 # Changes between 1 and 2


class GUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.reset_img = pygame.image.load("../Assets/Graphics/Reset Button.png")
        self.rules_img = pygame.image.load("../Assets/Graphics/Rules Button.png")
        self.reset_button = button_class.Button(15,500,self.reset_img,0.70)
        self.return_button = button_class.Button(15,600,self.rules_img,0.70)


    def render_buttons(self):
        self.reset_button.draw(surface=self.screen)
        self.return_button.draw(surface=self.screen)

class Music:
    def __init__(self):
        pygame.mixer.init(frequency=22050, size=16, channels=2, buffer=4096)  # Initialise music
        self.music_playing = True

        # Background Music
        bg_music = pygame.mixer.music.load("../Assets/Music/lunch.ogg")
        pygame.mixer.music.play(bg_music, -1)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.music_playing = False
    def resume_music(self):
        pygame.mixer.music.unpause()
        self.music_playing = True

class SoundFX:
    def __init__(self):
        # Dropping Checker sound effect
        self.sound_effect = pygame.mixer.Sound("../Assets/Music/jumb.wav")

    def play_sfx(self):
        self.sound_effect.play()
        self.sound_effect.set_volume(0.15)




class GameBoard:

    board_list = []
    WHITE = (255, 255, 255)
    allow_drop = True
    checkerXY = [0,0]
    checkerYend = 0
    # Define the game board size
    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6
    GRAVITY = 50
    VELOCITY = 0
    SPACESIZE = 100 # Size og tokens and individual board pieces in pixels
    XMARGIN = int((WIN_WIDTH - BOARD_WIDTH * SPACESIZE) / 2)
    YMARGIN = int((WIN_HEIGHT - BOARD_HEIGHT * SPACESIZE) / 2)

    # Board Image Assets
    texture_nochecker = pygame.image.load(
        os.path.join("../Assets/Graphics", "grid checker empty.png")).convert_alpha()
    texture_nochecker_scaled = pygame.transform.smoothscale(texture_nochecker,(100,100))
    texture_checker_cookie = pygame.image.load(
        (os.path.join("../Assets/Graphics", "cookie checker.png"))).convert_alpha()
    texture_checker_jammy = pygame.image.load(
        os.path.join("../Assets/Graphics", "jammy dodger checker.png")).convert_alpha()
    texture_cookie = pygame.image.load(
        (os.path.join("../Assets/Graphics", "Chocolate chip cookie graphic.png"))).convert_alpha()
    texture_jammy = pygame.image.load(
        (os.path.join("../Assets/Graphics", "Jammy dodger graphic.png"))).convert_alpha()
    texture_grid = pygame.image.load((os.path.join("../Assets/Graphics", "grid.png"))).convert_alpha()
    scaled_grid = pygame.transform.smoothscale(texture_grid, (100, 100))  # tweak this up
    tex_highlight = pygame.image.load((os.path.join("../Assets/Graphics", "circle_highlight.png"))).convert_alpha()
    tex_long_highlight = pygame.image.load(
        os.path.join("../Assets/Graphics", "circle_long_highlight.png")).convert_alpha()

    textures = {
        0: texture_nochecker_scaled,
        1: texture_checker_cookie,
        2: texture_checker_jammy,
        3: texture_cookie,
        4: texture_jammy

    }


    def __init__(self):
        self.get_new_board()

    def update(self, frameDeltaTime): # Utilised Delta Time as opposed to fps as it ensures consistent animation in the event of a low frame rate
        self.checker_fall(frameDeltaTime)

    def draw_board(self, window, turn, mouseX, smnwon, botactive):
        DISPLAYSURF.fill(BGCOLOUR)
        # Draw game board shadow
        pygame.draw.rect(window, self.WHITE, (300 + 15, 100+15, 700, 600)) #shadow
        # Draw Game Board
        for r in range(self.BOARD_HEIGHT):
            for c in range(self.BOARD_WIDTH):
                window.blit(self.textures.get(self.board_list[c][r]), (300 + c * 100, 605 - 100 * r))

        if self.allow_drop:
            if smnwon == 0 and botactive and not self.is_board_fill():
                window.blit(self.textures.get(turn + 3), (mouseX - 10, 10))

        else:
            window.blit(self.texture_nochecker, (300 + self.lowestemptyspace[0] * 100, 605 - 100 * self.lowestemptyspace[1]))
            turn += 1
            turn %= 2
            window.blit(self.textures.get(turn + 3), (self.checkerXY[0], self.checkerXY[1]))

        for r in range(self.BOARD_HEIGHT):
            for c in range(self.BOARD_WIDTH):
                window.blit(self.scaled_grid, (300 + c * 100, 605 - 100 * r))

        if smnwon != 0 and self.allow_drop: # When someone has won the game and the drop checker animation has finished
            for i in range(len(self.list_highlight_coords)):
                if self.list_highlight_coords[i][0] == [0]:
                    window.blit(self.list_highlight_rotate[i],(300 + self.list_highlight_coords[i][0] * 100, 600 - 100 * self.list_highlight_coords[i][1])) ## the texture around the winning stones is drawn
                else:
                    window.blit(self.list_highlight_rotate[i], (300 + self.list_highlight_coords[i][0] * 100 + self.list_highlight_offset[i][0],600 - 100 * self.list_highlight_coords[i][1] + self.list_highlight_offset[i][1]))


    def drop_checker(self, c, r, p):
        self.allow_drop = False
        self.velocity = 0
        self.checkerXY = [310 + c * 100, 100]
        self.checkerYend = 500 - r * 100 # COME BACK TO THI
        self.lowestemptyspace = (c,r)
        self.board_list[c][r] = p

    def checker_fall(self, frameDeltaTime):
        if not self.allow_drop:
            speed = 6

            self.checkerXY[1] += speed * frameDeltaTime * self.velocity
            self.velocity += speed * frameDeltaTime * self.GRAVITY

        if self.checkerXY[1] >= self.checkerYend:
            self.allow_drop = True


    def is_valid_move(self, board, column):
        if column < 0 or column >= (self.BOARD_WIDTH) or board[column][0]!= EMPTY:
            return False
        return True

    def get_open_row(self, c):

        for r in range(self.BOARD_WIDTH):
            if self.board_list[c][r] == 0:
                return r

    def column_available(self, column):
        return self.board_list[column][5] == 0

    def get_new_board(self):
        self.board_list.clear()
        for x in range(self.BOARD_WIDTH):
            self.board_list.append([0, 0, 0, 0, 0, 0])



    def is_board_fill(self):
        for c in range(self.BOARD_WIDTH):
            for r in range(self.BOARD_HEIGHT):
                if self.board_list[c][r] == 0:
                    return False
        return True

    def set_highlight_rotation(self, L):

        rotations = {
            0:0,
            1:90,
            2:45,
            3:-45
        }

        self.list_highlight_offset = []
        self.list_highlight_coords = []
        self.list_highlight_rotate = []

        for elem in L:
            self.highlight_offset = [0,0]
            self.rotated_highlight = pygame.transform.rotate(self.tex_highlight,rotations.get(elem[0]))

            if elem[0] == 0: #x coordinates
                self.highlight_coords = [min([c for c,f in elem[1]]), elem[1][0][1]] #smallest x or y cposdiaoord

            elif elem[0] == 1: #y coordinate
                self.highlight_coords = [elem[1][0][0],max([f for c,f in elem[1]])]

            elif elem[0] == 2:
                self.rotated_highlight = pygame.transform.rotate(self.tex_long_highlight, rotations.get(elem[0])) #As this is a diagnonal, long texture is used
                self.highlight_coords = [min([c for c, f in elem[1]]), min([f for c,f in elem[1]])]
                self.highlight_offset = [-13,-349]

            elif elem[0] == 3:
                self.rotated_highlight = pygame.transform.rotate(self.tex_long_highlight, rotations.get(elem[0])) #Diagnonal so long texture
                self.highlight_coords = [max([c for c,f in elem[1]]) , max([f for c,f in elem[1]])]
                self.highlight_offset = [-348,-12]


            self.list_highlight_offset.append(self.highlight_offset)
            self.list_highlight_coords.append(self.highlight_coords)
            self.list_highlight_rotate.append(self.rotated_highlight)





class GameRules(GameBoard):

    def __init__(self):
        pass

    def check_win(self, f, last_checker, paircount=4):
        def already_won(win, type, pairvalue):
            if win >= pairvalue:
                return True
                return True

        p = f[last_checker[0]][last_checker[1]] #value of the last stone placed = current player (1/2)

        final_list = []

        for xy_switch in range(2):
            win = 1
            return_list = []
            return_list.append([last_checker[0],last_checker[1]])
            for a in range(2):
                for move in range(1,4):
                    move *= pow(-1, a) ## so first round: 1, 2, 3; second pass: -1, -2, -3
                    if last_checker[0 + 1 * xy_switch] - move >= 0 and last_checker[0 + 1 * xy_switch] - move <= (self.BOARD_HEIGHT - 1 * xy_switch):  # xy_switch so that 1st pass: last_stone [0] (column) (X) and 2nd pass last_stone [1] (row) (Y) is moved
                        if f[last_checker[0] - (move - move * xy_switch)][last_checker[1] - move * xy_switch] == p:
                            win += 1
                            return_list.append([last_checker[0] - (move- move * xy_switch), last_checker[1] - move * xy_switch])
                        else:
                            break
                    if already_won(win, "XY", paircount):
                        final_list.append([xy_switch, return_list])

        for positivenegative in range(2):
            win = 1
            return_list = []
            return_list.append([last_checker[0], last_checker[1]])
            for a in range(2):
                for move in range(1,4):
                    move *= pow(-1,a)  ## so first round: 1, 2, 3; second pass: -1, -2, -3
                    if 0 <= last_checker[1] - move <= 5 and 0 <= last_checker[0] - (
                            move * pow(-1, positivenegative)) <= 6:
                        if f[last_checker[0] - (move * pow(-1, positivenegative))][last_checker[1] - move] == p: # by * pow (-1, posneg) the - was made a + in the second round where it is about the neg. diagonal win
                            win += 1
                            return_list.append([last_checker[0] - (move * pow(-1, positivenegative)), last_checker[1] - move])
                        else:
                            break
            if already_won(win, "DIA", paircount):
                final_list.append([2+ positivenegative, return_list])

        if len(final_list) > 1 and paircount != 4:
            return (True, 4, final_list) # 4 as a sign that more than 1 row starts from the stone # [bool so many stones lined up were found, int type of friction (x, y, dia ..), list of stones]
        elif len(final_list) == 1:
            if paircount != 4:
                return (True, final_list[0][0], final_list[0][1])
        if len(final_list) > 0 and paircount == 4:
            return (p, final_list)
        if paircount == 4:
            return (0,[])
        else:
            return (False, 0,[])

# Utilised AI I found online, as this a very complex topic https://www.youtube.com/watch?v=3_VEPnmMyDY
class GameBot(GameRules):
    def __init__(self):
        pass

    def bots_turn(self, f):
        column_blacklist = []

        # prüft ob es eine winmöglichkeit für den bot gibt
        winning_column = self.IwannaWin(f)
        if winning_column != 420:
            return winning_column

        if f[3][0] == 0:  # mittlere spalte taktisch klug zu besetzen
            print("MITTE EINNEHMEN")
            return 3

        for r in range(self.BOARD_HEIGHT):  # situationen wie: 0110100 sollen verhindert werden
            for m in range(4):
                if f[m][r] == 1 and f[m + 1][r] == 1 and f[m + 2][r] == 0 and f[m + 3][r] == 1:
                    if r - self.get_num_of_stones_in_column(m + 2,
                                                            f) == 0 and not m + 2 in column_blacklist:  # wenn höhendifferenz == 0 dann verhindere situation
                        print("1101 situation X verhindert!")
                        return m + 2
                    elif r - self.get_num_of_stones_in_column(m + 2,
                                                              f) == 1:  # wenn delta höhe == 1 dann blackliste spalte
                        column_blacklist.append(m + 2)
                if f[m][r] == 1 and f[m + 1][r] == 0 and f[m + 2][r] == 1 and f[m + 3][r] == 1:
                    if r - self.get_num_of_stones_in_column(m + 1, f) == 0 and not m + 1 in column_blacklist:
                        print("1011 situation X verhindert!")
                        return m + 1
                    elif r - self.get_num_of_stones_in_column(m + 1, f) == 1:
                        column_blacklist.append(m + 1)

        for r in range(self.BOARD_HEIGHT - 3):  # situationen wie 1101 aber in POS diagonal
            for c in range(self.BOARD_WIDTH - 3):
                if f[c][r] == 1 and f[c + 1][r + 1] == 1 and f[c + 2][r + 2] == 0 and f[c + 3][r + 3] == 1:
                    if r + 2 - self.get_num_of_stones_in_column(c + 2, f) == 0 and not c + 2 in column_blacklist:
                        print("1101 situation POS DIA verhindert!")
                        return c + 2
                    elif r + 2 - self.get_num_of_stones_in_column(c + 2, f) == 1:
                        column_blacklist.append(c + 2)
                if f[c][r] == 1 and f[c + 1][r + 1] == 0 and f[c + 2][r + 2] == 1 and f[c + 3][r + 3] == 1:
                    if r + 1 - self.get_num_of_stones_in_column(c + 1, f) == 0 and not c + 1 in column_blacklist:
                        print("1011 situation POS DIA verhindert!")
                        return c + 1
                    elif r + 1 - self.get_num_of_stones_in_column(c + 1, f) == 1:
                        column_blacklist.append(c + 1)

        for r in range(3, self.BOARD_HEIGHT):  # situationen wie 1101 aber in NEG diagonal
            for c in range(self.BOARD_HEIGHT - 3):
                if f[c][r] == 1 and f[c + 1][r - 1] == 1 and f[c + 2][r - 2] == 0 and f[c + 3][r - 3] == 1:
                    if r - 2 - self.get_num_of_stones_in_column(c + 2, f) == 0 and not c + 2 in column_blacklist:
                        print("1101 situation NEG DIA verhindert!")
                        return c + 2
                    elif r - 2 - self.get_num_of_stones_in_column(c + 2, f) == 1:
                        column_blacklist.append(c + 2)
                if f[c][r] == 1 and f[c + 1][r - 1] == 0 and f[c + 2][r - 2] == 1 and f[c + 3][r - 3] == 1:
                    if r - 1 - self.get_num_of_stones_in_column(c + 1, f) == 0 and not c + 1 in column_blacklist:
                        print("1011 situation NEG DIA verhindert!")
                        return c + 1
                    elif r - 1 - self.get_num_of_stones_in_column(c + 1, f) == 1:
                        column_blacklist.append(c + 1)

        triples = self.get_triples(f)  # gibt liste mit allen 3er kombis und deren koordinaten
        if len(triples) > 0:
            for a in triples:
                if a[0] == 1 and max([r for c, r in a[1]]) == self.get_num_of_stones_in_column(a[1][0][0],
                                                                                               f) - 1 and self.column_available(
                        a[1][0][
                            0]):  # type==Y and höchste ROW-/Y-coord == anzahl steine in gleicher spalte-1   (-1 weil anzahl zählt nicht ab 0)
                    print("Y VERHINDEN")
                    return a[1][0][0]

                if a[0] == 0 and min([c for c, r in a[1]]) > 0 and f[min([c for c, r in a[1]]) - 1][
                    a[1][0][1]] == 0:  # type==X and niedrigste COLUMN-/X-coord > 0 and feld links daneben frei
                    if a[1][0][1] == 0 and not min([c for c, r in a[1]]) - 1 in column_blacklist:  # 3erpaar auf höhe 0
                        print("LIIINKS (höhe 0)")
                        return min([c for c, r in a[1]]) - 1  # links vom X-3erpaar wird stein gesetzt
                    elif f[min([c for c, r in a[1]]) - 1][a[1][0][1] - 1] != 0 and not min([c for c, r in a[
                        1]]) - 1 in column_blacklist:  # nicht auf höhe 0, und wenn feld X=-1 Y=-1 (links daneben ein mal nach unten) nicht frei ist
                        print("LIIINKS (schlaue verhinderung)")
                        return min([c for c, r in a[1]]) - 1
                    elif (1 + a[1][0][1]) - self.get_num_of_stones_in_column(min([c for c, r in a[1]]) - 1,
                                                                             f) == 2:  # wenn höhendifferenz zwischen 3erpaar und höchster stein von spalte links daneben == 2 dann blackliste diese spalte
                        column_blacklist.append(min([c for c, r in a[1]]) - 1)

                if a[0] == 0 and max([c for c, r in a[1]]) < self.BOARD_WIDTH - 1 and f[max([c for c, r in a[1]]) + 1][
                    a[1][0][1]] == 0:
                    if a[1][0][1] == 0 and not max([c for c, r in a[1]]) + 1 in column_blacklist:  # 3erpaar auf höhe 0
                        print("REEECHTS (höhe 0)")
                        return max([c for c, r in a[1]]) + 1  # rechts vom X-3erpaar wird stein gesetzt
                    elif f[max([c for c, r in a[1]]) + 1][a[1][0][1] - 1] != 0 and not max([c for c, r in a[
                        1]]) + 1 in column_blacklist:  # nicht auf höhe 0, und wenn feld X=+1 Y=-1 (rechts daneben ein mal nach unten) nicht frei ist
                        print("REEECHTS (schlaue verhinderung)")
                        return max([c for c, r in a[1]]) + 1
                    elif (1 + a[1][0][1]) - self.get_num_of_stones_in_column(max([c for c, r in a[1]]) + 1,
                                                                             f) == 2:  # wenn höhendifferenz zwischen 3erpaar und höchster stein von spalte rechts daneben == 2 dann blackliste diese spalte
                        column_blacklist.append(max([c for c, r in a[1]]) + 1)
                        # POSITIV DIAGONAL
                if a[0] == 2 and min([c for c, r in a[1]]) - 1 >= 0 and min(
                        [r for c, r in a[1]]) - 1 >= 0:  # um out of range errors zu vermeiden
                    if f[min([c for c, r in a[1]]) - 1][min([r for c, r in a[1]]) - 1] == 0:  # zielfeld frei?
                        if min([r for c, r in a[1]]) - 1 - self.get_num_of_stones_in_column(
                                min([c for c, r in a[1]]) - 1, f) == 0 and not min(
                                [c for c, r in a[1]]) - 1 in column_blacklist:  # höhendifferenz == 0
                            print("diagonal verhinderung links unten")
                            return min([c for c, r in a[1]]) - 1
                        elif min([r for c, r in a[1]]) - 1 - self.get_num_of_stones_in_column(
                                min([c for c, r in a[1]]) - 1, f) == 1:
                            column_blacklist.append(min([c for c, r in a[1]]) - 1)
                if a[0] == 2 and max([c for c, r in a[1]]) + 1 <= 6 and max(
                        [r for c, r in a[1]]) + 1 <= 5:  # um out of range errors zu vermeiden
                    if f[max([c for c, r in a[1]]) + 1][max([r for c, r in a[1]]) + 1] == 0:
                        if max([r for c, r in a[1]]) + 1 - self.get_num_of_stones_in_column(
                                max([c for c, r in a[1]]) + 1, f) == 0 and not max(
                                [c for c, r in a[1]]) + 1 in column_blacklist:  # höhendifferenz == 0
                            print("diagonal verhinderung rechts oben")
                            return max([c for c, r in a[1]]) + 1
                        elif max([r for c, r in a[1]]) + 1 - self.get_num_of_stones_in_column(
                                max([c for c, r in a[1]]) + 1, f) == 1:
                            column_blacklist.append(max([c for c, r in a[1]]) + 1)
                # NEGATIV DIAGONAL
                if a[0] == 3 and min([c for c, r in a[1]]) - 1 >= 0 and max(
                        [r for c, r in a[1]]) + 1 <= 5:  # um out of range errors zu vermeiden
                    if f[min([c for c, r in a[1]]) - 1][max([r for c, r in a[1]]) + 1] == 0:
                        if max([r for c, r in a[1]]) + 1 - self.get_num_of_stones_in_column(
                                min([c for c, r in a[1]]) - 1, f) == 0 and not min(
                                [c for c, r in a[1]]) - 1 in column_blacklist:  # höhendifferenz == 0
                            print("negdiagonal verhinderung links oben")
                            return min([c for c, r in a[1]]) - 1
                        elif max([r for c, r in a[1]]) + 1 - self.get_num_of_stones_in_column(
                                min([c for c, r in a[1]]) - 1, f) == 1:
                            column_blacklist.append(min([c for c, r in a[1]]) - 1)
                if a[0] == 3 and max([c for c, r in a[1]]) + 1 <= 6 and min(
                        [r for c, r in a[1]]) - 1 >= 0:  # um out of range errors zu vermeiden
                    if f[max([c for c, r in a[1]]) + 1][min([r for c, r in a[1]]) - 1] == 0:
                        if min([r for c, r in a[1]]) - 1 - self.get_num_of_stones_in_column(
                                max([c for c, r in a[1]]) + 1, f) == 0 and not max(
                                [c for c, r in a[1]]) + 1 in column_blacklist:  # höhendifferenz == 0
                            print("negdiagonal verhinderung rechts unten")
                            return max([c for c, r in a[1]]) + 1
                        elif min([r for c, r in a[1]]) - 1 - self.get_num_of_stones_in_column(
                                max([c for c, r in a[1]]) + 1, f) == 1:
                            column_blacklist.append(max([c for c, r in a[1]]) + 1)

        for r in range(self.BOARD_HEIGHT):
            for m in range(6):
                if f[m][r] == 1 and f[m + 1][r] == 1:
                    if m - 1 >= 0:
                        if r - self.get_num_of_stones_in_column(m - 1,
                                                                f) == 0 and not m - 1 in column_blacklist:  # wenn höhendifferenz == 0 dann verhindere situation
                            print("2erPack von LINKS vorraussichtlich eingeschränkt!")
                            return m - 1
                    elif m + 2 <= 6:
                        if r - self.get_num_of_stones_in_column(m + 2,
                                                                f) == 0 and not m + 2 in column_blacklist:  # wenn höhendifferenz == 0...
                            print("2erPack von RECHTS vorraussichtlich eingeschränkt!")
                            return m + 2

        print("RANDOM, geblacklistet: ", column_blacklist)
        valid_columns = []
        for c in range(self.BOARD_WIDTH):
            if self.get_num_of_stones_in_column(c, f) < 6:
                valid_columns.append(c)

        rand = random.randrange(len(valid_columns))
        if self.all_valid_columns_blacklistet(valid_columns, column_blacklist) and len(
                column_blacklist) > 0:  # wenn alle freien spalten geblacklistet sind muss bot eine blacklistspalte nehmen
            return column_blacklist[0]

        while valid_columns[
            rand] in column_blacklist:  # random zug soll bot nicht in schwierige situationen bringen die oben im code zu verhindern versucht wurden
            rand = random.randrange(len(valid_columns))
        return valid_columns[rand]

    def all_valid_columns_blacklistet(self, valcolL, blacklistL):
        for a in range(len(valcolL)):
            if not valcolL[a] in blacklistL:
                return False
        else:
            return True

    def IwannaWin(self, f):
        for r in range(self.BOARD_HEIGHT):  # situationen wie: 0110100 sollen verhindert werden
            for m in range(4):
                if f[m][r] == 2 and f[m + 1][r] == 2 and f[m + 2][r] == 0 and f[m + 3][r] == 2:
                    if r - self.get_num_of_stones_in_column(m + 2,
                                                            f) == 0:  # wenn höhendifferenz == 0 dann verhindere situation
                        print("2202 WINsituation NUTZUNG!")
                        return m + 2
                if f[m][r] == 2 and f[m + 1][r] == 0 and f[m + 2][r] == 2 and f[m + 3][r] == 2:
                    if r - self.get_num_of_stones_in_column(m + 1, f) == 0:
                        print("2022 WINsituation NUTZUNG!")
                        return m + 1
        for r in range(self.BOARD_HEIGHT - 3):  # situationen wie 1101 aber in POS diagonal
            for c in range(self.BOARD_WIDTH - 3):
                if f[c][r] == 2 and f[c + 1][r + 1] == 2 and f[c + 2][r + 2] == 0 and f[c + 3][r + 3] == 2:
                    if r + 2 - self.get_num_of_stones_in_column(c + 2, f) == 0:
                        print("2202 situation POS DIA NUTZUNG!")
                        return c + 2
                if f[c][r] == 2 and f[c + 1][r + 1] == 0 and f[c + 2][r + 2] == 2 and f[c + 3][r + 3] == 2:
                    if r + 1 - self.get_num_of_stones_in_column(c + 1, f) == 0:
                        print("2022 situation POS DIA NUTZUNG!")
                        return c + 1
        for r in range(3, self.BOARD_HEIGHT):  # situationen wie 1101 aber in NEG diagonal
            for c in range(self.BOARD_WIDTH - 3):
                if f[c][r] == 2 and f[c + 1][r - 1] == 2 and f[c + 2][r - 2] == 0 and f[c + 3][r - 3] == 2:
                    if r - 2 - self.get_num_of_stones_in_column(c + 2, f) == 0:
                        print("2202 situation NEG DIA NUTZUNG!")
                        return c + 2
                if f[c][r] == 2 and f[c + 1][r - 1] == 0 and f[c + 2][r - 2] == 2 and f[c + 3][r - 3] == 2:
                    if r - 1 - self.get_num_of_stones_in_column(c + 1, f) == 0:
                        print("2022 situation NEG DIA NUTZUNG!")
                        return c + 1
        triples = self.get_triples(f, 2)  # gibt liste mit allen 3er kombis und deren koordinaten
        if len(triples) > 0:
            for a in triples:
                if a[0] == 1 and max([r for c, r in a[1]]) == self.get_num_of_stones_in_column(a[1][0][0],
                                                                                               f) - 1 and self.column_available(
                        a[1][0][
                            0]):  # type==Y and höchste ROW-/Y-coord == anzahl steine in gleicher spalte-1   (-1 weil anzahl zählt nicht ab 0)
                    print("Y WIN")
                    return a[1][0][0]

                if a[0] == 0 and min([c for c, r in a[1]]) > 0 and f[min([c for c, r in a[1]]) - 1][
                    a[1][0][1]] == 0:  # type==X and niedrigste COLUMN-/X-coord > 0 and feld links daneben frei
                    if a[1][0][1] == 0:  # 3erpaar auf höhe 0
                        print("LIIINKS (höhe 0) WIN")
                        return min([c for c, r in a[1]]) - 1  # links vom X-3erpaar wird stein gesetzt
                    elif f[min([c for c, r in a[1]]) - 1][a[1][0][
                                                              1] - 1] != 0:  # nicht auf höhe 0, und wenn feld X=-1 Y=-1 (links daneben ein mal nach unten) nicht frei ist
                        print("LIIINKS (schlauer WIN)")
                        return min([c for c, r in a[1]]) - 1

                if a[0] == 0 and max([c for c, r in a[1]]) < self.BOARD_WIDTH - 1 and f[max([c for c, r in a[1]]) + 1][
                    a[1][0][1]] == 0:
                    if a[1][0][1] == 0:  # 3erpaar auf höhe 0
                        print("REEECHTS (höhe 0) WIN")
                        return max([c for c, r in a[1]]) + 1  # rechts vom X-3erpaar wird stein gesetzt
                    elif f[max([c for c, r in a[1]]) + 1][a[1][0][
                                                              1] - 1] != 0:  # nicht auf höhe 0, und wenn feld X=+1 Y=-1 (rechts daneben ein mal nach unten) nicht frei ist
                        print("REEECHTS (schlauer WIN)")
                        return max([c for c, r in a[1]]) + 1

                # POSITIV DIAGONAL
                if a[0] == 2 and min([c for c, r in a[1]]) - 1 >= 0 and min(
                        [r for c, r in a[1]]) - 1 >= 0:  # um out of range errors zu vermeiden
                    if f[min([c for c, r in a[1]]) - 1][min([r for c, r in a[1]]) - 1] == 0:  # zielfeld frei?
                        if min([r for c, r in a[1]]) - 1 - self.get_num_of_stones_in_column(
                                min([c for c, r in a[1]]) - 1, f) == 0:  # höhendifferenz == 0
                            print("diagonaler WIN links unten")
                            return min([c for c, r in a[1]]) - 1
                if a[0] == 2 and max([c for c, r in a[1]]) + 1 <= 6 and max(
                        [r for c, r in a[1]]) + 1 <= 5:  # um out of range errors zu vermeiden
                    if f[max([c for c, r in a[1]]) + 1][max([r for c, r in a[1]]) + 1] == 0:
                        if max([r for c, r in a[1]]) + 1 - self.get_num_of_stones_in_column(
                                max([c for c, r in a[1]]) + 1, f) == 0:  # höhendifferenz == 0
                            print("diagonaler WIN rechts oben")
                            return max([c for c, r in a[1]]) + 1
                # NEGATIV DIAGONAL
                if a[0] == 3 and min([c for c, r in a[1]]) - 1 >= 0 and max(
                        [r for c, r in a[1]]) + 1 <= 5:  # um out of range errors zu vermeiden
                    if f[min([c for c, r in a[1]]) - 1][max([r for c, r in a[1]]) + 1] == 0:
                        if max([r for c, r in a[1]]) + 1 - self.get_num_of_stones_in_column(
                                min([c for c, r in a[1]]) - 1, f) == 0:  # höhendifferenz == 0
                            print("negdiagonaler WIN links oben")
                            return min([c for c, r in a[1]]) - 1
                if a[0] == 3 and max([c for c, r in a[1]]) + 1 <= 6 and min(
                        [r for c, r in a[1]]) - 1 >= 0:  # um out of range errors zu vermeiden
                    if f[max([c for c, r in a[1]]) + 1][min([r for c, r in a[1]]) - 1] == 0:
                        if min([r for c, r in a[1]]) - 1 - self.get_num_of_stones_in_column(
                                max([c for c, r in a[1]]) + 1, f) == 0:  # höhendifferenz == 0
                            print("negdiagonaler WIN rechts unten")
                            return max([c for c, r in a[1]]) + 1
        return 420  # falls es keine winoption gibt

    def get_triples(self, f, p=1):
        _return = []
        for a in range(self.BOARD_WIDTH):
            for b in range(self.BOARD_HEIGHT):
                if f[a][b] == p:
                    _stone_data = self.check_win(f, (a, b), 3)
                    if _stone_data[0] and _stone_data[
                        1] != 4:  # wenn 3erpaar gefunden wurde UND type != 4 (4 bedeutet dass die zurückgegebene liste mehr als einen type beinhaltet)
                        _return.append([_stone_data[1], _stone_data[2]])  # [ [type, [list with stonecoords]] ]
                    elif _stone_data[0] and _stone_data[1] == 4:
                        for i in _stone_data[2]:
                            _return.append(i)  # [ [type, [list with stonecoords]] * len(_stone_data[2]) ]
        return self.delete_multiple_coords(_return)

    def delete_multiple_coords(self, L):
        # [ [X, [[0,1], [1,1], [2,1]]], [X, [[1,1], [0,1], [2,1]]] ]   <--- beispiel
        for a in L:
            [L.remove(b) for b in L if a[0] == b[0] and a != b and a[1][0] in b[
                1]]  # man betrachte 2 elemente a und b, wenn ihr typ(x,y,dia,negdia) gleich ist und die erste stonecoord in a in der stonecoordlist von b vorkommt dann kann b aussortiert werden
        return L

    def get_num_of_stones_in_column(self, c, f):

        for n in range(5, -1, -1):
            if f[c][n] != 0:
                return n + 1  # gibt anzahl steine zurück (zählt nicht ab 0 sondern ab 1)
            elif n == 0:
                return 0


def gameplay_loop():
    connect_four = Game()

    while not connect_four.game_over:
        connect_four.update()
        connect_four.handle_events()
        connect_four.render()
        connect_four.render_text()

if __name__ == '__main__':
    gameplay_loop()