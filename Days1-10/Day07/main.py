from art import logo, stages
import random
import os
import time

word_list = [
    "hang",
    "clique",
    "launch",
    "initial",
    "attention",
    "professional",
    "drawing",
    "calm",
    "solve",
    "elapse",
]


def play_hangman():
    """Plays the hangman game"""
    lives_remaining = 6
    chosen_word = random.choice(word_list)
    blanks = []
    for _ in chosen_word:
        blanks.append(" _ ")

    os.system("clear")
    print(logo)
    time.sleep(1.5)
    while lives_remaining > 0 and " _ " in blanks:
        os.system("clear")
        print(stages[lives_remaining])
        print("".join(blanks))
        user_guess = input("\nMake your guess: ").lower()

        # Check is user has entered a single character only
        if len(user_guess) != 1:
            print("Please enter a single letter.")
            time.sleep(1.5)
            continue

        # Check if user has already guessed the character previously
        if user_guess in blanks:
            print("You've already guessed that letter.")
            time.sleep(1.5)
            continue

        for index in range(len(chosen_word)):
            if user_guess == chosen_word[index]:
                blanks[index] = user_guess

        if user_guess in chosen_word:
            print("Great! your guess is correct 🎉")
        else:
            print("You have made an incorrect guess. You lose a life 😕")
            lives_remaining -= 1
        time.sleep(1.5)

        os.system("clear")
        if " _ " not in blanks:
            print("Congratulations! You guessed the word!")
        else:
            print(stages[0])
            print("\nYou have exhausted all your lives. Game over 💀")
            print(f"The word was: {chosen_word}")


play_hangman()
