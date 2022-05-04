# Include an ASCII art logo.
import random
from art import logo

print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
answer = random.randrange(1, 101)
print("Psst, It is " + str(answer))
diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diff == 'easy':
    att = 10
else:
    att = 5

print("You have " + str(att) + " attempts to make a guess.")

while att != 0:
    guess = int(input("Make a guess: "))
    if guess == answer:
        print("You got it! The answer was " + str(answer))
        break
    elif guess > answer:
        print("Too high!")
        att -= 1
    elif guess < answer:
        print("Too low!")
        att -= 1
    print("Guess again.\nYou have " + str(att) + " attempts remaining to guess the number.")
    if att == 0:
        print("You run out of guesses, you lose.")

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
