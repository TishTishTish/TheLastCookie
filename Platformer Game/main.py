# El Do-Cookie-Rado - Platform Game
# A part of 'The Last Cookie' gamw
# Created by Ahartisha Selakanabarajah

import arcade
import pathlib

# Constants
# Screen Dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "El Do-Cookie-Rado | The Last Cookie"

# Path to the assets folder
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"

# Class that runs the entire game
class Platformer(arcade.Window):
    # Initialise game object
    def __init__(self):
        pass
    
    # Set Up game
    def setup(self):
        pass
    
    # Process key presses
    def on_key_press(self, symbol: int, modifiers: int):
        # return super().on_key_press(symbol, modifiers)
        pass
    
    # Process key releases
    def on_key_release(self, symbol: int, modifiers: int):
        # return super().on_key_release(symbol, modifiers)
        pass
    
    # Update the state of the game and all the objects in it
    def on_update(self, delta_time: float):
        # return super().on_update(delta_time)
        pass
    
    def on_draw(self):
        # return super().on_draw()
        pass

if __name__ == "__main__":
    window = Platformer()
    window.setup()
    window.run()