from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Clock")
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)
label = Label(root, font=("times", 100, "bold"), background="black", foreground="cyan")
label.pack(fill=BOTH, expand=1)
time()
mainloop()