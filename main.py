import tkinter as tk

from WindowParametes import WindowParameters
from Widgets import *


class Window:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Numbers in computer")
        self.__parameters = WindowParameters()
        self.__root.geometry(self.__parameters.get_geometry())
        self.__root.resizable(*self.__parameters.get_resizable())
        self.__root.iconbitmap(self.__parameters.get_ico_path())

        self.labels = LabelsList(self.__root)
        self.radiobuttons = RadiobuttonsList(self.__root)
        self.entries = EntriesList(self.__root)
        self.buttons = ButtonsList(self.__root)

    def draw_widgets(self):
        for i in range(2):
            self.radiobuttons.list[i].grid(row=0, column=i)

        for i in range(6):
            self.labels.list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20,
                                     pady=10)
        for i in range(6):
            self.entries.list[i].grid(row=i + 1, column=1)

        self.buttons.list[0].grid(row=7, column=0, sticky=tk.W, padx=20,
                                  pady=10)
        self.buttons.list[1].grid(row=7, column=1, padx=20, pady=10)

    def run(self):
        self.draw_widgets()
        self.__root.mainloop()


window = Window()
window.run()
