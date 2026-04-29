import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
TOP_LIMIT = HEIGHT / 2 - 20
BOTTOM_LIMIT = (HEIGHT * -1) / 2 + 20

sc = Screen()
sc.setup(width=WIDTH, height=HEIGHT)
sc.bgcolor("black")
sc.title("PONG by Luis G.")
sc.tracer(0)

p_l = Paddle((-350, 0))
p_r = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

sc.listen()
sc.onkeypress(p_l.move_up, "w")
sc.onkeypress(p_l.move_down, "s")
sc.onkeypress(p_r.move_up, "Up")
sc.onkeypress(p_r.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    if ball.ycor() > TOP_LIMIT or ball.ycor() < BOTTOM_LIMIT:
        ball.bounce_y()

    if ball.xcor() > WIDTH / 2:
        ball.reset()
        ball.bounce_x()
        score.increase_l_score()

    if ball.xcor() < WIDTH / 2 * -1:
        ball.reset()
        ball.bounce_x()
        score.increase_r_score()

    if (
        ball.xcor() > 320
        and ball.distance(p_r) < 50
        or ball.xcor() < -320
        and ball.distance(p_l) < 50
    ):
        ball.bounce_x()


sc.exitonclick()
