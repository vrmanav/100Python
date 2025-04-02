from art import logo, stages
import random
from os import system
from time import sleep

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
lives_remaining = 6
chosen_word = random.choice(word_list)
#  Make blank spaces equal to the number of alphabets in the chosen word
blanks = []
for _ in chosen_word:
    blanks.append(" _ ")

print(logo)
sleep(1.5)
continue_game = True
while continue_game:
    system("clear")
    print(stages[lives_remaining])
    print("".join(blanks))
    # print(f"HINT: {chosen_word}")
    # Ask user for input
    user_guess = input("\nMake your guess: ")
    # Check user's guess
    for index in range(len(chosen_word)):
        if user_guess == chosen_word[index]:
            blanks[index] = user_guess

    if user_guess in chosen_word:
        print("Great! your guess is correct 🎉")
    else:
        print("You have made an incorrect guess. You lose a life 😕")
        lives_remaining -= 1

    if lives_remaining == 0:
        print("\nYou have exhausted all your lives. Game over 💀")
        continue_game = False
    sleep(1.5)
