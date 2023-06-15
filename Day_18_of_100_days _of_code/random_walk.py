import turtle as t
import random

walker = t.Turtle()
direction = [0, 90, 180, 270]

# direction = direction1
t_colors = ['green', 'crimson', 'purple', 'lawn green', 'cyan', 'navy', 'light salmon', 'dark violet']
for i in range(800):

    # direction += random.choice(direction1)
    # direction.right(random.choice(direction1))
    walker.color(random.choice(t_colors))
    walker.pensize(5)
    walker.speed(3)
    walker.forward(20)
    walker.setheading(random.choice(direction))
    # walker.forward(20)
print(direction)
t.exitonclick()

