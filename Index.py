from tkinter import *
from tkinter import ttk


class Menu_panel(Frame):
    def __init__(self, container):
        super().__init__(container, highlightbackground='red', highlightthickness=4)

        self.label = Label(self, text='im a menu panel')
        self.label.pack(expand=True)

        self.pack(side=LEFT)


class General_frame(Frame):
    def __init__(self, container, side, **kwargs):
        super().__init__(container, kwargs, highlightbackground='blue', highlightthickness=4)
        self.pack(side=side)


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.title('App')


def main():
    app = Window()
    top_frame = General_frame(app, TOP, bg='black')
    left_frame = General_frame(app, LEFT, bg='black')
    right_frame = General_frame(app, RIGHT, bg='black')
    label = Label(top_frame, text='top panel')
    label.pack()
    label = Label(right_frame, text='right panel', anchor='center', width=100)
    label.pack()
    menu1 = Menu_panel(left_frame)
    menu2 = Menu_panel(left_frame)
    menu3 = Menu_panel(left_frame)

    app.mainloop()


if __name__ == '__main__':
    main()
