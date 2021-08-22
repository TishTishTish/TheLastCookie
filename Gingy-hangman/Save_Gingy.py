import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()
Height = 480
Width = 800

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Save Gingy | The Last Cookie")

btn_font = pygame.font.Font("Gingy-Hangman-Graphics/Peaberry-Mono.otf", 20)
letter_font = pygame.font.Font("Gingy-Hangman-Graphics/Peaberry-Mono.otf",40)
game_font = pygame.font.Font("Gingy-Hangman-Graphics/Peaberry-Mono.otf", 25)
title_font = pygame.font.Font("Gingy-Hangman-Graphics/Peaberry-Mono.otf", 30)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (190, 169, 223)
PINK = (225, 138, 170)

IMAGES = []
hangman_status = 0
for i in range(7):
    image = pygame.image.load(f'Gingy-Hangman-Graphics/gingy{i}.png')
    IMAGES.append(image)

# Buttons
ROWS = 2
COLS = 13
GAP = 20
SIZE = 40
BOXES = []

for row in range(ROWS):
    for col in range(COLS):
        x = ((GAP * col) + GAP) + (SIZE * col)
        y = ((GAP * row) + GAP) + (SIZE * row) + 330
        box = pygame.Rect(x,y,SIZE,SIZE)
        BOXES.append(box)

A = 65
BUTTONS = []

for ind, box in enumerate(BOXES):
    letter = chr(A+ind)
    button = ([box, letter])
    BUTTONS.append(button)

def draw_btns(BUTTONS):
    for button,letter in BUTTONS:
        btn_text = btn_font.render(letter, True, WHITE)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, PINK, button)
        screen.blit(btn_text, btn_text_rect)

def display_guess():
    display_word = ''

    for letter in WORD:
        if letter in GUESSED:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    text = letter_font.render(display_word, True, BLACK)
    screen.blit(text, (400,150))

GUESSED = []

def random_word():
    file = open('Gingy-Hangman-Words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]

WORD = random_word()

def title_screen():
    #screen.fill(PURPLE)
    castle = pygame.image.load('Gingy-Hangman-Graphics/farquaad_castle.png')
    screen.blit(castle, (0, 0))
    logo = pygame.image.load('Gingy-Hangman-Graphics/Save_Gingy_Logo_2.png')
    screen.blit(logo, (230, 30))
    title_text = title_font.render('Press any key to begin', True, BLACK)
    screen.blit(title_text, (200, 400))
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def running():
    global hangman_status
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = event.pos

                for button, letter in BUTTONS:
                    if button.collidepoint(clicked_pos):
                        GUESSED.append(letter)

                        if letter not in WORD:
                            hangman_status += 1

                        if hangman_status == 6:
                            game_over = True

                        BUTTONS.remove([button, letter])

        screen.fill(PURPLE)
        screen.blit(IMAGES[hangman_status], (50, 70))
        draw_btns(BUTTONS)
        display_guess()

        game_won = True
        for letter in WORD:
            if letter not in GUESSED:
                game_won = False

        if game_won:
            game_over = True
            game_over_message = 'You saved Gingy and gained Clue Number 2!'
        else:
            game_over_message = f'Oh no! The answer was: {WORD}. Try again.'
        pygame.display.update()
        clock.tick(50)

        if game_over:
            if game_over:
                pygame.time.delay(1000)
                screen.fill(PINK)
                game_over_text = game_font.render(game_over_message, True, BLACK)
                game_over_text_rect = game_over_text.get_rect(center=(Width // 2, Height // 2))
                screen.blit(game_over_text, game_over_text_rect)
                pygame.display.update()
                pygame.time.delay(2500)
                sys.exit()


title_screen()
running()
pygame.quit()
