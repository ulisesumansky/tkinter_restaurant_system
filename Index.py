
from tkinter import *
from tkinter import ttk


class Menu_panel(Frame):
    def __init__(self, container):
        super().__init__(container, highlightbackground='blue', highlightthickness=4)

        self.label = Label(self, text='im a menu panel')
        self.label.pack(expand=True)

        self.pack(side=LEFT)


class General_panel(Frame):
    def __init__(self, container, side):
        super().__init__(container, bg='black', padx=10, pady=10)
        self.pack(side=side, fill=Y)

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.title('App')


def main():
    app = Window()
    top_panel = General_panel(app, TOP)
    left_panel = General_panel(app, LEFT)
    label = Label(top_panel, text='top panel')
    menu1 = Menu_panel(left_panel)
    menu2 = Menu_panel(left_panel)
    menu3 = Menu_panel(left_panel)

    app.mainloop()


if __name__ == '__main__':
    main()
