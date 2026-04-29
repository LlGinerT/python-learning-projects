from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position, shape="square"):
        super().__init__(shape)
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.setheading(90)
        self.shapesize(1, 5)
        self.reset(starting_position)

    def reset(self, starting_position):
        self.goto(starting_position)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
