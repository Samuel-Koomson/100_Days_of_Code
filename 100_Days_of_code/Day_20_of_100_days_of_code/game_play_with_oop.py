from turtle import Screen, Turtle
import time
from snake_oop import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('purple')
screen.title("The infamous snake game, now created by Sammy Koomson")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_play = True
while game_play:
    snake.snake_move()
    screen.update()
    time.sleep(.2)