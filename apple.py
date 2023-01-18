import arcade
import random

class Apple(arcade.Sprite):
    def __init__ (self, Game):
        super().__init__("Assignment 15/tamrin/pngfind.com-apple-icon-png-56881.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, Game.width - 10)
        self.center_y = random.randint(10, Game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Rock(Apple):
    def __init__(self,Game):
        super().__init__("my-project\session15\pear.png")

class Pear(Apple):
    def __init__(self,Game):
        super().__init__("my-project\session15\pear.png")
