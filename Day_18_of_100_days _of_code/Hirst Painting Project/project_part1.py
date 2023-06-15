import colorgram
import turtle as t
import random

rgb_paint = []
paints = colorgram.extract("Hirstpainting.jpg", 50)
for paint in paints:
    r = paint.rgb.r
    g = paint.rgb.g
    b = paint.rgb.b
    new_paints = (r, g, b)
    rgb_paint.append(new_paints)

print(rgb_paint)

# paint_brush = t.Turtle()
# ready_paint = [(225, 228, 234), (244, 238, 224), (241, 233, 239), (234, 243, 238), (189, 166, 118), (141, 166, 186), (136, 93, 55), (60, 101, 134), (12, 22, 50), (56, 19, 10), (219, 205, 128), (179, 153, 47), (179, 147, 165), (143, 175, 152), (75, 115, 81), (53, 16, 25), (123, 82, 102), (15, 39, 25), (126, 32, 20), (26, 54, 123), (179, 188, 211), (160, 107, 135), (101, 149, 101), (97, 124, 171), (108, 36, 52), (207, 180, 198), (31, 85, 58), (172, 106, 97), (79, 148, 162), (175, 204, 182), (85, 76, 23), (167, 201, 208), (215, 181, 175), (23, 81, 92), (230, 204, 15)]
#
# for paint in range(1, 100):
#     paint_brush.dot(3, random.choice(ready_paint))
#     paint_brush.forward(20)

t.exitonclick()