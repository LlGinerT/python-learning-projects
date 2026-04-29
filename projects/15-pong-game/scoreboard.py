from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 35, "normal")
# GAMEOVER_FONT = ("Courier", 35, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x=0, y=250)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.show_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(arg=f"{self.l_score}:{self.r_score}", align=ALIGNMENT, font=FONT)
