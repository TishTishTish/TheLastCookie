from character import Character

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.clue = None
        self.puzzle = None

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_clue(self, room_clue):
        self.clue = room_clue

    def get_clue(self):
        return self.clue

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # # # set a character for each room
    def set_character(self, new_character):
        self.character = new_character

    # # # get the character for a room
    def get_character(self):
        return self.character

    def get_details(self):
        print("----------------------")
        print(f"You are standing in {self.name}")
        print("----------------------")
        print(self.description)
        occupied = self.get_character()
        if occupied is not None:
            occupied.describe()
        print("----------------------")
        print("Here are the neighbouring rooms:")
        print("----------------------")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"{room.get_name()} is {direction}")
        print("----------------------")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self
