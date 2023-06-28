import turtle
from turtle import Turtle, Screen

tommy = Turtle()
screen = Screen()

def go_ahead():
    tommy.forward(40)

def back():
    tommy.back(40)

def right_turn():
    tommy.right(10)

def left_turn():
    tommy.left(10)

def clear_screen():
    tommy.clear()
    tommy.home()

screen.listen()

screen.onkey(go_ahead, 'w')
screen.onkey(back, 's')
screen.onkey(right_turn, 'e')
screen.onkey(left_turn, 'f')
screen.onkey(clear_screen, 'c')

turtle.exitonclick()
