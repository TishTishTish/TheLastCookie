import turtle
import time

# create the screen for the turtle game
window = turtle.Screen()
window.screensize(800, 600)
# create a list called pixels which stores the lines of the maze
pixels = list()


class Game:

    # maze creation: 1s are walls 0s are space
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
          [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
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

    def __init__(self):
        self.game_state = "splash"  # start the game with a splash screen
        self.start_screen()
        # set the state of variables
        self.cookie_crumbs = False
        self.found_fountain = False
        self.no_win = False

    # separate the constructor into a second function that runs when the game state changes to "game"
    def init_game_state(self):
        turtle.hideturtle()
        turtle.title("Maryland Maze")
        turtle.bgcolor("Beige")
        self.detective_player = turtle.Turtle()
        turtle.tracer(0)
        self.make_maze(self.hl, self.vl, -320, 300)
        self.start()
        self.winning_pos = (-325, 199)
        self.crumb_placement()
        self.fountain_placement()
        turtle.update()
        turtle.tracer(1)

    # horizontal line creation for the maze
    def make_horizontal_line(self, hl, x, y):
        if self.game_state == "game":
            line_horizontal = turtle.Turtle()
            line_horizontal.speed(0)
            line_horizontal.hideturtle()
            line_horizontal.up()
            line_horizontal.setposition(x, y)
            for n in hl:
                if n == 1:
                    for i in range(4):
                        line_horizontal.forward(42 / 8)
                        pixel = line_horizontal.clone()
                        pixel.showturtle()
                        pixel.shape("square")
                        pixel.color("DarkGreen")
                        pixel.shapesize(2 / 40, 21 / 40)
                        pixels.append(pixel)
                        line_horizontal.forward(42 / 8)

                if n == 0:
                    line_horizontal.forward(42)

    def create_horizontal_lines(self, hl, x, y):
        if self.game_state == "game":
            step_y = y
            for n in hl:
                self.make_horizontal_line(n, x, step_y)
                step_y -= 42

    # vertical line creation for the maze
    def make_vertical_line(self, vl, x, y):
        if self.game_state == "game":
            line_v = turtle.Turtle()
            line_v.hideturtle()
            line_v.speed(0)
            line_v.up()
            line_v.setposition(x, y)
            line_v.right(90)
            for n in vl:
                if n == 1:
                    for i in range(4):
                        line_v.forward(42 / 8)
                        pixel = line_v.clone()
                        pixel.showturtle()
                        pixel.shape("square")
                        pixel.color("DarkGreen")  # pick a colour appropriate for rest of team's colour schemes
                        pixel.shapesize(2 / 40, 21 / 40)
                        pixels.append(pixel)
                        line_v.forward(42 / 8)
                if n == 0:
                    line_v.forward(42)

    def create_vertical_lines(self, vl, x, y):
        if self.game_state == "game":
            step_right = x
            for n in vl:
                self.make_vertical_line(n, step_right, y)
                step_right += 42

    # function for the splash screen, when "f" is pressed, state_of_game function is called and game state is changed
    def start_screen(self):
        if self.game_state == "splash":
            window.bgpic("maze-images/start_image.gif")
            window.listen()
            window.onkeypress(self.state_of_game, "f")

    # changes the state_of_game to "game" to run the main game
    def state_of_game(self):
        self.game_state = "game"
        window.bgpic("nopic")
        self.init_game_state()

    # creates the maze if game state is "game"
    def make_maze(self, hl, vl, x, y):
        if self.game_state == "game":
            self.create_horizontal_lines(hl, x, y)
            self.create_vertical_lines(vl, x, y)

    # places the player in the maze
    def start(self):
        if self.game_state == "game":
            starting_pos = (335, -181)
            # starting_pos = (-258, 196)  # starting position for testing win
            turtle.hideturtle()
            window.register_shape('maze-images/pikachu_left.gif')
            self.detective_player.shape('maze-images/pikachu_left.gif')
            self.detective_player.speed(3)
            self.detective_player.up()
            self.detective_player.setposition(starting_pos)
            self.detective_player.setheading(180)
            self.detective_player.color("DarkMagenta")
            self.detective_player.up()
            self.detective_player.down()

    # places the crumbs in the maze
    def crumb_placement(self):
        if self.game_state == "game":
            self.crumbs_position = (288, -223)
            # self.crumbs_position = (-218, 195)  # crumb position for testing win
            self.cookie_crumbs_image = ('maze-images/cookie_crumbs.gif')
            window.register_shape(self.cookie_crumbs_image)
            self.crumbs = turtle.Turtle(shape=self.cookie_crumbs_image)
            self.crumbs.penup()
            self.crumbs.setposition(self.crumbs_position)

    # places the fountain in the maze
    def fountain_placement(self):
        if self.game_state == "game":
            self.fountain_position = (-5, -14)
            self.fountain_image = ("maze-images/fountain.gif")
            window.register_shape(self.fountain_image)
            self.fountain = turtle.Turtle(shape=self.fountain_image)
            self.fountain.penup()
            self.fountain.setposition(self.fountain_position)

    # creates collision with the maze walls
    def collision(self):
        if self.game_state == "game":
            for i in range(25):
                self.detective_player.forward(1)
                if any(pixel.distance(self.detective_player) < 7 for pixel in pixels):
                    break

    # changes the cookie_crumbs variable to True if the player comes <20 pixels to the crumbs
    def find_crumbs(self):
        if self.game_state == "game":
            if self.false_cookie_crumbs() and self.is_detective_near_crumbs():
                self.cookie_crumbs = True
                self.crumbs.hideturtle()
                message_position = (0, -340)
                crumbs_message = ('maze-images/crumbs_message.gif')
                window.register_shape(crumbs_message)
                message = turtle.Turtle(shape=crumbs_message)
                message.penup()
                message.setposition(message_position)
                time.sleep(3)
                message.hideturtle()

    # a function to define proximity to the cookie crumbs
    def is_detective_near_crumbs(self):
        return self.detective_player.distance(self.crumbs_position) <= 20

    # changes the found_fountain variable to True if the player comes <20 pixels to the fountain
    def find_fountain(self):
        if self.game_state == "game":
            if self.found_fountain is False and self.is_detective_near_fountain():
                self.found_fountain = True
                self.speed = self.detective_player.speed(0)
                message_position = (0, -340)
                fountain_message = ('maze-images/fountain_message.gif')  # create a fountain message
                window.register_shape(fountain_message)
                message = turtle.Turtle(shape=fountain_message)
                message.penup()
                message.setposition(message_position)
                time.sleep(3)
                message.hideturtle()

    # a function to define proximity to the fountain
    def is_detective_near_fountain(self):
        return self.detective_player.distance(self.fountain_position) <= 20

    # a function to determine if the player has or has not fulfilled the parameters to win the game
    def win(self):
        if self.game_state == "game":
            if self.is_detective_near_winning_position() and self.true_cookie_crumbs():
                self.game_state = "win"
                self.win_screen()
            elif self.is_detective_near_winning_position() and self.false_cookie_crumbs() and self.false_no_win():
                self.true_no_win()
                message_position = (0, -340)
                no_win_message = ('maze-images/no_win_message.gif')
                window.register_shape(no_win_message)
                message = turtle.Turtle(shape=no_win_message)
                message.penup()
                message.setposition(message_position)
                time.sleep(2)
                message.hideturtle()

    # The player has not won the game - this stops the message displaying in a loop when at the winning_position
    def true_no_win(self):
        self.no_win = True

    # The player has not won the game
    def false_no_win(self):
        return self.no_win is False

    # The player has not picked up the cookie crumbs
    def false_cookie_crumbs(self):
        return self.cookie_crumbs is False

    # The player has picked up the cookie crumbs - this allows the image of the crumbs to be removed
    def true_cookie_crumbs(self):
        return self.cookie_crumbs is True

    # if game_state is "win" display the win screen, on "f" replay the game, on "enter" quit the game
    def win_screen(self):
        if self.game_state == "win":
            turtle.clearscreen()
            window.bgpic("maze-images/end_screen.gif")
            window.listen()
            window.onkeypress(main, "f")
            window.onkeypress(self.close, "Return")

    # a function to define proximity to the winning position
    def is_detective_near_winning_position(self):
        return self.detective_player.distance(self.winning_pos) <= 20

    # movement function for right
    def right(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_left.gif')
        self.detective_player.shape('maze-images/pikachu_left.gif')
        self.collision()
        self.detective_player.speed(0)
        self.detective_player.right(0)

    # movement function for left
    def left(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_right.gif')
        self.detective_player.shape('maze-images/pikachu_right.gif')
        self.detective_player.right(180)
        self.collision()
        self.detective_player.speed(0)
        self.detective_player.right(-180)

    # movement function for down
    def down(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_up.gif')
        self.detective_player.shape('maze-images/pikachu_up.gif')
        self.detective_player.right(90)
        self.collision()
        self.detective_player.speed(0)
        self.detective_player.right(-90)

    # movement function for up
    def up(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_down.gif')
        self.detective_player.shape('maze-images/pikachu_down.gif')
        self.detective_player.right(-90)
        self.collision()
        self.detective_player.speed(0)
        self.detective_player.right(90)

    # movement function for backtracking over the drawn line - right
    def undo_right(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_right.gif')
        self.detective_player.shape('maze-images/pikachu_right.gif')
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()

    # movement function for backtracking over the drawn line - left
    def undo_left(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_left.gif')
        self.detective_player.shape('maze-images/pikachu_left.gif')
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()

    # movement function for backtracking over the drawn line - down
    def undo_down(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_down.gif')
        self.detective_player.shape('maze-images/pikachu_down.gif')
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()

    # movement function for backtracking over the drawn line - up
    def undo_up(self):
        self.win()
        self.find_crumbs()
        self.find_fountain()
        window.register_shape('maze-images/pikachu_up.gif')
        self.detective_player.shape('maze-images/pikachu_up.gif')
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()
        self.detective_player.undo()

    # close the turtle window
    def close(self):
        window.bye()

    # display coordinates on buttonclick on the screen - used for determining positions for elements of the game
    def buttonclick(self, x, y):
        print(f"You clicked at this coordinate({x},{y})")

# the main function that runs the game
def main():
    play = Game()
    window.onkeypress(play.right, "a")
    window.onkeypress(play.left, "d")
    window.onkeypress(play.up, "s")
    window.onkeypress(play.down, "w")
    window.onkeypress(play.close, "q")
    window.onkeypress(play.undo_right, "Right")
    window.onkeypress(play.undo_left, "Left")
    window.onkeypress(play.undo_down, "Down")
    window.onkeypress(play.undo_up, "Up")
    # window.onscreenclick(play.buttonclick, 1)
    window.listen()
    window.mainloop()
    turtle.done()


if __name__ == '__main__':
    main()
