import tkinter
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tkinter.END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    password_list.extend([random.choice(string.ascii_lowercase) for _ in range(nr_letters)])
    password_list.extend([random.choice(string.punctuation) for _ in range(nr_symbols)])
    password_list.extend([random.choice(string.digits) for _ in range(nr_numbers)])
    random.shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)  # Copy to clipboard
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    with open('./saved_password', mode='a') as file:
        website = website_entry.get()
        email = email_username_entry.get()
        password = password_entry.get()
        if len(website) == 0 or len(password) == 0:  # OR => (website or password) == '':
            messagebox.showinfo(title='Invalid data!', message="Please make sure you haven't left any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
            if is_ok:
                file.write(f'{website} | {email} | {password}\n')
                website_entry.delete('0', tkinter.END)
                password_entry.delete('0', tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.minsize()
window.config(pady=50, padx=50)
window.title('Password Manager')
canvas = tkinter.Canvas(height=200, width=200)
image = tkinter.PhotoImage(file='logo.png')

canvas.create_image(100, 100, image=image)  # my problem
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text='Website:')
website_label.grid(row=1, column=0)

email_username_label = tkinter.Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)

password_label = tkinter.Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = tkinter.Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'mskarbaschian@gmail.com')

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
password_generator_button = tkinter.Button(text='Generate Password', command=generate_password)
password_generator_button.grid(row=3, column=2)

add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
