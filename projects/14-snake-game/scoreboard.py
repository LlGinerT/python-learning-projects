from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
GAMEOVER_FONT = ("Courier", 35, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x=0, y=270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear
        self.teleport(x=0, y=0)
        self.color("red")
        self.write(
            arg=f"GAME OVER\nSCORE: {self.score}", align=ALIGNMENT, font=GAMEOVER_FONT
        )
