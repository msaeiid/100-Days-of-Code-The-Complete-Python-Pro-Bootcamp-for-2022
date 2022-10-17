import tkinter
import pandas
import random

data = pandas.read_csv('data/french_words.csv')
words = data.to_dict(orient='records')

current_card = {}


def next_card():
    global flip_timer, current_card
    windows.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=f'{current_card["French"]}', fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = windows.after(3000, func=flip_the_card)


def flip_the_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=f'{current_card["English"]}', fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, 'italic')
WORD_FONT = ("Arial", 60, 'bold')
windows = tkinter.Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_the_card)
# Card front
canvas = tkinter.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file='images/card_front.png')
card_back_img = tkinter.PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=TITLE_FONT)
card_word = canvas.create_text(400, 263, font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)
# Unknown image
cross_image = tkinter.PhotoImage(file='images/wrong.png')
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)
# Check image
check_image = tkinter.PhotoImage(file='images/right.png')
known_button = tkinter.Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
known_button.grid(row=1, column=1)
next_card()
windows.mainloop()
