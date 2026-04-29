from random import choice, randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.setx(290)
            new_car.sety(randint(-230, 250))
            new_car.resizemode("user")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_speed
            car.setx(new_x)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
