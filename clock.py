from tkinter import *

from time import strftime

root = Tk()
root.title("Digital clock")

def get_time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(200,get_time)

label = Label(root, font=("Calibri",90),bg="grey",fg="white")
label.pack(anchor='center')

get_time()
mainloop()
