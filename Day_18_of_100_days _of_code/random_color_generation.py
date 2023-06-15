import turtle as t
import random

walker = t.Turtle()
t.colormode(255)

def full_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    full_random_color = (red, green, blue)
    return full_random_color


direction = [0, 90, 180, 270]
# direction = direction1
# t_colors = ['green', 'crimson', 'purple', 'lawn green', 'cyan', 'navy', 'light salmon', 'dark violet']
for i in range(800):

    # direction += random.choice(direction1)
    # direction.right(random.choice(direction1))
    # walker.color(random.choice(t_colors))
    walker.color(full_random_color())
    walker.pensize(5)
    walker.speed(3)
    walker.forward(20)
    walker.setheading(random.choice(direction))
    # walker.forward(20)
print(direction)
t.exitonclick()
