import json
import tkinter
from tkinter import messagebox
import random
import string
import pyperclip
import json


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

# json.dump => write
# json.load => Read
# json.update => Update
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:  # OR => (website or password) == '':
        messagebox.showinfo(title='Invalid data!', message="Please make sure you haven't left any fields empty!")
    else:
        # Reading old data
        try:
            with open('./data.json', mode='r') as data_files:
                data = json.load(data_files)
        except FileNotFoundError as message:
            with open('./data.json', mode='w') as data_files:
                json.dump(new_data, data_files, indent=4)
        else:
            data.update(new_data)
            # save data
            with open('./data.json', mode='w') as data_files:
                json.dump(data, data_files, indent=4)
        finally:
            # clear fields
            website_entry.delete('0', tkinter.END)
            password_entry.delete('0', tkinter.END)


# ---------------------------- LOAD DATA ------------------------------- #

def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as message:
        messagebox.showwarning(title="bad request!", message="data file doesn't exists.")
    else:
        website = website_entry.get()
        if len(website) == 0:
            messagebox.showwarning(title="bad request!", message="please enter website.")
        else:
            requested_data = data.get(website)
            if requested_data is None:
                messagebox.showwarning(title="bad request!",
                                       message=f"there isn't any data for requested site: {website}")
            else:
                messagebox.showinfo(title=f"{website}",
                                    message=f"Email: {requested_data.get('email')}\nPassword: {requested_data.get('password')}")


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
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_entry = tkinter.Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'mskarbaschian@gmail.com')

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
password_generator_button = tkinter.Button(text='Generate Password', width=13, command=generate_password)
password_generator_button.grid(row=3, column=2)

add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", command=find_password, width=13)
search_button.grid(row=1, column=2)

window.mainloop()
