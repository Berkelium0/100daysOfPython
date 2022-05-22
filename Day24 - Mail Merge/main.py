with open("Input/Names/invited_names.txt") as names:
    name_list = names.read().split("\n")

with open("Input/Letters/starting_letter.txt") as let:
    letter = let.read()

for name in name_list:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as current_letter:
        current_letter.write(letter.replace("[name]", f"{name}"))

print(name_list, letter)
