from tkinter import *

FONT = ("Arial", 12, "normal")


def button_clicked():
    result_label.config(text=float(miles_input.get()) * 1.6)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

result_label = Label(text="0", font=FONT)
result_label.grid(row=1, column=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

window.mainloop()
