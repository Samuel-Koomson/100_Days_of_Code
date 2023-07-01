from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(.5, .5)
        self.color('green')
        self.speed(0)
        self.new_food()

    def new_food(self):
            x_position = random.randint(-280, 280)
            y_position = random.randint(-280, 280)
            self.goto(x_position, y_position)
