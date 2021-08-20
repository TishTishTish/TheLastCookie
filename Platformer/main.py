# El Do-Cookie-Rado - Platform Game
# A part of 'The Last Cookie' gamw
# Created by Ahartisha Selakanabarajah

import arcade
import pathlib

# Screen Dimension Constants
SCREEN_WIDTH = 648
SCREEN_HEIGHT = 468
SCREEN_TITLE = "El Do-Cookie-Rado | The Last Cookie"

# Scaling Constant
MAP_SCALING = 1.0

# Player Constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256
PLAYER_MOVE_SPEED = 10
PLAYER_JUMP_SPEED = 20

# Path to the assets folder
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "Platformer" / "assets"
# print(ASSETS_PATH)

# Class that runs the entire game
class Platformer(arcade.Window):
    # Initialise game object
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # The sprites in the game
        self.cookies = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        
        # Player Sprite
        self.player = None
        
        # Physics Engine
        self.physics_engine = None
        
        # Score
        self.score = 0
        
        # Level
        self.level = 1
        
        # Sounds
        # self.cookie_sound = arcade.load_sound(str(ASSETS_PATH / "audio" / "sounds" / "select.mp3"))
        # self.jump_sound = arcade.load_sound(str(ASSETS_PATH / "audio" / "sounds" / "jump.mp3"))
    
    # Set Up game
    def setup(self) -> None:
        # Get current map for this particular level
        map_name = f"platform_level_{self.level:02}.tmx"
        map_path = ASSETS_PATH / map_name
        
        # Name of the layers
        ground_layer = "ground"
        cookie_layer = "cookies"
        goal_layer = "goal"
        background_layer = "background"
        ladders_layer = "ladders"
        
        # Load current map
        game_map = arcade.tilemap.read_tmx(str(map_path))
        
        # Load layers
        self.background = arcade.tilemap.process_layer(game_map, layer_name=background_layer, scaling = MAP_SCALING)
        self.goals = arcade.tilemap.process_layer(game_map, layer_name=goal_layer, scaling = MAP_SCALING)
        self.ground = arcade.tilemap.process_layer(game_map, layer_name=ground_layer, scaling = MAP_SCALING)
        self.ladders = arcade.tilemap.process_layer(game_map, layer_name=ladders_layer, scaling = MAP_SCALING)
        self.cookies = arcade.tilemap.process_layer(game_map, layer_name=cookie_layer, scaling = MAP_SCALING)
        
        # Set background colour
        background_colour = arcade.color.FRESH_AIR
        if game_map.background_color:
            background_colour = game_map.background_color
        arcade.set_background_color(background_colour)

        # If not already set up, create the player sprite
        if not self.player:
            self.player = self.create_player_sprite()
        
        # Move player sprite back to the beginning (x, y) coordinates
        self.player.centre_x = PLAYER_START_X
        self.player.centre_y = PLAYER_START_Y
        self.player.change_x = 0
        self.player.change_y = 0
        
        # Load up the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player,
            platforms=self.walls,
            gravity_constant=GRAVITY,
            ladders=self.ladders,
        )
    
    def create_player_sprite(self) -> arcade.AnimatedWalkingSprite:
        # Create Player Sprite
        
        # Location of Player Sprites
        texture_path = ASSETS_PATH / "images" / "player"
        
        # Set up textures
        walking_paths = [texture_path / f"walking_to_right{x}.png" for x in (1, 2)]
        climbing_paths = [texture_path / f"climbing_{x}.png" for x in (1, 2)]
        standing_path = texture_path / "standing_l.png"
        
        # Load all the textures
        walking_right_textures = [arcade.load_texture(texture) for texture in walking_paths]
        walking_left_textures = [arcade.load_texture(texture, mirrored=True) for texture in walking_paths]
        walking_up_textures = [arcade.load_texture(texture) for texture in climbing_paths]
        walking_down_textures = [arcade.load_texture(texture) for texture in climbing_paths]
        standing_right_textures = [arcade.load_texture(standing_path)]
        standing_left_textures = [arcade.load_texture(standing_path, mirrored=True)]
        
        # Create Sprite
        player = arcade.AnimatedWalkingSprite()
        
        # Add Textures
        player.stand_left_textures = standing_left_textures
        player.stand_right_textures = standing_right_textures
        player.walk_left_textures = walking_left_textures
        player.walk_right_textures = walking_right_textures
        player.walk_up_textures = walking_up_textures
        player.walk_down_textures = walking_down_textures
        
        # Set up the player defaults
        player.centre_x = PLAYER_START_X
        player.centre_y = PLAYER_START_Y
        player.state = arcade.FACE_RIGHT
        
        # Set up initial texture 
        player.texture = player.stand_right_textures[0]
        
        return player
    
    # Process key presses
    def on_key_press(self, key: int, modifiers: int) -> None:
        # Left/right movement
        if key in [arcade.key.LEFT, arcade.key.J]:
            self.player.change_x = -PLAYER_MOVE_SPEED
        elif key in [arcade.key.RIGHT, arcade.key.L]:
            self.player.change_x = PLAYER_MOVE_SPEED

        # Climb up or down
        elif key in [arcade.key.UP, arcade.key.I]:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = PLAYER_MOVE_SPEED
        elif key in [arcade.key.DOWN, arcade.key.K]:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = -PLAYER_MOVE_SPEED

        # Check if we can jump
        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
                # Play the jump sound
                arcade.play_sound(self.jump_sound)
    
    # Process key releases
    def on_key_release(self, key: int, modifiers: int):
        # Check for player left/right movement
        if key in [
            arcade.key.LEFT,
            arcade.key.J,
            arcade.key.RIGHT,
            arcade.key.L,
        ]:
            self.player.change_x = 0

        # Check if player can climb up or down
        elif key in [
            arcade.key.UP,
            arcade.key.I,
            arcade.key.DOWN,
            arcade.key.K,
        ]:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = 0
    
    # Update the state of the game and all the objects in it
    def on_update(self, delta_time: float) -> None:
        # Update the player animation
        self.player.update_animation(delta_time)
        
        # Update player movement based on the physics engine
        # self.physics_engine.update()
        
        # Restrict player movement
        if self.player.left < 0:
            self.player.left = 0
            
        # Check if a cookie is collected
        cookies_hit = arcade.check_for_collision_with_list(
            sprite=self.player, sprite_list=self.cookies
        )
        
        for cookie in cookies_hit:
            # Add cookie score to our score
            self.score += int(cookie.properties["point_value"])
            
            # Play the cookie sound
            arcade.play_sound(self.cookie_sound)
            
            # Remove the cookie
            cookie.remove_from_sprite_lists()
            
        # Check for ending goal i.e. the door
        goals_hit = arcade.check_for_collision_with_list(
            sprite=self.player, sprite_list=self.goals
        )
        
        if goals_hit:
            # Play victory sound
            # self.victory_sound.play()
            
            # Setup the next level
            self.level += 1
            self.setup()
    
    def on_draw(self) -> None:
        arcade.start_render()
        
        # Draw all sprites
        self.background.draw()
        self.ground.draw()
        self.cookies.draw()
        self.goals.draw()
        self.ladders.draw()
        self.player.draw()

if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()
    print("You found El Do-Cookie-Rado!")