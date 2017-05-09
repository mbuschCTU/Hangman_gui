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
        self.target_word = self.target_word.rstrip().upper()
        # self.target_word = 'APPLE'
        print('Target word =  ', self.target_word)
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
        self.win = False
        self.lose = False
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

        # self.word.used_letters = ['A','S','F']
        # Draw the text
        arcade.draw_text('Used Letters',
                         SCREEN_WIDTH //2, SCREEN_HEIGHT - 50, arcade.color.BLACK, 36)
        arcade.draw_text(' '.join(self.word.used_letters), SCREEN_WIDTH//2, SCREEN_HEIGHT - 85,
                         arcade.color.BRIGHT_MAROON, 24)

        arcade.draw_text('Target Word',
                         10, SCREEN_HEIGHT // 3 + 75, arcade.color.BLACK, 36)

        arcade.draw_text(' '.join(self.word.guess_word),
                         10, SCREEN_HEIGHT // 3, arcade.color.BLUE,36)

        if self.win:
            arcade.draw_text('Winner!',
                             200, 50, arcade.color.YELLOW_ORANGE, 72)
        if self.lose:
            arcade.draw_text('Loser!',
                             200, 50, arcade.color.RED_DEVIL, 72)

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
        if key in range(arcade.key.A, arcade.key.Z + 1) and not (self.win or self.lose):
            letter = chr(key).upper()
            index_list = handle_input(letter, self.word.target_word, self.word.used_letters)
            if letter not in self.word.used_letters:
                if len(index_list) > 0:
                    for index in index_list:
                        self.word.guess_word[index] = letter
                elif len(index_list) == 0:
                    self.current_sprite += 1
                    self.word.used_letters.append(chr(key).upper())

        # Check for win or loss
            self.win = self.word.guess_word.count('_') == 0
            self.lose = self.current_sprite == len(self.all_sprites_list) - 1

# ------------------------------------------------#

def handle_input(letter, target, used):
    """
    Find all indeces of letter in target
    :param letter: User input guess 
    :param target: Target word user is guessing
    :param used: List of letters already guessed
    :return: list of letter positions or empty list
    """
    if letter not in used and letter in target:
        return [i for i,x in enumerate(target) if x == letter ]
    return []


if __name__ == '__main__':
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()