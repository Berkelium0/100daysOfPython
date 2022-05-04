############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
import os


def clear():
    os.system('cls')


def score(hand):
    sum = 0
    aceflag = 0

    for card in hand:
        if card == 11:
            aceflag += 1
        sum += card

        if sum > 21 and aceflag != 0:
            hand[hand.index(11)] = 1
            aceflag -= 1
            sum -= 10

    return sum


def final(yhand, chand):
    print(f"  Your final hand: {yhand}, final score: {score(yhand)}")
    print(f"  Computer's final hand: {chand}, final score: {score(chand)}")


while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()

    if play == "y":
        print(logo)
        yhand = []
        chand = []
        cdone = False

        yhand.append(random.choice(cards))
        yhand.append(random.choice(cards))
        chand.append(random.choice(cards))
        chand.append(random.choice(cards))

        while True:

            print(f"  Your cards: {yhand}, current score: {score(yhand)}")
            print(f"  Computer's first card: {chand[0]}")

            if score(chand) == 21:
                final(yhand, chand)
                print("Computer has blackjack you lose.")
                break
            elif score(yhand) == 21:
                final(yhand, chand)
                print("You have blackjack you win!")
                break
            elif score(yhand) > 21:
                final(yhand, chand)
                print("You score is over 21. You lose.")
                break
            elif score(chand) > 21:
                final(yhand, chand)
                print("Computer's score is over 21. You win!")
                break
            elif cdone and score(yhand) > score(chand):
                final(yhand, chand)
                print("Your score is over Computer's score. You win!")
                break
            elif cdone and score(yhand) < score(chand):
                final(yhand, chand)
                print("Computer's score is over your score. You lose.")
                break
            elif cdone and score(yhand) == score(chand):
                final(yhand, chand)
                print("Your score equals Computer's score. It's a draw")
                break
            if play == "y":
                play = input("Type 'y' to get another card, type 'n' to pass: ")
            if play == "y":
                yhand.append(random.choice(cards))
            elif score(chand) < 17:
                chand.append(random.choice(cards))
            elif score(chand) > 16:
                cdone = True

    else:
        print("Then go fuck yourself!")
        break

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
