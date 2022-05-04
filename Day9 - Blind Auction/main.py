import art
import os
clear = lambda: os.system('cls')
# HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the secret auction program.")

more = "yes"
bidders = {}




while more == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bidders[name] = bid
    clear()

highest_bidder = ""
highest_bid = 0
for name in bidders:
    bid = bidders[name]
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = name

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
