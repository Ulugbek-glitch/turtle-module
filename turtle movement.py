import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(3):
    t.forward(100)
    t.left(360/3)

t.penup()
t.goto(200,0)
t.pendown()

for i in range(6):
    t.forward(100)
    t.left(360/6)
