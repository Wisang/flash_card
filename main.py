from tkinter import *
import pandas as pd
from random import choice


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    df = pd.DataFrame(data)
    to_learn = df.to_dict(orient="records")
    current_card = {}


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def on_match():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/to_learn.csv", index=False)
    next_card()
    print(len(to_learn))


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="")
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="")


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=on_match)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
