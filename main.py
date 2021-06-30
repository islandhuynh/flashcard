from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

window = Tk()
window.title("Fash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_image = PhotoImage(file="images/card_front.png")
flashcard.create_image(400, 263, image=flashcard_image)
flashcard.grid(column=0, row=0, columnspan=2)
flashcard.create_text(400, 150, font=TITLE_FONT, text="French")
flashcard.create_text(400, 263, font=WORD_FONT, text="trouve")

checkmark_image = PhotoImage(file="images/right.png")
checkmark_button = Button(image=checkmark_image, highlightthickness=0)
checkmark_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=1, row=1)



window.mainloop()