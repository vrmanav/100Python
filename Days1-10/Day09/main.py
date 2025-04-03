# Secret Auction

import art
import os


def find_highest_bidder(bids):
    "Finds out the user who has placed the highest bid"
    max_bid = 0
    winner_name = ""
    for user in bids:
        current_user_bid = bids[user]
        if current_user_bid > max_bid:
            winner_name = user
            max_bid = current_user_bid
    os.system("clear")
    print(f"The winner is {winner_name.capitalize()} with a bid of ₹{max_bid} 🎉")


def secret_auction():
    """Starts secret auction"""
    bids = {}
    continue_game = True
    while continue_game:
        os.system("clear")
        print(art.logo)
        print("Welcome to Secret Auction Program")
        name = input("\nWhat is your name: ").lower()
        bid_amount = int(input("Enter your bidding amount: ₹"))
        bids[name] = bid_amount
        more_bidders = input("Are there any more bidder [YES/NO]: ").lower()
        if more_bidders == "no":
            continue_game = False
            find_highest_bidder(bids)


secret_auction()
