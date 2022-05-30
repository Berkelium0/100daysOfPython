import pandas

# Create a dictionary in this format:
# example = {"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.

def enter():
    entered_word = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in entered_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        enter()
    else:
        print(result)


enter()