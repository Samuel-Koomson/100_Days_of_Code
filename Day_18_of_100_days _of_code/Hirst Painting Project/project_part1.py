import colorgram
import turtle as t
import random

t.colormode(255)

rgb_paint = []
paints = colorgram.extract("Hirstpainting.jpg", 50)
for paint in paints:
    r = paint.rgb.r
    g = paint.rgb.g
    b = paint.rgb.b
    new_paints = (r, g, b)
    rgb_paint.append(new_paints)

print(rgb_paint)

t.exitonclick()