import turtle

turtle.title("Detective maze")

# functions that mark the walls of the maze through lists.

pixels = list()


def make_horizontal_line(hl, x, y):
    line_horizontal = turtle.Turtle()
    line_horizontal.speed(0)
    line_horizontal.hideturtle()
    line_horizontal.up()
    line_horizontal.setposition(x, y)
    for n in hl:
        if n == 1:
            for i in range(2):
                line_horizontal.forward(21 / 4)
                pixel = line_horizontal.clone()
                pixel.showturtle()
                pixel.shape("square")
                pixel.shapesize(1 / 20, 10.5 / 20)
                pixels.append(pixel)
                line_horizontal.forward(21 / 4)

        if n == 0:
            line_horizontal.forward(21)


def create_horizontal_lines(hl, x, y):
    step_y = y
    for n in hl:
        make_horizontal_line(n, x, step_y)
        step_y -= 21


def make_vertical_line(vl, x, y):
    line_v = turtle.Turtle()
    line_v.hideturtle()
    line_v.speed(0)
    line_v.up()
    line_v.setposition(x, y)
    line_v.right(90)
    for n in vl:
        if n == 1:
            for i in range(2):
                line_v.forward(21 / 4)
                pixel = line_v.clone()
                pixel.showturtle()
                pixel.shape("square")
                pixel.shapesize(1 / 20, 10.5 / 20)
                pixels.append(pixel)
                line_v.forward(21 / 4)
        if n == 0:
            line_v.forward(21)


def create_vertical_lines(vl, x, y):
    step_right = x
    for n in vl:
        make_vertical_line(n, step_right, y)
        step_right += 21


# this function marks the entire maze by attaching all the others above

def mark_maze(hl, vl, x, y):
    create_horizontal_lines(hl, x, y)
    create_vertical_lines(vl, x, y)


# create a window for the game

window = turtle.Screen()
window.screensize(600, 400)

# maze creation

hl = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, ],
      [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, ],
      [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, ],
      [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, ],
      [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, ],
      [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, ],
      [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, ],
      [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
      [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, ],
      [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, ],
      [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, ],
      [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, ],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


vl = [[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
      [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, ],
      [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, ],
      [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, ],
      [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, ],
      [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, ],
      [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, ],
      [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, ],
      [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, ],
      [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, ],
      [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, ],
      [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, ],
      [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, ],
      [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, ],
      [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, ],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]

# generate the maze

turtle.tracer(0)
mark_maze(hl, vl, -162, 182)
turtle.update()
turtle.tracer(1)

# movement

starting_pos = (159, -59)
winning_pos = (-163, 134)

def win():
    if detective_player.distance(winning_pos) <= 10:
        print("You escaped the maze!")
        quit()

turtle.hideturtle()
detective_player = turtle.Turtle()
detective_player.speed(0)
detective_player.up()
detective_player.setposition(starting_pos)
detective_player.setheading(180)
detective_player.color("purple")
detective_player.up()
detective_player.down()


def forward(turt):
    win()
    for i in range(10):
        turt.forward(1)
        if any(pixel.distance(turt) < 5 for pixel in pixels):
            break


def right():
    win()
    detective_player.speed(5)
    forward(detective_player)
    detective_player.speed(0)


def left():
    win()
    detective_player.right(180)
    detective_player.speed(5)
    forward(detective_player)
    detective_player.speed(0)
    detective_player.right(-180)


def down():
    win()
    detective_player.right(90)
    detective_player.speed(5)
    forward(detective_player)
    detective_player.speed(0)
    detective_player.right(-90)


def up():
    win()
    detective_player.right(-90)
    detective_player.speed(5)
    forward(detective_player)
    detective_player.speed(0)
    detective_player.right(90)


def close():
    window.bye()


def buttonclick(x,y):
    print(f"You clicked at this coordinate({x},{y})")


x = turtle.xcor()
y = turtle.ycor()

window.onkey(right, "a")
window.onkey(left, "d")
window.onkey(up, "s")
window.onkey(down, "w")
window.onkey(close, "q")
window.onscreenclick(buttonclick, 1)
window.listen()
window.mainloop()
turtle.done()

