from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('purple')
screen.title("The infamous snake game, now created by Sammy Koomson")
screen.tracer(0)

snake_position = [(0, 0), (-20, 0), (-40, 0)]

babe_snake = []

for snake in snake_position:
    new_snake = Turtle(shape='square')
    new_snake.penup()
    new_snake.goto(snake)
    babe_snake.append(new_snake)

# screen.update()


game_play = True
while game_play:
    screen.update()
    time.sleep(.2)
    for moving_snake in range(len(babe_snake)-1, 0, -1):
        x_position = babe_snake[moving_snake - 1].xcor()
        y_position = babe_snake[moving_snake - 1].ycor()
        babe_snake[moving_snake].goto(x_position, y_position)
    babe_snake[0].forward(20)
    #     each_snake.forward(20)
    #     # screen.update()
    #     # time.sleep(1)
    #
    # babe_snake[0].left(90)


screen.exitonclick()