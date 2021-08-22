from room import Room
from game_info import GameInfo
from character import Character
import os
import sys

class Game1:

    def __init__(self):
        game_name = GameInfo("The Last Cookie")
        game_name.welcome()
        GameInfo.info()
        GameInfo.author = "\nJo Baker, Funmi Falegan, Karan Kaur, Anna Robertson and Ahartisha Selakanabarajah"
        self.char_name = input("\nHello young Digestive Detective. What is your name?: ")
        self.main_room_vists = 0
        self.clues = []
        self.current_room = None


def main():
    play = Game1()
    play.maryland_cookie_master = Character("The Maryland Cookie Master", "He is the master of the cookie-verse")
    play.maryland_cookie_master.set_conversation("You must traverse my maze and retrieve the cookie crumbs for the "
                                                 "first clue!")

    play.cookie_mistress = Character("Cookie Mistress", "This is the mistress of the house.")
    play.cookie_mistress.set_conversation("Let’s settle this for the last time which biscuit is superior, jammie "
                                          "dodgers or chocolate chip cookies. If you can beat me I'll give you my "
                                          "clue.")

    play.vin_diesel = Character("Vin Diesel", "He is fast and he is furious")
    play.vin_diesel.set_conversation("Family is everything. Help me save Gingy from Lord Farquaad\'s interrogation!\n"
                                     "Guess the cookie-related word to get the clue and save Gingy before he is broken "
                                     "apart")

    play.queen_rich_tea = Character("Queen Rich Tea", "")
    play.queen_rich_tea.set_conversation("For every Rich Tea biscuit, there are currently thousands of tea biscuits "
                                         "living in poverty, so why on earth am I being treated like a tart in this "
                                         "god-forsaken place for something I haven't done?!\nAny who, this book has "
                                         "been in my family for generations and it\'s about a place where The Last "
                                         "Cookie was originally made.\nNow please let me go because this place really "
                                         "takes the biscuit!")

    play.jammie_dodger = Character("Major Jamie Dodger-McCrumbs", "He has a heart of jam, but a ferocious temper which "
                                                                  "makes for some sticky situations")
    play.jammie_dodger.set_conversation("You must score 5 points against me to escape this bread and jam!")

    play.sherlock_scones = Character("Sherlock Scones", "")

    room_0 = Room("The Main Hall")
    room_0.set_description("There are four doors coming off this room and a set of stairs that lead down to the "
                           "basement.")
    room_0.set_clue(None)
    room_0.set_character(play.sherlock_scones)
    play.sherlock_scones.set_room(room_0)

    room_1 = Room("The Maryland Maze")
    room_1.set_description("You see a path laid out before you, which way will you turn?")
    room_1.set_clue("Clue One")
    room_1.set_character(play.maryland_cookie_master)
    play.maryland_cookie_master.set_room(room_1)

    room_2 = Room("Karan Room")
    room_2.set_description('As you approach this room you hear a cry "Not my gum drop button!"')
    room_2.set_clue("Clue Two")
    room_2.set_character(play.vin_diesel)
    play.vin_diesel.set_room(room_2)

    room_3 = Room("Funmi Room")
    room_3.set_description("You approach the door to the south of the main room, the door is a pastel pink colour with "
                           "aromas as sweet as a bakery. As you enter you see an elegant figure, decorated from head to"
                           " toe with jewels and pearls.  In the room you see an assortment of chocolate chip cookies "
                           "and jammie dodgers lined up in rows.")
    room_3.set_clue("Clue Three")
    room_3.set_character(play.cookie_mistress)
    play.cookie_mistress.set_room(room_3)

    room_4 = Room("Tish Room")
    room_4.set_description("You approach the door to the west of the main room and it creaks as you open it. There is a"
                           " figure who is sitting on the chair, drumming her fingernails impatiently on the table.\n"
                           "She sees you and stands up, handing you an old book that she says may prove her innocence "
                           "in this case.\nYou blow the dust off of the front cover and you see the title "
                           "'The Legend of El Do-Cookie-Rado'.\n")
    room_4.set_clue("Clue Four")
    room_4.set_character(play.queen_rich_tea)
    play.queen_rich_tea.set_room(room_4)

    room_5 = Room("The Kitchen")
    room_5.set_description("You are stood in a kitchen. Suddenly a giant Jammie Dodger biscuit begins hurtling towards "
                           "you! Quick! Use your loaf!")
    room_5.set_clue("Clue Five")
    room_5.set_character(play.jammie_dodger)
    play.jammie_dodger.set_room(room_5)

    room_0.link_room(room_1, "north")
    room_0.link_room(room_2, "east")
    room_0.link_room(room_3, "south")
    room_0.link_room(room_4, "west")
    room_0.link_room(room_5, "downstairs")
    room_1.link_room(room_0, "south")
    room_2.link_room(room_0, "west")
    room_3.link_room(room_0, "north")
    room_4.link_room(room_0, "east")
    room_5.link_room(room_0, "upstairs")

    play.current_room = room_0
    while True:
        print("\n")
        if play.current_room == room_0:
            play.main_room_vists += 1
        if play.main_room_vists <= 1:
            play.sherlock_scones.set_conversation(
                "Hello there young Detective Digestive. To solve the mystery of who ate "
                "'The Last Cookie' you must collect the clues from around the Gingerbread "
                "House.\nYou can navigate by moving the directions of the rooms.\n"
                "Come back to me when you have all five of the clues.\n"
                "To check how many clues you have input 'i'.\n"
                "Good luck!")
        else:
            play.sherlock_scones.set_conversation("Hello there young Detective Digestive. I see you have visited some "
                                                  "rooms. Do you have enough clues to solve the puzzle? y/n: ")
            if play.command == "y":
                if len(play.clues) >= 5:
                    print("Congratulations, you have solved the mystery!")
                    GameInfo.credits()
                    sys.exit()
                else:
                    print("Sorry, you need to find more clues!")
            elif play.command == "n":
                print("Never give up, Detective. This mystery will be solved!")

        play.current_room.get_details()
        occupier = play.current_room.get_character()
        if occupier is not None:
            action = input(f"Do you want to talk to the person in this room? y/n: ")
            if action == "y":
                occupier.talk()
                if play.current_room is not room_0:
                    decision = input("Do you want to enter this room? y/n:")
                    if decision == "y":
                        if play.current_room == room_1:
                            play.clues.append(play.current_room.get_clue())
                            print("You enter a maze made of lush green hedges. Can you find the cookie crumbs?")
                            os.startfile("maze_puzzle.exe")
                        elif play.current_room == room_2:
                            play.clues.append(play.current_room.get_clue())
                        elif play.current_room == room_3:
                            play.clues.append(play.current_room.get_clue())
                        elif play.current_room == room_4:
                            print("After you open up the book, the room begins to shift and suddenly you\'re falling "
                                  "through a vortex then you hit the ground except it\'s not the ground...it\'s made "
                                  "of cookie dough!\nNow you look around and you realise you\'re in El Do-Cookie-Rado!"
                                  "\nThat means there\'s a clue here somewhere!")
                            play.clues.append(play.current_room.get_clue())
                        elif play.current_room == room_5:
                            play.clues.append(play.current_room.get_clue())
                            os.startfile("baguette_tennis.exe")
                    if decision == "n":
                        print("Please pick another action or a direction to move.")
            if action == "n":
                print("Please pick another action or a direction to move.")

        play.command = input("> ")
        if play.command == "i":
            if len(play.clues) > 0:
                print(play.clues)
            else:
                print("You do not have any clues yet!")
        else:
            play.current_room = play.current_room.move(play.command)


if __name__ == '__main__':
    main()

