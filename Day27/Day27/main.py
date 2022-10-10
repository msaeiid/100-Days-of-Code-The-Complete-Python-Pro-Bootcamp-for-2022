# Tkinter to create Graphical User Interface

import tkinter


# change label text with button event
def button_clicked():
    # Challenge 1
    # label_text_number = int(my_label['text'].split()[1])
    # my_label['text'] = f'label {label_text_number + 1} times changed!'
    text = input.get()
    my_label.config(text=text)


window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=150, pady=150)

# Label
my_label = tkinter.Label(text='label 1 time changed!', font=("Arial", 24, "bold"))
# my_label.pack()  ## to show label on GUI
# my_label.pack(expand=True)  ## to show label on screen center
my_label.config(text='New text')
# my_label.pack()  ## show label onside= 'left','right','bottom','top'
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# ways to change attribute value
# my_label['text'] = 'label 2 times changed!'
# my_label.config(text='label 3 times changed!')

# button
button = tkinter.Button(text='Click Me!', command=button_clicked)
# button.pack()
# button.place(x=100, y=100)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
# input.place(x=100, y=200)
input.grid(column=3, row=2)

# NEW button
new_button = tkinter.Button(text='NEW BUTTON')
new_button.grid(column=2, row=0)
new_button.config(padx=20,pady=20)

window.mainloop()  # to stay window up
