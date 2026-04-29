from turtle import Turtle, Screen

t = Turtle()
sc = Screen()

for n in range(50):
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()

sc.exitonclick()
