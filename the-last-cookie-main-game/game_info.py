class GameInfo:

    author = "Anonymous"

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print(f"Welcome to {self.title}")

    @staticmethod
    def info():
        print("Made using OOP in python (c) Jo Baker, Funmi Falegan, Karan Kaur, Anna Robertson and Ahartisha "
              "Selakanabarajah")

    @classmethod
    def credits(cls):
        print("Thanks for playing!")
        print(f"This game was created by {cls.author}")
