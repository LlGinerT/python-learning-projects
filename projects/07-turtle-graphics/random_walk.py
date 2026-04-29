import turtle as tu
from random import choice, randint

t = tu.Turtle()
sc = tu.Screen()
t.pensize(10)
t.speed(0)
heading = [0, 90, 180, 270]
tu.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def random_heading():
    t.color(random_color())
    t.seth(choice(heading))
    t.fd(30)


for n in range(300):
    random_heading()

sc.exitonclick()
