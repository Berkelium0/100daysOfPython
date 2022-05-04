import art
import game_data
import random
import os


def clear():
    os.system('cls')


streak = 0
game_end = False

while not game_end:
    print(art.logo)
    if streak > 0:
        print("You are right! your score is " + str(streak))
    else:
        print("")
    c1 = random.choice(game_data.data)
    print(f"Compare A: {c1['name']}, a {c1['description']}, from {c1['country']}.")
    # print("cheat " + str(c1["follower_count"]))
    print(art.vs)
    c2 = random.choice(game_data.data)
    print(f"Compare B: {c2['name']}, a {c2['description']}, from {c2['country']}.")
    # print("cheat " + str(c2["follower_count"]))

    guess = input("Who has more followers? Type 'A' or 'B': ")
    if (guess == "A" or guess == "a") and c1["follower_count"] > c2["follower_count"]:
        streak += 1
    elif (guess == "B" or guess == "b") and c1["follower_count"] < c2["follower_count"]:
        streak += 1
    else:
        game_end = True
    clear()
print(art.logo)
print("Sorry you lost. Your score is: " + str(streak))
