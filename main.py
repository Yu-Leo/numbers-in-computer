# Главный код приложения

import tkinter as tk

import config
import constants as c
from floatOperations import calculate as float_calc
from floatOperations import copy_to_buffer as float_copy
from intOperations import calculate as int_calc
from intOperations import copy_to_buffer as int_copy
from widgets import NumTypeMenu, IntWidgets, FloatWidgets
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
        self.num_type_menu = NumTypeMenu(self.__root)
        # Виджеты режима int
        self.int_widgets = IntWidgets(self.__root,
                                      lambda: int_calc(self.int_widgets.entries),
                                      self.int_copy)
        # Виджеты режима float
        self.float_widgets = FloatWidgets(self.__root,
                                          lambda: float_calc(self.float_widgets.entries),
                                          self.float_copy)

        self.num_type_menu.set_funcs(self.int_widgets.draw, self.int_widgets.hide,
                                     self.float_widgets.draw, self.float_widgets.hide)

    def int_copy(self, index):
        int_copy(self.int_widgets.entries, index)

    def float_copy(self, index):
        float_copy(self.float_widgets.entries, index)

    def run(self):
        """Запуск приложения"""
        self.num_type_menu.draw()
        if config.numbers_type == c.Int.TYPE_NUM:  # Если по умолчанию выбран тип int
            self.int_widgets.draw()
        elif config.numbers_type == c.Float.TYPE_NUM:  # Если по умолчанию выбран тип float
            self.float_widgets.draw()
        self.__root.mainloop()


window = Window()
window.run()
