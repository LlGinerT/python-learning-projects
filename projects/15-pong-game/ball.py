from random import randint
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, shape="circle"):
        super().__init__(shape)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = randint(5, 10)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset(self):
        self.goto(0, 0)
        new_x_move = 10 * (self.x_move / abs(self.x_move))
        new_y_move = randint(5, 10) * (self.y_move / abs(self.y_move))
        self.x_move = new_x_move
        self.y_move = new_y_move
        self.move_speed = 0.1
