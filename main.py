# Главный код приложения

import tkinter as tk
from windowParametes import WindowParameters
from widgets import Widgets
from mechanics import calculate


class Window:
    """Окно приложения"""

    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Numbers in computer")
        self.__parameters = WindowParameters()
        self.__root.geometry(self.__parameters.get_geometry())
        self.__root.resizable(*self.__parameters.get_resizable())
        self.__root.iconbitmap(self.__parameters.get_ico_path())
        self.widgets = Widgets(self.__root, calculate)

    def run(self):
        self.widgets.draw_int()
        self.__root.mainloop()


window = Window()
window.run()
