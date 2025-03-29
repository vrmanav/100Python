# Rock Paper Scissors game

import random

symbols = [
    "Rock",
    "Paper",
    "Scissors",
]
print("Welcome to Rock-Paper-Scissors game\n")
print("0: Rock")
print("1: Paper")
print("2: Scissors")
user_choice = int(input("What do you choose:\n"))
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice > 2:
    print("\nYou have passed an invalid number. Game Over 💀")
else:
    print(f"\nYou chose {symbols[user_choice]}")
    print(f"\nComputer chose {symbols[computer_choice]}")
    if user_choice == computer_choice:
        print("\nIt is a draw ⛔️")
    elif user_choice == 0 and computer_choice == 2:
        print("\nYou win 🎉")
    elif computer_choice == 0 and user_choice == 2:
        print("\nComputer wins, better luck next time 😕")
    elif user_choice < computer_choice:
        print("\nComputer wins, better luck next time 😕")
    elif computer_choice < user_choice:
        print("\nYou win 🎉")
