from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.teleport(x, y)
