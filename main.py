# Главный код приложения

import tkinter as tk

from windowParameters import WindowParameters
from widgets import IntWidgets
import calculate


class Window:
    """Окно приложения"""

    def __init__(self):
        self.__root = tk.Tk()
        self.__parameters = WindowParameters()
        self.__root.title(self.__parameters.title)
        self.__root.geometry(self.__parameters.geometry())
        self.__root.resizable(*self.__parameters.resizable)
        self.__root.iconbitmap(self.__parameters.ico_path)
        # Виджеты целочисленного режима
        self.int_widgets = IntWidgets(self.__root,
                                      lambda: calculate.int_calculate(self.int_widgets.entries),
                                      self.copy_to_buffer)

    def copy_to_buffer(self, index):
        calculate.copy_val_to_buffer(self.int_widgets.entries, index)

    def run(self):
        """Запуск приложения"""
        self.int_widgets.draw_int()
        self.__root.mainloop()


window = Window()
window.run()
