import turtle as t
import random

t.colormode(255)
paint_brush = t.Turtle()
paint_brush.speed(0)
paint_brush. penup()

ready_paint = [(225, 228, 234), (244, 238, 224), (241, 233, 239), (234, 243, 238), (189, 166, 118), (141, 166, 186), (136, 93, 55), (60, 101, 134), (12, 22, 50), (56, 19, 10), (219, 205, 128), (179, 153, 47), (179, 147, 165), (143, 175, 152), (75, 115, 81), (53, 16, 25), (123, 82, 102), (15, 39, 25), (126, 32, 20), (26, 54, 123), (179, 188, 211), (160, 107, 135), (101, 149, 101), (97, 124, 171), (108, 36, 52), (207, 180, 198), (31, 85, 58), (172, 106, 97), (79, 148, 162), (175, 204, 182), (85, 76, 23), (167, 201, 208), (215, 181, 175), (23, 81, 92), (230, 204, 15)]

paint_brush.setheading(225)
paint_brush.forward(250)
paint_brush.setheading(0)
movement = 300

for i in range(1, movement + 1):
    paint_brush.dot(15, random.choice(ready_paint))
    paint_brush.setheading(0)
    paint_brush.forward(20)

    if i % 15 == 0:
        paint_brush.setheading(90)
        paint_brush.forward(20)
        paint_brush.setheading(180)
        paint_brush.forward(300)
        paint_brush.setheading(0)


t.exitonclick()