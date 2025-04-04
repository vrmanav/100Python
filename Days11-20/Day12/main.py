# Number guessing game

import random
import art
import os
import time

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_turns():
    """Sets the difficulty level and returns the number of attempts."""
    while True:
        difficulty = input("Choose your difficulty [EASY / HARD]: ").lower()
        if difficulty == "easy":
            return EASY_LEVEL_TURNS
        elif difficulty == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please enter 'easy' or 'hard'")


def check_guess(guess, number, turns):
    """Checks the user's guess against the secret number and returns the remaining turns."""
    if guess == number:
        print("\nThat's correct! You have guessed the number 🎉")
        return 0
    elif guess < number:
        print("That is too low 🔽")
        return turns - 1
    elif guess > number:
        print("That is too high 🔼")
        return turns - 1


def number_guessing():
    os.system("clear")
    print(art.logo)
    number = random.randint(1, 101)
    print("* I am thinking of a integer number between 1 and 100")
    print("* Your task is to guess that number")
    print("* For easy difficulty, you will be given 10 turns")
    print("* For hard difficulty, you will be given 5 turns")
    time.sleep(3)
    os.system("clear")

    # print(f"HINT: {number}") Uncomment for testing purpose
    turns = set_turns()
    while turns > 0:
        print(f"\nYou have {turns} turns remaining")
        while True:
            try:
                guess = int(input("Make your guess: "))
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        turns = check_guess(guess=guess, number=number, turns=turns)
        time.sleep(0.5)
        if turns == 0 and guess != number:
            os.system("clear")
            print("You have exhausted all your attempts. Game over 💀")
            print(f"The secret number was {number}.")
            return
        elif turns == 0 and guess == number:
            return


number_guessing()
