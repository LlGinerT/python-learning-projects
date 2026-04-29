from turtle import Turtle, Screen

turtle = Turtle()
sc = Screen()
for n in range(4):
    turtle.forward(100)
    turtle.right(90)

sc.exitonclick()
