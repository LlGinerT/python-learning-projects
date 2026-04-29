from turtle import Turtle


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape="classic", visible=False):
        super().__init__(shape, visible)
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
