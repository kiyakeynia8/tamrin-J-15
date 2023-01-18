import random
import arcade
from apple import Apple,Pear,Rock
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="super_snake -- V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.apple_food = Apple(self)
        self.rock = Rock(self)
        self.pear_food = Pear(self)

        self.a = 1

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple_food.draw()    
        self.rock.draw()
        self.pear_food.draw()
        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.rock) or arcade.check_for_collision(self.snake, self.apple_food) or arcade.check_for_collision(self.snake, self.pear_food):
            if arcade.check_for_collision(self.snake, self.apple_food):
                self.snake.apple_eat(self.apple_food)

            if arcade.check_for_collision(self.snake, self.rock):
                self.snake.rock_eat(self.rock)

            if arcade.check_for_collision(self.snake, self.pear_food):
                self.snake.pear_eat(self.pear_food)

            self.a = random.randint(1, 3)
            if self.a == 1:
                self.apple_food = Apple(self)
            if self.a == 2:
                self.rock = Rock(self)
            if self.a == 3:
                self.pear_food == Pear(self)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        if symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

if __name__ == "__main__":
    game = Game()
    arcade.run()