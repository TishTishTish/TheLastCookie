
# import modules
import turtle # import turtle
import winsound # sound for windows machines
import random # need to create random direction for start / computer moves

# create classes

# create functions
def start_game():
    global game_state
    game_state = "game"

# screen and game set-up
window = turtle.Screen() # screen window
window.title("Baguette Tennis") # screen title
window.bgcolor("black") # background colour
window.setup(width=800, height=600) # screen size
window.tracer(0) # stops window from updating - makes faster


# turtle object
# ball_shape = turtle.Turtle()
# baguette_shape = turtle.Turtle()
  
# registering the images as new shapes
turtle.register_shape('jammie_dodger.gif')
turtle.register_shape('baguette_1_left.gif')
turtle.register_shape('baguette_2_right.gif')

# score and win state initialisation
human = 0
computer = 0
human_wins = False
computer_wins = False

# Baguette_1 - Human
baguette_1 = turtle.Turtle()
# baguette_1.speed(0) # speed of animation
baguette_1.shape("baguette_1_left.gif") # sprite
baguette_1.penup() # stops line tracing across screen
baguette_1.goto(-350, 0) # starting co-ordinate

# Baguette_2 - Computer
baguette_2 = turtle.Turtle()
# baguette_2.speed(0)
baguette_2.shape("baguette_2_right.gif") # sprite
baguette_2.penup() # stops line tracing across screen
baguette_2.goto(350, 0) # starting co-ordinate

# ball (Jammie Dodger)
ball = turtle.Turtle()
# ball.speed(0) # speed of animation
ball.shape("jammie_dodger.gif")
ball.penup() # stops line tracing across screen
ball.goto(0, 0) # starting co-ordinates
ball.dx = 1 # amount pixels moving (x)
ball.dy = 1 # amount pixels moving (y)


# scoreboard
pen = turtle.Turtle()
pen.speed(0)
# pen.shape("square")
pen.color("white")
pen.penup() # avoids drawing line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Detective: 0  /  Jamie Dodger: 0", align="center", font=("San Serif", 16, "normal"))

# movement of baguettes
def baguette_1_up():
    y = baguette_1.ycor() # returns the y co-ordinate
    y += 25
    baguette_1.sety(y)

def baguette_1_down():
    y = baguette_1.ycor() # returns the y co-ordinate
    y -= 25
    baguette_1.sety(y)

def baguette_2_up():
    y = baguette_2.ycor() # returns the y co-ordinate
    y += 0.7
    baguette_2.sety(y)

def baguette_2_down():
    y = baguette_2.ycor() # returns the y co-ordinate
    y -= 0.7
    baguette_2.sety(y)

# need to randomise the computer movement

# listening for keyboard input 
window.listen()
window.onkeypress(start_game, "space")
window.onkeypress(baguette_1_up, "Up")
window.onkeypress(baguette_1_down, "Down")

game_state = "splash"


# Main game loop
while True:
    window.update() # every time loop runs it updates screen
    
    if game_state == "splash":
        window.bgpic("splash.gif")
        
    elif game_state == "game":
        window.bgpic("nopic")
        
#     elif game_state == "gameover":
#         window.bgpic("game_over.gif")
#         
        
        # move the ball
        ball.setx(ball.xcor() + ball.dx) # setx()
        ball.sety(ball.ycor() + ball.dy) # sety()
        

        # checks gameplay area
        
        # top 
        if ball.ycor() > 270:
            ball.sety(270)
            ball.dy *= -1
            winsound.PlaySound("splat_wall.wav", winsound.SND_ASYNC)

        # bottom
        elif ball.ycor() < -270:
            ball.sety(-270)
            ball.dy *= -1
            winsound.PlaySound("splat_wall.wav", winsound.SND_ASYNC)

        # Left and right
        if ball.xcor() > 325: # past right paddle off screen
            ball.goto(0, 0) # back to centre
            ball.dx = 1 # reset to initial speed
            human += 1 # player a scores a point
            pen.clear() # clears
            pen.write("Detective: {}  /  Jamie Dodger: {}".format(human, computer), align="center", font=("San Serif", 16, "normal"))
           
        elif ball.xcor() < -325: # past left paddle off screen
            ball.goto(0, 0) # back to centre
            ball.dx = 1 # resets to initial speed
            computer += 1 # player b scores a point
            pen.clear() # clears
            pen.write("Detective: {}  /  Jamie Dodger: {}".format(human, computer), align="center", font=("San Serif", 16, "normal"))    
            

        # Paddle and ball collisions
        if ball.xcor() < -320 and ball.ycor() < baguette_1.ycor() + 100 and ball.ycor() > baguette_1.ycor() - 100:
            ball.dx *= -1
            ball.dx +=0.2 # speed it up
            winsound.PlaySound("splat_baguette.wav", winsound.SND_ASYNC)
        
        elif ball.xcor() > 320 and ball.ycor() < baguette_2.ycor() + 100 and ball.ycor() > baguette_2.ycor() - 100:
            ball.dx *= -1
            ball.dx -=0.2 # speed it up
            winsound.PlaySound("splat_baguette", winsound.SND_ASYNC)

        # computer player movements
        if baguette_2.ycor() < ball.ycor() and abs(baguette_2.ycor() - ball.ycor()) > 20:
            baguette_2_up()
                   
            
        elif baguette_2.ycor() > ball.ycor() and abs(baguette_2.ycor() - ball.ycor()) > 20:
            baguette_2_down()
            

    # score result

        if human == 5:
            turtle.clearscreen()
            human_wins = True
            break

        elif computer == 5:
            turtle.clearscreen()
            computer_wins = True
            break


while True:
    if human_wins:
        window.bgcolor("black")
        pen.penup() # avoids drawing line
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("You win! The clue fragment is: 0000", align="center", font=("Courier New", 16, "normal"))
    elif computer_wins:
        window.bgcolor("black")       
        pen.penup() # avoids drawing line
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Jamie Dodger Wins!", align="center", font=("Courier New", 16, "normal"))
            



        
        
        
