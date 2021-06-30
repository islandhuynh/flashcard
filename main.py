from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

french_word_dict = pandas.read_csv("data/french_words.csv", skiprows=0).T.to_dict()
french_word_list = [french_eng_pair for french_eng_pair in french_word_dict.values()]

eng_french_pair = {}

def new_french_word():
  global eng_french_pair
  random_index = random.randint(0, len(french_word_list) - 1)
  eng_french_pair = french_word_list[random_index]
  flashcard.itemconfig(title, text="French")
  flashcard.itemconfig(card_image, image=card_front)
  flashcard.itemconfig(word, text=eng_french_pair['French'])
  window.after(3000, flip_card)

def flip_card():
  flashcard.itemconfig(title, text="English")
  flashcard.itemconfig(word, text=eng_french_pair['English'])
  flashcard.itemconfig(card_image, image=card_back)

window = Tk()
window.title("Fash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = flashcard.create_image(400, 263, image=card_front)
flashcard.grid(column=0, row=0, columnspan=2)
title = flashcard.create_text(400, 150, font=TITLE_FONT, text="French")
word = flashcard.create_text(400, 263, font=WORD_FONT, text="")
new_french_word()

checkmark_image = PhotoImage(file="images/right.png")
checkmark_button = Button(image=checkmark_image, highlightthickness=0, command=new_french_word)
checkmark_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=flip_card)
wrong_button.grid(column=1, row=1)

window.mainloop()