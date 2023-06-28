import turtle as t

dashed_t = t.Turtle('turtle')
dashed_t.color('green')
for i in range(15):
    dashed_t.forward(10)
    dashed_t.pendown()
    dashed_t.forward(10)
    dashed_t.penup()
t.exitonclick()