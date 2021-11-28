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
    """
    Main application window
    """

    def __init__(self):
        self.__root = tk.Tk()
        self.__parameters = WindowParameters()
        self.__root.title(self.__parameters.title)
        self.__root.geometry(self.__parameters.geometry())
        self.__root.resizable(*self.__parameters.resizable)
        try:
            self.__root.iconbitmap(self.__parameters.ico_path)
        except tk.TclError:  # Error with icon display (icon file not found)
            pass  # Using default icons
        self.num_type_menu = NumTypeMenu(self.__root)
        # Widgets for working with integer type (int mode)
        self.int_widgets = IntWidgets(self.__root,
                                      calculate_func=lambda: int_calc(self.int_widgets.entries),
                                      copy_func=lambda index: int_copy(self.int_widgets.entries, index))
        # Widgets for working with float type (float mode)
        self.float_widgets = FloatWidgets(self.__root,
                                          calculate_func=lambda: float_calc(self.float_widgets.entries),
                                          copy_func=lambda index: float_copy(self.float_widgets.entries, index))

        self.num_type_menu.set_funcs(self.int_widgets.draw, self.int_widgets.hide,
                                     self.float_widgets.draw, self.float_widgets.hide)

    def run(self):
        """
        Run application
        """
        self.num_type_menu.draw()
        if config.numbers_type == c.Int.TYPE_NUM:
            self.int_widgets.draw()
        elif config.numbers_type == c.Float.TYPE_NUM:
            self.float_widgets.draw()
        self.__root.mainloop()


window = Window()
window.run()
