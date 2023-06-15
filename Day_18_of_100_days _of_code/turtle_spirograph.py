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


direction = []
# t_colors = ['green', 'crimson', 'purple', 'lawn green', 'cyan', 'navy', 'light salmon', 'dark violet']
for i in range(1, 360):
    direction.append(i)

movement = 0
max_movement = 70

    # walker.color(random.choice(t_colors))
while movement <= max_movement:
    walker.color(full_random_color())
    # walker.pensize(5)
    walker.speed(0)
    walker.circle(100)
    # walker.setheading(random.choice(direction))
    walker.right(10)
    movement += 1
# print(direction)
t.exitonclick()
