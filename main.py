# Главный код приложения

import tkinter as tk
from windowParametes import WindowParameters
from widgets import Widgets
import mechanics
import exceptions as e
import text


class Window:
    """Окно приложения"""

    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Numbers in computer")
        self.__parameters = WindowParameters()
        self.__root.geometry(self.__parameters.get_geometry())
        self.__root.resizable(*self.__parameters.get_resizable())
        self.__root.iconbitmap(self.__parameters.get_ico_path())
        self.widgets = Widgets(self.__root, self.calculate_result)

    def calculate_result(self):
        try:
            mechanics.calculate(self.widgets.int_entries)
        except e.BinSizeTypeError:
            # Вызов messagebox
            print(text.Exceptions.bin_size_type_error)
            self.widgets.int_entries.clear_all_except(0)
        except e.BinSizeValueError:
            # Вызов messagebox
            print(text.Exceptions.bin_size_value_error)
            self.widgets.int_entries.clear_all_except(0)
        except e.DecNumTypeError:
            # Вызов messagebox
            print(text.Exceptions.dec_num_type_error)
            self.widgets.int_entries.clear_all_except(0)
        except e.DecNumValueError:
            # Вызов messagebox
            print(text.Exceptions.dec_num_value_error)
            self.widgets.int_entries.clear_all_except(0, 1, 2)

    def run(self):
        self.widgets.draw_int()
        self.__root.mainloop()


window = Window()
window.run()
