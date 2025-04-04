# Number guessing game

import random
import art
import os
import time

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_turns():
    difficulty = input("\nChoose your difficulty [EASY / HARD]: ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


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

    print(f"HINT: {number}")
    turns = set_turns()
    number_not_guessed = True
    while turns > 0 and number_not_guessed:
        print(f"\nYou have {turns} turns remaining")
        guess = int(input("Make your guess: "))
        if guess == number:
            print("\nThat's correct! You have guessed the number 🎉")
            number_not_guessed = False
            return
        elif guess < number:
            print("That is too low 🔽")
            turns -= 1
        elif guess > number:
            print("That is too high 🔼")
            turns -= 1

    os.system("clear")
    print("\nYou have exhausted all your turns. Game over 💀")
    print(f"The number was {number}")


number_guessing()
