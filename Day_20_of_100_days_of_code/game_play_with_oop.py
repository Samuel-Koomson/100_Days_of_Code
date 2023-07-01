import random
import turtle
from turtle import Screen, Turtle
import time
from snake_oop import Snake
from snake_food import Food
from score_board import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('purple')
screen.title("The infamous snake game, now created by Sammy Koomson")
screen.tracer(0)

snake = Snake()
first_food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_play = True

while game_play:
    screen.update()
    snake.snake_move()
    time.sleep(.1)

    if snake.head.distance(first_food) < 15:
        first_food.new_food()
        snake.increase_length()
        scoreboard.new_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_play = False
        scoreboard.game_over()

turtle.exitonclick()

