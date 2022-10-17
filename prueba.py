from tkinter import *
from tkinter import ttk

root = Tk()
window = root
window.geometry('500x500')


frame = Frame(window, bg='red')
frame.pack(side=TOP)
label = ttk.Label(frame, text='hola')
label.pack(expand=True)



window.mainloop()