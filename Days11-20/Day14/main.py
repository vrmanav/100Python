# Higher or Lower - Instagram edition
from game_data import data
import random
import art
import time
import os


def check_guess(accountA_followers, accountB_follower, guess):
    """Check the user's guess and compare it account A & B's follower"""
    if accountA_followers > accountB_follower:
        return "a" == guess
    else:
        return "b" == guess


def display_formatted_data(accountA, accountB):
    """Display name, description & country of both accounts"""

    print(
        f"Compare A: {accountA['name']}, a {accountA['description']}, from {accountA['country']}"
    )
    print(art.vs)
    print(
        f"Compare B: {accountB['name']}, a {accountB['description']}, from {accountB['country']}"
    )


def play_higher_lower():
    """Start Higher-Lower game"""

    score = 0
    os.system("clear")
    print(art.logo)
    print("* You will be displayed two Instagram accounts.")
    print("* Your task is to guess which account has more followers")
    time.sleep(3)
    os.system("clear")
    account_B = random.choice(data)
    while True:
        account_A = account_B
        if account_B == account_A:
            account_B = random.choice(data)
            display_formatted_data(account_A, account_B)
            guess = input("\nWho do you think has more followers (A/B): ").lower()
            is_guess_correct = check_guess(
                account_A["follower_count"], account_B["follower_count"], guess
            )
            if is_guess_correct:
                score += 1
                print("\nGreat! you have guessed it correct 🎉")
                print(f"Your current score is {score}. Moving on to the next one ⏭️")
                time.sleep(2)
                os.system("clear")
            else:
                print("\nOops! that's not correct. Game over 💀")
                print(f"Your final score is {score}")
                time.sleep(2)
                return


play_higher_lower()
