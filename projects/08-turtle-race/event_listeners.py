import turtle as tu

t = tu.Turtle()
sc = tu.Screen()


def move_forwards():
    t.forward(5)


def move_backwards():
    t.backward(5)


def turn_right():
    t.right(2)


def turn_left():
    t.left(2)


def reset():
    tu.resetscreen()


sc.onkeypress(fun=move_forwards, key="w")
sc.onkeypress(fun=move_backwards, key="s")
sc.onkeypress(fun=turn_right, key="d")
sc.onkeypress(fun=turn_left, key="a")
sc.onkey(fun=reset, key="c")
sc.listen()
sc.exitonclick()
