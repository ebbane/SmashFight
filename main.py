
import arcade
from constants import * 
import os


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.playerOne = None
        self.playerTwo = None
        self.physics_engine = None
        # self.life = 3 
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Draw the floor
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/stoneCorner_right.png", SPRITE_SCALING)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)

        # Draw the platform
        for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/stoneHalf_mid.png", SPRITE_SCALING)
            # wall = arcade.draw_rectangle_filled(300, 10, 600, 50, arcade.color.BLUSH)
            wall.bottom = SPRITE_SIZE * 3
            wall.left = 950
            self.wall_list.append(wall)

        # Draw the platform
        for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/stoneHalf_mid.png", SPRITE_SCALING)
            # wall = arcade.draw_rectangle_filled(300, 10, 600, 50, arcade.color.BLUSH)
            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        # -- Set up the player 1
        self.playerOne = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", SPRITE_SCALING)
        self.player_list.append(self.playerOne)

        # Starting position of the first player
        self.playerOne.center_x = 200
        self.playerOne.center_y = 90

        # -- Set up the player 2
        self.playerTwo = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", SPRITE_SCALING)
        self.player_list.append(self.playerTwo)

        # Starting position of the second player
        self.playerTwo.center_x = 1000
        self.playerTwo.center_y = 90


        self.physics_engine = arcade.PhysicsEnginePlatformer(self.playerOne,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.ALMOND)         
        self.background = arcade.load_texture("images/backgrounds/map.png")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw background
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


        # Draw all the sprites.
        self.player_list.draw()
        self.wall_list.draw()

    def on_key_press(self, key, modifiers):
        
        # For the first player
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.playerOne.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.playerOne.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.playerOne.change_x = MOVEMENT_SPEED
        
        # # For the second player
        # if key == arcade.key.Z:
        #     if self.physics_engine.can_jump():
        #         self.playerOne.change_y = JUMP_SPEED
        # elif key == arcade.Q.LEFT:
        #     self.playerOne.change_x = -MOVEMENT_SPEED
        # elif key == arcade.key.S:
        #     self.playerOne.change_x = MOVEMENT_SPEED



    def on_key_release(self, key, modifiers):
       
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.playerOne.change_x = 0
            self.playerTwo.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the player based on the physics engine
        if not self.game_over:

            # Update the player using the physics engine
            self.physics_engine.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()