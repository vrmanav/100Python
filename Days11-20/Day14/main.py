# Higher or Lower - Instagram edition
from game_data import data
import random
import art
import time
import os


def check_guess(accountA_followers, accountB_follower, guess):
    """Checks if the user's guess is correct."""
    if accountA_followers > accountB_follower:
        return "a" == guess
    else:
        return "b" == guess


def format_account_data(account):
    """Formats the account data into a readable string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def get_random_account():
    """Returns a random account from the game data."""
    return random.choice(data)


def play_higher_lower():
    """Start Higher-Lower game"""

    score = 0
    continue_game = True
    os.system("clear")
    print(art.logo)
    print("* You will be displayed two Instagram accounts.")
    print("* Your task is to guess which account has more followers")
    time.sleep(3)
    os.system("clear")
    account_B = random.choice(data)

    while continue_game:
        account_A = account_B
        while account_B == account_A:
            account_B = get_random_account()

        print(f"Compare A: {format_account_data(account_A)}.")
        print(art.vs)
        print(f"Against B: {format_account_data(account_B)}.")
        guess = input(
            "\nWho do you think has more followers. Type 'A' or 'B': "
        ).lower()
        followers_A = account_A["follower_count"]
        followers_B = account_B["follower_count"]
        is_guess_correct = check_guess(followers_A, followers_B, guess)
        if is_guess_correct:
            score += 1
            print("\nGreat! you have guessed it correct 🎉")
            print(f"Your current score is {score}. Moving on to the next one ⏭️")
        else:
            continue_game = False
            print("\nSorry, that's wrong. 💀")
            print(f"Your final score: {score}.")
            print(
                f"{account_A['name']} has {followers_A} followers while {account_B['name']} has {followers_B} followers."
            )
        time.sleep(4)
        os.system("clear")


play_higher_lower()
