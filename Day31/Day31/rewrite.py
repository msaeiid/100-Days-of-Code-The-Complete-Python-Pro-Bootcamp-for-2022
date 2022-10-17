import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, 'italic')
WORD_FONT = ("Arial", 60, 'bold')

try:
    words = pandas.read_csv('data/words_to_learn_data.csv')
except FileNotFoundError:
    words = pandas.read_csv('data/french_words.csv')
to_learn = words.to_dict(orient='records')

current_word = {}


def next_card():
    global current_word, flip_timer
    windows.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=f'{current_word["French"]}', fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = windows.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv('./data/words_to_learn_data.csv', index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=f'{current_word["English"]}', fill='white')


########################## UI ##########################
windows = tkinter.Tk()
windows.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = windows.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# IMAGES
card_front_img = tkinter.PhotoImage(file='images/card_front.png')
card_back_img = tkinter.PhotoImage(file='images/card_back.png')
# back_image = canvas.create_image(400, 263, image=card_back_img)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=TITLE_FONT)
card_word = canvas.create_text(400, 263, font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# BUTTON
wrong_image = tkinter.PhotoImage(file='images/wrong.png')
right_image = tkinter.PhotoImage(file='images/right.png')
unknown_button = tkinter.Button(bg=BACKGROUND_COLOR, image=wrong_image, highlightthickness=0, command=next_card)
known_button = tkinter.Button(bg=BACKGROUND_COLOR, image=right_image, highlightthickness=0, command=is_known)
unknown_button.grid(row=1, column=0)
known_button.grid(row=1, column=1)
next_card()

windows.mainloop()
