# Blackjack Capstone
import random
import os
import time
import art


def deal_card():
    """Deals a single random card from a standard 52-card deck."""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return random.choice(ranks), random.choice(suits)


def calculate_hand_value(hand):
    """Calculates the value of a hand in Blackjack."""
    value = 0
    ace_count = 0
    ranks = [card[0] for card in hand]
    for rank in ranks:
        if rank.isdigit():
            value += int(rank)
        elif rank in ("J", "Q", "K"):
            value += 10
        elif rank == "A":
            value += 11
            ace_count += 1
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value


def display_hand(hand, hide_one=False):
    """Displays the cards in a hand."""
    display = []
    for i, card in enumerate(hand):
        if hide_one and i == 0:
            display.append("XX")
        else:
            display.append(f"{card[0]}{card[1][0]}")  # Rank and first letter of suit
    return ", ".join(display)


def play_blackjack():
    """Main function to run the Blackjack game."""
    money = 1000
    while money > 0:
        time.sleep(1.5)
        os.system("clear")
        print(art.logo)
        print(f"\nYour current money: ₹{money}")
        bet = 0
        while True:
            try:
                bet = int(input("Place your bet (or 0 to quit): ₹"))
                if bet == 0:
                    print("Thanks for playing!")
                    return
                if 0 < bet <= money:
                    break
                else:
                    print("Invalid bet. Please bet within your money limit.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        player_hand = []
        dealer_hand = []

        # Deal initial hands
        for _ in range(2):
            player_hand.append(deal_card())
            dealer_hand.append(deal_card())

        print(
            f"\nYour hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})"
        )
        print(
            f"Dealer's face-up card: {display_hand([dealer_hand[0]], hide_one=False)}, XX"
        )

        # Player's turn
        while calculate_hand_value(player_hand) < 21:
            action = input("Hit (h) or Stand (s)? ").lower()
            if action == "h":
                player_hand.append(deal_card())
                print(
                    f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})"
                )
                if calculate_hand_value(player_hand) > 21:
                    print("Bust! You went over 21.")
                    money -= bet
                    break
            elif action == "s":
                break
            else:
                print("Invalid action. Please enter 'h' or 's'.")

        # Dealer's turn if player hasn't busted
        if calculate_hand_value(player_hand) <= 21:
            print(
                f"\nDealer's full hand: {display_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})"
            )
            while calculate_hand_value(dealer_hand) < 17:
                print("Dealer hits.")
                dealer_hand.append(deal_card())
                print(
                    f"Dealer's hand: {display_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})"
                )
                if calculate_hand_value(dealer_hand) > 21:
                    print("Dealer busts!")
                    money += bet
                    break

            # Determine the winner
            if calculate_hand_value(dealer_hand) <= 21:
                if calculate_hand_value(player_hand) > calculate_hand_value(
                    dealer_hand
                ):
                    print("You win 🎉")
                    money += bet
                elif calculate_hand_value(player_hand) < calculate_hand_value(
                    dealer_hand
                ):
                    print("Dealer wins!")
                    money -= bet
                else:
                    print("Push! It's a tie.")

        if money <= 0:
            print("\nYou're out of money! Game over 😕")
            break


play_blackjack()
