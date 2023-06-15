import turtle as t
import random
new_turtle = t.Turtle()
new_turtle.shape('turtle')
#
# for i in range(3):
#     new_turtle.forward(30)
#     new_turtle.right(120)
#     new_turtle.forward(30)
#
# for i in range(4):
#     new_turtle.forward(30)
#     new_turtle.right(90)
#     new_turtle.forward(30)
#
# for i in range(5):
#     new_turtle.forward(30)
#     new_turtle.right(72)
#     new_turtle.forward(30)
#
# for i in range(6):
#     new_turtle.forward(30)
#     new_turtle.right(60)
#     new_turtle.forward(30)
#
# for i in range(7):
#     new_turtle.forward(30)
#     new_turtle.right(51)
#     new_turtle.forward(30)
#
# for i in range(8):
#     new_turtle.forward(30)
#     new_turtle.right(45)
#     new_turtle.forward(30)
#
# for i in range(10):
#     new_turtle.forward(30)
#     new_turtle.right(36)
#     new_turtle.forward(30)

#To make the code easy we can just write a function
t_colors = ['green', 'crimson', 'purple', 'lawn green', 'cyan', 'navy', 'light salmon', 'dark violet']
def different_shapes(angle_sizes):
    area_of_circle = 360
    for i in range(angle_sizes):
        angle = area_of_circle/angle_sizes
        new_turtle.forward(30)
        new_turtle.right(angle)
different_shapes(6)

for more_shapes in range(4, 11):
    new_turtle.color(random.choice(t_colors))
    different_shapes(more_shapes)

t.exitonclick()