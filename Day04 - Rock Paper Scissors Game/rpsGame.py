import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
moves = [rock, paper, scissors]
print("You chose:\n" + moves[player])
computer = random.randint(0, 2)
print("The computer chose:\n" + moves[computer])

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
  print("You Win!")
elif(player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
  print("You Lose :(")
else:
  print("It's a draw.")