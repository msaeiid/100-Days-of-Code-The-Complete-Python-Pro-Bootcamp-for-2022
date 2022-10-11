import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1  # 25
SHORT_BREAK_MIN = 0.5  # 5
LONG_BREAK_MIN = 0.7  # 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    windows.after_cancel(timer)
    check_mark_label.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    time_label.config(text='Timer', fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    word_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text='Break', fg=RED)
    # If it's the 2st/4st/6st rep:
    if reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text='Break', fg=PINK)
    # If it's the 1st/3st/5st/7st/ rep:
    else:
        count_down(word_sec)
        time_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if count >= 0:
        count_min = f'0{count // 60}' if count // 60 < 10 else count // 60
        count_sec = f'0{count % 60}' if count % 60 < 10 else count % 60
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += '✔'
            check_mark_label.config(text=mark)

        # ---------------------------- UI SETUP ------------------------------- #


windows = tkinter.Tk()
windows.config(padx=100, pady=50, bg=YELLOW)
windows.title("Pomodoro")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(row=1, column=1)

# Timer label
time_label = tkinter.Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
time_label.grid(row=0, column=1)

# Start button
start_button = tkinter.Button(text='Start', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = tkinter.Button(text='Reset', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmarks
check_mark_label = tkinter.Label(bg=YELLOW, fg=GREEN)
check_mark_label.grid(row=3, column=1)

# prevent close windows
windows.mainloop()
