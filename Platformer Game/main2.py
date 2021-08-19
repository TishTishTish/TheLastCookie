# El Do-Cookie-Rado - Platform Game
# A part of 'The Last Cookie' gamw
# Created by Ahartisha Selakanabarajah

import arcade
from pyglet import window

class Platformer(arcade.Window):
    def __init__(self):
        pass
    
    # Set Up game
    def setup(self):
        pass
    
    def on_key_press(self, symbol: int, modifiers: int):
        # return super().on_key_press(symbol, modifiers)
        pass
    
    def on_key_release(self, symbol: int, modifiers: int):
        # return super().on_key_release(symbol, modifiers)
        pass
    
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