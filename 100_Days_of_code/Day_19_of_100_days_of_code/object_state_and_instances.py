import random
import turtle
import turtle as t
# import tTurtle, t.Screen

start_race = False
screen = t.Screen()
screen.setup(width=500, height=500)
bet = screen.textinput(title="lottery", prompt="which of the options do you prefer: nla ")
print(bet)
start_point = [-200, 200, 0, 100, -100]
tommy_colors = ['red', 'green', 'blue', 'purple', 'yellow']
lineup_turtle = []

for tom in range(0, 5):

    tommy = t.Turtle(shape='turtle')
    tommy.color(tommy_colors[tom])
    tommy.penup()
    tommy.goto(x=-220, y=start_point[tom])
    lineup_turtle.append(tommy)

if bet:
    start_race = True
while start_race:

    for race_turtle in lineup_turtle:
        if race_turtle.xcor() > 220:
            start_race = False
            winning_turtle = race_turtle.pencolor()
            if winning_turtle == bet:
                print(f"Congratulations, you bet on {winning_turtle} and you won")
            else:
                print(f"sorry you lost, the winning turtle is {winning_turtle}")
        movement = random.randint(0, 15)
        race_turtle.forward(movement)

""" from line 5 to 36 provides the efficient way to implement this program while line 40 to 64 uses the hard coding approach"""

# kofi = t.Turtle('turtle')
# kofi.color('red')
# kofi.penup()
# kofi.goto(x=-220, y=-100)
#

# yaw = t.Turtle('turtle')
# yaw.color('purple')
# yaw.penup()
# yaw.goto(x=-220, y=100)
#
# kwame = t.Turtle('turtle')
# kwame.color('green')
# kwame.penup()
# kwame.goto(x=-220, y=-0)
#
# senanu = t.Turtle('turtle')
# senanu.color('yellow')
# senanu.penup()
# senanu.goto(x=-220, y=-200)
#
# wizzy = t.Turtle('turtle')
# wizzy.color('blue')
# wizzy.penup()
# wizzy.goto(x=-220, y=200)

t.exitonclick()