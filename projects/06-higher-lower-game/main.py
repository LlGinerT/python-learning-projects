from art import logo, vs
from game_data import data as dt
import random


def follower_comparer(obj1, obj2, answer):
    if obj1["follower_count"] > obj2["follower_count"]:
        return answer.lower() == "a"
    else:
        return answer.lower() == "b"


def format_obj(obj):
    return f"{obj["name"]}, {obj["description"]}, from {obj["country"]}"


def main():
    score = 0
    obj2 = random.choice(dt)
    while True:
        obj1 = obj2
        obj2 = random.choice(dt)
        while obj1["name"] == obj2["name"]:
            obj2 = random.choice(dt)
        print(logo)
        print(f"You're current score: {score}")
        print(f"Compare A: {format_obj(obj1)}")
        print(vs)
        print(f"Against B: {format_obj(obj2)}")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        print("\n" * 20)
        if follower_comparer(obj1, obj2, guess):
            score += 1
        else:
            break
    print(logo)
    print(f"Game ends\nFinal score: {score}")
    restart = input("Do you want another game? Type 'y' for continue or 'n' for end. ")
    if restart.lower() == "y":
        main()


main()
