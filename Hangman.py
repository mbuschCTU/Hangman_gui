"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

A walk-through of this code is available at:
https://vimeo.com/168051968
"""
import arcade
from random import choice
import string
# import attr

SPRITE_SCALING = 1.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_WIDTH = 163 * SPRITE_SCALING
SPRITE_HEIGHT = 152 * SPRITE_SCALING
# BALL_RADIUS = 20

class Hangman(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

#------------------------------------------------#
# @attr.s
class Word(object):
    """ 
    Class responsible for selecting target word, drawing blanks,
    drawing correct guesses, drawing wrong guesses.
    """

    #------------------------------------------------#

    def __init__(self, fname='wordlist.txt'):
        """Constructor for Word"""
        with open(fname,'r') as infile:
            self.target_word = choice(list(infile))
        self.target_word = self.target_word.rstrip()
        self.target_length = len(self.target_word)
        self.guess_word = ['_'] * self.target_length
        self.used_letters = []


class MyApplication(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        # self.ball_x_position = BALL_RADIUS
        # self.ball_x_pixels_per_second = 70

        arcade.set_background_color(arcade.color.WHITE)
        self.current_sprite = 0
        self.word = Word()
        self.all_sprites_list = arcade.SpriteList()
        for i in range(0,9):
            self.player_sprite = Hangman("Hangman"+str(i)+".png", SPRITE_SCALING)
            self.player_sprite.center_x = (SPRITE_WIDTH // 2 + 1)
            self.player_sprite.center_y = SCREEN_HEIGHT - (SPRITE_HEIGHT // 2 + 1)
            self.all_sprites_list.append(self.player_sprite)
        print('Setup done.')

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Draw the circle
        # arcade.draw_circle_filled(self.ball_x_position, SCREEN_HEIGHT // 2,
        #                           BALL_RADIUS, arcade.color.GREEN)

        # Draw Hangman sprite
        self.all_sprites_list[self.current_sprite].draw()


        # Draw the text
        arcade.draw_text('Used Letters',
                         SCREEN_WIDTH //2, SCREEN_HEIGHT - 50, arcade.color.BLACK, 36)

        arcade.draw_text('Target Word',
                         10, SCREEN_HEIGHT // 3 + 75, arcade.color.BLACK, 36)

        arcade.draw_text(' '.join(self.word.guess_word),
                         10, SCREEN_HEIGHT // 3, arcade.color.BLACK,36)

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        # self.ball_x_position += self.ball_x_pixels_per_second * delta_time
        #
        # # Did the ball hit the right side of the screen while moving right?
        # if self.ball_x_position > SCREEN_WIDTH - BALL_RADIUS \
        #         and self.ball_x_pixels_per_second > 0:
        #     self.ball_x_pixels_per_second *= -1
        #
        # # Did the ball hit the left side of the screen while moving left?
        # if self.ball_x_position < BALL_RADIUS \
        #         and self.ball_x_pixels_per_second < 0:
        #     self.ball_x_pixels_per_second *= -1

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)

        #Check for actual alphabet key
        if key in range(arcade.key.A, arcade.key.Z):
            self.word.used_letters.append(chr(key).upper())
            print("you pressed ", chr(key).upper())


        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            print("You pressed the space bar.")

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()