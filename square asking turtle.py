import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput(" ", "Enter the number of sides: ")
n = int(s)

l = turtle.textinput(" ", "Enter the length of each side: ")
l = int(l)
for i in range(n):
    t.forward(l)
    t.left(360/n)
