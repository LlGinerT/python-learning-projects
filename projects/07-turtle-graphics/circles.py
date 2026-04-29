import turtle as tu
from random import choice, randint

t = tu.Turtle()
sc = tu.Screen()
t.speed(0)
tu.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for n in range(0, 360, 5):
    t.setheading(n)
    t.color(random_color())
    t.circle(100)

sc.exitonclick()
