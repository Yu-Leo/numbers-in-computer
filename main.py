import tkinter as tk

from calculations import config, constants as constants
from tkgui.int_operations import calculate as int_calc
from tkgui.int_operations import copy_to_clipboard as int_copy
from tkgui.real_operations import calculate as real_calc
from tkgui.real_operations import copy_to_clipboard as real_copy
from tkgui.widgets import NumTypeMenu, IntWidgets, RealWidgets
from tkgui.window_parameters import WindowParameters


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
        # Widgets for working with real type (real mode)
        self.real_widgets = RealWidgets(self.__root,
                                        calculate_func=lambda: real_calc(self.real_widgets.entries),
                                        copy_func=lambda index: real_copy(self.real_widgets.entries, index))

        self.num_type_menu.set_funcs(self.int_widgets.draw, self.int_widgets.hide,
                                     self.real_widgets.draw, self.real_widgets.hide)

    def run(self):
        """
        Run application
        """
        self.num_type_menu.draw()
        if config.numbers_type == constants.Int.TYPE_NUM:
            self.int_widgets.draw()
        elif config.numbers_type == constants.Real.TYPE_NUM:
            self.real_widgets.draw()
        self.__root.mainloop()


window = Window()
window.run()
