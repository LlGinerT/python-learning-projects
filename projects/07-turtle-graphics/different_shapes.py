from turtle import Turtle, Screen

t = Turtle()
sc = Screen()
colors = ["red", "blue", "green", "yellow", "orange", "magenta", "navy", "purple"]
sides = 3

for n in range(8):
    t.pencolor(colors[n])
    angle = 360 / sides
    for n in range(sides):
        t.right(angle)
        t.forward(100)
    sides += 1

sc.exitonclick()
