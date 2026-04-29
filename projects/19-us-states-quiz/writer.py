from turtle import Turtle as t


class Writer(t):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def display_state(self, state, x, y):
        self.goto(x, y)
        self.write(state)
