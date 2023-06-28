from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.babe_snake = []
        self.snake_body()
        self.head = self.babe_snake[0]

    def snake_body(self):
        for snake in SNAKE_POSITION:
            new_snake = Turtle(shape='square')
            new_snake.penup()
            new_snake.goto(snake)
            self.babe_snake.append(new_snake)

    def snake_move(self):
        for moving_snake in range(len(self.babe_snake) - 1, 0, -1):
            x_position = self.babe_snake[moving_snake - 1].xcor()
            y_position = self.babe_snake[moving_snake - 1].ycor()
            self.babe_snake[moving_snake].goto(x_position, y_position)
        self.babe_snake[0].forward(SNAKE_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.babe_snake[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.babe_snake[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.babe_snake[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.babe_snake[0].setheading(RIGHT)
