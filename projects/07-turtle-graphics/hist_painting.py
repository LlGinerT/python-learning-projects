import turtle as tu
from random import randint

t = tu.Turtle()
sc = tu.Screen()
tu.colormode(255)
t.hideturtle()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for y in range(-200, 300, 50):
    for x in range(-250, 250, 50):
        t.teleport(x, y)
        t.dot(20, random_color())
        print(t.pos())


sc.exitonclick()
