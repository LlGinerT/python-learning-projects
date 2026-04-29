from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

TOP_LIMIT = 285
BOTTOM_LIMIT = -285
RIGHT_LIMIT = 290
LEFT_LIMIT = -295

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.spawn()
        scoreboard.increase_score()
        snake.extend()

    if (
        snake.head.xcor() > RIGHT_LIMIT
        or snake.head.ycor() > TOP_LIMIT
        or snake.head.xcor() < LEFT_LIMIT
        or snake.head.ycor() < BOTTOM_LIMIT
    ):
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


sc.exitonclick()
