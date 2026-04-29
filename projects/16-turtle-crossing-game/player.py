from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape="turtle"):
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.reset()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reset()
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)
