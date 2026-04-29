from turtle import Turtle, Screen
import random

sc = Screen()
colors = ["red", "orange", "black", "green", "blue", "purple"]
sc.setup(width=500, height=400)
y = 70
turtles = []
race_on = False


def race(bet):
    global race_on
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            if turtle.pencolor() == bet:
                print(f"You win! {turtle.pencolor().title()} turtle is the winner.")
            else:
                print(f"You lose! {turtle.pencolor().title()} turtle is the winner.")
            break
        turtle.forward(random.randint(0, 10))


for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-240, y=y)
    turtles.append(t)
    t.pendown()
    y -= 30

user_bet = sc.textinput(
    title="Make you bet", prompt="Which turtle will win the race? Enter a color: "
)
if user_bet:
    race_on = True

while race_on:
    race(user_bet)
sc.exitonclick()
