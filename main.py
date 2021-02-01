# Главный код приложения

import tkinter as tk

import calculate
import config
import constants as c
from widgets import IntWidgets
from windowParameters import WindowParameters


class Window:
    """Окно приложения"""

    def __init__(self):
        self.__root = tk.Tk()
        self.__parameters = WindowParameters()
        self.__root.title(self.__parameters.title)
        self.__root.geometry(self.__parameters.geometry())
        self.__root.resizable(*self.__parameters.resizable)
        try:
            self.__root.iconbitmap(self.__parameters.ico_path)
        except tk.TclError:  # Ошибка отображения иконки (её отсутствие)
            pass  # Иконка по умолчанию
        # Виджеты целочисленного режима
        self.int_widgets = IntWidgets(self.__root,
                                      lambda: calculate.int_calculate(self.int_widgets.entries),
                                      self.copy_to_buffer)

    def copy_to_buffer(self, index):
        calculate.copy_val_to_buffer(self.int_widgets.entries, index)

    def run(self):
        """Запуск приложения"""
        if config.numbers_type == c.Type.INT:  # Если по умолчанию выбран тип int
            self.int_widgets.draw()
        elif config.numbers_type == c.Type.FLOAT:  # Если по умолчанию выбран тип float
            pass
        self.__root.mainloop()


window = Window()
window.run()
