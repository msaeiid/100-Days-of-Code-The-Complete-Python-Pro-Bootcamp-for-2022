import tkinter


def calculate_kilometer():
    miles = int(miles_input.get())
    km = round(miles * 1.60934, 2)
    kilometer_result_label.config(text=f"{km}")


windows = tkinter.Tk()
windows.title('Mile to Km Converter')
windows.minsize(width=500, height=300)
windows.config(padx=80, pady=80)

miles_input = tkinter.Entry(font=("Arial", 15), width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text='Miles', font=("Arial", 15))
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text='is equal to', font=("Arial", 15))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

kilometer_result_label = tkinter.Label(text='0', font=("Arial", 15))
kilometer_result_label.grid(column=1, row=1)
kilometer_result_label.config(padx=10, pady=10)

kilometer_label = tkinter.Label(text='Km', font=("Arial", 15))
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=10, pady=10)

calculate_button = tkinter.Button(text='Calculate', font=("Arial", 15), command=calculate_kilometer)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

windows.mainloop()
