# Главный код приложения

import tkinter as tk

from messageboxes import Messageboxes as Mb
from windowParametes import WindowParameters
from widgets import Widgets
import mechanics
import const as c
import exceptions as e


class Window:
    """Окно приложения"""

    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Numbers in computer")
        self.__parameters = WindowParameters()
        self.__root.geometry(self.__parameters.get_geometry())
        self.__root.resizable(*self.__parameters.get_resizable())
        self.__root.iconbitmap(self.__parameters.get_ico_path())
        self.widgets = Widgets(self.__root, self.calculate_result, self.copy_to_buffer)

    def calculate_result(self):
        try:
            mechanics.calculate(self.widgets.int_entries)
        except e.BinSizeTypeError:
            Mb.BinSizeTypeError.show()
            self.widgets.int_entries.clear_all_except()
        except e.BinSizeValueError:
            Mb.BinSizeValueError.show()
            self.widgets.int_entries.clear_all_except(c.Int.BIN_SIZE_INDEX)

        except e.DecNumTypeError:
            Mb.DecNumTypeError.show()
            self.widgets.int_entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
        except e.DecNumValueCodesWarning:
            Mb.DecNumValueCodesWarning.show()
            self.widgets.int_entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX, c.Int.BIN_NUM_INDEX)

        except e.BinNumTypeError:
            Mb.BinNumTypeError.show()
            self.widgets.int_entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
        except e.BinNumValueCodesWarning:
            Mb.BinNumValueCodesWarning.show()
            self.widgets.int_entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX, c.Int.BIN_NUM_INDEX)

    def copy_to_buffer(self, index):
        mechanics.copy_val_to_buffer(self.widgets.int_entries, index)

    def run(self):
        """Запуск приложения"""
        self.widgets.draw_int()
        self.__root.mainloop()


window = Window()
window.run()
