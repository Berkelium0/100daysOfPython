from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    german_word_list = pandas.read_csv("data/german_words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    german_word_list = pandas.read_csv("data/german_words.csv").to_dict(orient="records")
timer = ""
current_word = {}


def get_random_word():
    global timer, current_word
    current_word = random.choice(german_word_list)
    flashcard.itemconfig(image, image=CARD_FRONT_IMAGE)
    flashcard.itemconfig(title, text="German", fill="black")
    flashcard.itemconfig(word, text=current_word["German"], fill="black")

    timer = window.after(3000, turn_the_card, current_word)


def turn_the_card(backside):
    flashcard.itemconfig(image, image=CARD_BACK_IMAGE)
    flashcard.itemconfig(title, text="English", fill="white")
    flashcard.itemconfig(word, text=backside["English"], fill="white")


def correct_button_press():
    global timer, current_word
    window.after_cancel(timer)
    german_word_list.remove(current_word)
    get_random_word()


def wrong_button_press():
    global timer, current_word
    get_random_word()


window = Tk()
window.title("German Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flashcard
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")

image = flashcard.create_image(400, 263, image=CARD_FRONT_IMAGE)
title = flashcard.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = flashcard.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
flashcard.grid(row=0, column=0, columnspan=2)

# Buttons
CORRECT_BUTTON_IMAGE = PhotoImage(file="images/right.png")
WRONG_BUTTON_IMAGE = PhotoImage(file="images/wrong.png")
correct_button = Button(image=CORRECT_BUTTON_IMAGE, highlightthickness=0, command=correct_button_press)
wrong_button = Button(image=WRONG_BUTTON_IMAGE, highlightthickness=0, command=wrong_button_press)
correct_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

get_random_word()

window.mainloop()

pandas.DataFrame.from_dict(german_word_list).to_csv("data/german_words_to_learn.csv", index=False)
