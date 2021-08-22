### future features ###

# 1/ link back into main game
# 2/ redo simple code into OOP
# 3/ ball movement in a function
# 4/ specular reflection or random angle of ball on return
# 5/ spinning jammie dodger which spins in different direction on return
# 6/ better collision detection
# 7/ sort out speed being different on different computers!



# import modules
import turtle # import turtle
import winsound # sound for windows machines
import random # for random angle of ball on return - feature to add


# game state to start game
def start_game():
    global game_state
    game_state = "game_on"


# screen and game set-up
window = turtle.Screen() # screen window
window.title("Baguette Tennis") # screen title
window.bgcolor("black") # background colour
window.setup(width=800, height=600) # screen size
window.tracer(0) # stops window from updating - makes faster


# registering .gif images as new shapes
turtle.register_shape('jammie_dodger.gif')
turtle.register_shape('baguette_1_left.gif')
turtle.register_shape('baguette_2_right.gif')


# score and win state initialisation
human = 0
computer = 0
human_wins = False
computer_wins = False
game_state = "title_screen"


# Baguette_1 - Human
baguette_1 = turtle.Turtle()
baguette_1.shape("baguette_1_left.gif") # baguette_1 image
baguette_1.penup() # stops line tracing across screen
baguette_1.goto(-350, 0) # starting co-ordinate


# Baguette_2 - Computer
baguette_2 = turtle.Turtle()
baguette_2.shape("baguette_2_right.gif") # baguette_2 image
baguette_2.penup() # stops line tracing across screen
baguette_2.goto(350, 0) # starting co-ordinate


# ball (Jammie Dodger)
ball = turtle.Turtle()
ball.shape("jammie_dodger.gif") # ball image
ball.penup() # stops line tracing across screen
ball.goto(0, -20) # starting co-ordinates
ball.dx = 1 # amount pixels moving (x)
ball.dy = 1 # amount pixels moving (y)


# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # avoids drawing line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Detective: 0  /  Jamie Dodger: 0", align="center", font=("Courier New", 16, "normal"))


# movement of baguettes
def baguette_1_up():
    y = baguette_1.ycor() # returns the y co-ordinate
    y += 25 # amount of movement 
    baguette_1.sety(y)
    
def baguette_1_down():
    y = baguette_1.ycor() # returns the y co-ordinate
    y -= 25 # amount of movement
    baguette_1.sety(y)

def baguette_2_up():
    y = baguette_2.ycor() # returns the y co-ordinate
    y += 0.77 # slower speed for computer to allow human to win sometimes!
    baguette_2.sety(y)

def baguette_2_down():
    y = baguette_2.ycor() # returns the y co-ordinate
    y -= 0.77 # slower speed for computer to allow human to win sometimes!
    baguette_2.sety(y)


# listening for keyboard input 
window.listen()
window.onkeypress(start_game, "space")
window.onkeypress(baguette_1_up, "Up")
window.onkeypress(baguette_1_down, "Down")


# Main game loop
while True:
    window.update() # every time loop runs it updates screen
    
    if game_state == "title_screen": # checks game state           
        window.bgpic("title_screen.gif") # displays title screen
        
    elif game_state == "game_on": # checks game state 
        window.bgpic("nopic") # clears title screen to play game
        
           
        # moving the ball
        ball.setx(ball.xcor() + ball.dx) # setx()
        ball.sety(ball.ycor() + ball.dy) # sety()
        

        # checks gameplay area limits
        
        # top 
        if ball.ycor() > 270:
            ball.sety(270)
            ball.dy *= -1 # reverse ball direction
            winsound.PlaySound("splat_wall.wav", winsound.SND_ASYNC)

        # bottom
        elif ball.ycor() < -270:
            ball.sety(-270)
            ball.dy *= -1 # reverse ball direction
            winsound.PlaySound("splat_wall.wav", winsound.SND_ASYNC)

        # left side    
        if ball.xcor() < -325: # past baguette_1 and off screen
            ball.goto(0, -20) # returns to start position
            ball.dx = -1 # reset to initial speed and next go ball goes towards opponent
            computer += 1 # player b scores a point
            pen.clear() # clears
            winsound.PlaySound("evil_laugh.wav", winsound.SND_ASYNC)
            pen.write("Detective: {}  /  Jamie Dodger: {}".format(human, computer), align="center", font=("Courier New", 16, "normal"))
        
        # right side
        elif ball.xcor() > 325: # past baguette_2 and off screen
            ball.goto(0, -20) # returns to start position
            ball.dx = 1 # reset to initial speed and next go ball goes towards opponent
            human += 1 # player a scores a point
            pen.clear() # clears
            winsound.PlaySound("win_point.wav", winsound.SND_ASYNC)
            pen.write("Detective: {}  /  Jamie Dodger: {}".format(human, computer), align="center", font=("Courier New", 16, "normal"))
            

        # Baguette and ball collisions
        if ball.xcor() < -320 and ball.ycor() < baguette_1.ycor() + 100 and ball.ycor() > baguette_1.ycor() - 100:
            ball.dx *= -1 # ball reverse direction
            ball.dx +=0.2 # speed ball up
            winsound.PlaySound("splat_baguette.wav", winsound.SND_ASYNC)
        
        elif ball.xcor() > 320 and ball.ycor() < baguette_2.ycor() + 100 and ball.ycor() > baguette_2.ycor() - 100:
            ball.dx *= -1 # ball reverse direction
            ball.dx -=0.2 # speed it up
            winsound.PlaySound("splat_baguette", winsound.SND_ASYNC)

        # computer player movements
        if baguette_2.ycor() < ball.ycor() and abs(baguette_2.ycor() - ball.ycor()) > 20:
            baguette_2_up()
                               
        elif baguette_2.ycor() > ball.ycor() and abs(baguette_2.ycor() - ball.ycor()) > 20:
            baguette_2_down()
            

    # score result
        if human == 5: # checks if human score is 5
            turtle.clearscreen() # clears screen
            human_wins = True
            break

        elif computer == 5: # checks if computer score is 5
            turtle.clearscreen() # clears screen
            computer_wins = True 
            break 


while True:
    if human_wins:
        window.bgcolor("black") # background colour
        window.bgpic("end_win_screen.gif")
        time.sleep(3)
        window.bye()             
    
        
    elif computer_wins:
        window.bgcolor("black") # background colour
        window.bgpic("end_lose_screen.gif")
        time.sleep(3)
        window.bye()
      

        
