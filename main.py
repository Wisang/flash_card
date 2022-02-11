from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)

front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="trouve")


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
