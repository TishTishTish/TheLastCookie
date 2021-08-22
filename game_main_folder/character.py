import room
# from game_main_folder import main_game

class Character:

    # # # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.actions = None

    # # # Describe this character
    def describe(self):
        print(f"{self.name} is standing nearby!")
        print(self.description)

    # # # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # # # get what this character says when talked to
    def get_conversation(self):
        return self.conversation

    def set_room(self, room):
        self.room = room

    def get_room(self):
        return room

    def talk(self):
        if self.conversation is not None:
            print("----------------------")
            print(f"[{self.name} says]: {self.conversation}")
            print("----------------------")
        else:
            print("----------------------")
            print(f"{self.name} doesn't want to talk to you")
            print("----------------------")

