from random import randint
from art import logo

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def set_difficulty():
    while True:
        try:
            choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
            if choice == "easy":
                return EASY_DIFFICULTY
            elif choice == "hard":
                return HARD_DIFFICULTY
            else:
                raise ValueError("No valid choice")
        except ValueError as ve:
            print(ve)


def check_answer(user_guess, answer, attempts):
    """Compare the user guess with the answer, and update attempts remaining"""
    if user_guess > answer:
        print("Too high.")
        return attempts - 1
    elif user_guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")


def main():
    print(logo)
    print("I'm thinking a number between 1 to 100. Try to guess")
    answer = randint(1, 100)
    attempts = set_difficulty()
    guess = 0
    while guess != answer and attempts > 0:
        guess = int(input("Make a guess: "))
        attempts = check_answer(user_guess=guess, answer=answer, attempts=attempts)
        print(f"You have {attempts} attempts remaining.")
    if attempts == 0:
        print(f"You lose. The correct answer was {answer}.")


main()
