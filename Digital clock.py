from tkinter import *
from tkinter.ttk import *
from time import strftime, localtime

root = Tk()
root.title("Clock")


def time():
    current_time = strftime("%I:%M:%S %p")
    current_date = strftime("%A, %B %d, %Y")
    label.config(text=f"{current_time}\n{current_date}")
    label.after(1000, time)


label = Label(
    root,
    font="ds-digital 80",
    background="sky blue",
    foreground="green",
    justify="center",
)
label.pack(anchor="center")

time()

mainloop()
