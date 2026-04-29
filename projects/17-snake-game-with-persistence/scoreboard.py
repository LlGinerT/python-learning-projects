from pathlib import Path
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
GAMEOVER_FONT = ("Courier", 35, "normal")
DATA_PATH = Path(__file__).parent / "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open(DATA_PATH) as data:
            self.high_score = int(data.read())
        self.teleport(x=0, y=270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_PATH, "w") as dt:
                dt.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # Replaced for store high_score
    """ def game_over(self):
        self.clear
        self.teleport(x=0, y=0)
        self.color("red")
        self.write(
            arg=f"GAME OVER\nSCORE: {self.score}", align=ALIGNMENT, font=GAMEOVER_FONT
        )
"""
