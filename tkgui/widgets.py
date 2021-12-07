# File with widget list classes

import tkinter as tk
from typing import List, Optional

from PIL import Image as PilImage
from PIL import ImageTk

import text_ru as text
from calculations import config, constants
from calculations.numbers_kits import IntKit, RealKit


class Widgets:
    """
    Base class for a set of widgets
    """

    def __init__(self):
        self._entries_names = None
        self._entries = None
        self._buttons = None

    @property
    def entries(self):
        return self._entries

    def draw(self):
        self._entries_names.draw()
        self._entries.draw()
        self._buttons.draw()

    def hide(self):
        self._entries_names.hide()
        self._entries.hide()
        self._buttons.hide()


class IntWidgets(Widgets):
    """
    Widgets for int mode
    """

    def __init__(self, window, calculate_func, copy_func):
        super().__init__()
        self._entries_names: IntLabels = IntLabels(window)
        self._entries: IntEntries = IntEntries(window, calculate_func, copy_func)
        self._buttons: IntButtons = IntButtons(window,
                                               del_func=self._entries.clear_except_settings,
                                               copy_func=copy_func,
                                               calc_func=lambda i: Entries.call_calc(i, calculate_func))


class RealWidgets(Widgets):
    """
    Widgets for real mode
    """

    def __init__(self, window, calculate_func, copy_func):
        super().__init__()
        self._entries_names: RealLabels = RealLabels(window)
        self._entries: RealEntries = RealEntries(window, calculate_func, copy_func)

        self._buttons: RealButtons = RealButtons(window,
                                                 del_func=self._entries.clear_except_settings,
                                                 copy_func=copy_func,
                                                 calc_func=lambda i: Entries.call_calc(i, calculate_func))


class NumTypeMenu:
    """
    Menu for selecting the type of numbers
    """

    def __init__(self, window):
        self.window = window
        # List of functions for managing widget rendering
        self.__funcs = {"draw_int": lambda: None,
                        "hide_int": lambda: None,
                        "draw_real": lambda: None,
                        "hide_real": lambda: None}
        def_val = (constants.Int.TYPE_NUM if config.numbers_type == constants.Int.TYPE_NUM else constants.Real.TYPE_NUM)
        self.__numbers_type: tk.IntVar = tk.IntVar(value=def_val)  # Controller of radio-button values
        self.__int_type_button: tk.Radiobutton = tk.Radiobutton(window,
                                                                text=text.int_nums_text,
                                                                variable=self.__numbers_type,
                                                                value=0,
                                                                font="Arial 12",
                                                                command=self.__change_type)

        self.__real_type_button: tk.Radiobutton = tk.Radiobutton(window,
                                                                 text=text.real_nums_text,
                                                                 variable=self.__numbers_type,
                                                                 value=1,
                                                                 font="Arial 12",
                                                                 command=self.__change_type)

    def set_funcs(self, draw_int, hide_int, draw_real, hide_real):
        """
        Initialize the list of functions to control the rendering of widgets

        :param draw_int: function for rendering widgets for int mode
        :param hide_int: function for hide widgets for int mode
        :param draw_real: function for rendering widgets for real mode
        :param hide_real: function for hide widgets for real mode
        """
        self.__funcs["draw_int"] = draw_int
        self.__funcs["hide_int"] = hide_int
        self.__funcs["draw_real"] = draw_real
        self.__funcs["hide_real"] = hide_real

    def draw(self):
        self.__int_type_button.grid(row=0, column=0)
        self.__real_type_button.grid(row=0, column=1)

    def __change_type(self):
        num_type = self.__numbers_type.get()
        config.numbers_type = num_type  # Set type of number in config file
        if num_type == constants.Int.TYPE_NUM:
            self.__funcs["hide_real"]()
            self.__funcs["draw_int"]()
        elif num_type == constants.Real.TYPE_NUM:
            self.__funcs["hide_int"]()
            self.__funcs["draw_real"]()


class Labels:
    def __init__(self, window, names: List[str]):
        self._list: List[tk.Label] = []  # Labels list
        for name in names:
            self._list.append(tk.Label(window,
                                       text=name + ":",
                                       font=("Arial", 12),
                                       width=25,
                                       anchor=tk.W,
                                       justify=tk.LEFT))

    def draw(self, row: int = 1, column: int = 0):
        for i in range(len(self._list)):
            self._list[i].grid(row=i + row, column=column, sticky=tk.W, padx=20, pady=5)

    def hide(self):
        for item in self._list:
            item.grid_remove()


class IntLabels(Labels):
    """
    List of labels for int mode
    """

    def __init__(self, window):
        super().__init__(window, text.int_labels_text)

    def draw(self, **kwargs):
        self._list[0].grid(row=1, column=0, sticky=tk.W, padx=20, pady=(10, 20))
        for i in range(1, 6):
            self._list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20, pady=10)


class RealLabels(Labels):
    """
    List of labels for real mode
    """

    def __init__(self, window):
        super().__init__(window, text.real_labels_text)


class Entries:

    @staticmethod
    def call_calc(i, calculate_func):
        """
        Change the translation mode to the one in which Enter was pressed, and translate

        :param i: index of the field where enter was pressed
        :param calculate_func: function of starting calculations
        """
        config.translate_type = i
        calculate_func()

    def __init__(self, window, number_of_params: int):
        self._list: List[tk.Entry] = []
        for i in range(1, number_of_params + 1):
            self._list.append(tk.Entry(window, font=("Arial", 12), width=18))
        self._settings_list = set()

    def _set_settings_entries(self, *args):
        self._settings_list = set(args)

    def draw(self, row: int = 1, column: int = 1):
        for i in range(len(self._list)):
            self._list[i]["state"] = tk.NORMAL
            self._list[i].grid(row=(1 + i), column=1, sticky=tk.W)

    def hide(self):
        for item in self._list:
            item["state"] = tk.DISABLED
            item.grid_remove()

    def clear_except_settings(self):
        """
        Clear all field except settings fields
        """
        self.clear_all_except(*self._settings_list)

    def clear_all_except(self, *args):
        """
        Clears all fields except those specified in the arguments
        """
        for i in range(len(self._list)):
            if i not in args:
                self._list[i].delete(0, tk.END)

    def clear(self, *args):
        """
        Clears the fields that are specified in the arguments
        """
        for i in args:
            self._list[i].delete(0, tk.END)

    def _get(self, index) -> str:
        """
        :return: value from the field by its index
        """
        return str(self._list[index].get())

    def _write(self, index, value: str):
        """
        Write value to the field by its index
        """
        self._list[index].delete(0, tk.END)
        self._list[index].insert(0, value)

    def _bind_buttons(self, calculate_func, copy_func):
        self._bind_enter(calculate_func)
        self._bind_delete()
        self._bind_ctrlc(copy_func)

    def _bind_enter(self, calculate_func):
        pass

    def _bind_delete(self):
        pass

    def _bind_ctrlc(self, copy_func):
        pass

    def _bind_enter_button(self, index, func):
        self._list[index].bind("<Return>",
                               lambda x: Entries.call_calc(index, func))

    def _bind_delete_button(self, index):
        self._list[index].bind("<Delete>", lambda x: self.clear_except_settings())

    def _bind_ctrlc_button(self, index, func):
        self._list[index].bind("<Control-c>", lambda x: func(index))


class IntEntries(Entries):
    """
    List of entries fields in int mode
    """

    def __init__(self, window, calculate_func, copy_func):
        super().__init__(window, constants.Int.NUMBER_OF_PARAMS)
        self._set_settings_entries(constants.Int.BIN_SIZE_INDEX)
        self._list[constants.Int.BIN_SIZE_INDEX]["width"] = 5
        self.__set_bin_size(constants.Int.DEFAULT_BIN_SIZE)
        super()._bind_buttons(calculate_func, copy_func)

    def _bind_enter(self, calculate_func):
        """
        Bind 'Enter' button
        """
        self._bind_enter_button(constants.Int.DEC_NUM_INDEX, calculate_func)
        self._bind_enter_button(constants.Int.BIN_NUM_INDEX, calculate_func)
        self._bind_enter_button(constants.Int.STR_CODE_INDEX, calculate_func)
        self._bind_enter_button(constants.Int.REV_CODE_INDEX, calculate_func)
        self._bind_enter_button(constants.Int.ADD_CODE_INDEX, calculate_func)

    def _bind_delete(self):
        """
        Bind 'Delete' button
        """
        indexes = [constants.Int.DEC_NUM_INDEX, constants.Int.BIN_NUM_INDEX,
                   constants.Int.STR_CODE_INDEX, constants.Int.REV_CODE_INDEX,
                   constants.Int.ADD_CODE_INDEX]
        for index in indexes:
            self._bind_delete_button(index)

    def _bind_ctrlc(self, copy_func):
        """
        Bind 'Ctrl'+'C'
        """
        self._bind_ctrlc_button(constants.Int.DEC_NUM_INDEX, copy_func)
        self._bind_ctrlc_button(constants.Int.BIN_NUM_INDEX, copy_func)
        self._bind_ctrlc_button(constants.Int.STR_CODE_INDEX, copy_func)
        self._bind_ctrlc_button(constants.Int.REV_CODE_INDEX, copy_func)
        self._bind_ctrlc_button(constants.Int.ADD_CODE_INDEX, copy_func)

    def __set_bin_size(self, bin_size: int):
        self._list[constants.Int.BIN_SIZE_INDEX].insert(0, str(bin_size))

    def get_bin_size(self) -> str:
        return self._get(constants.Int.BIN_SIZE_INDEX)

    def get_dec_num(self) -> str:
        return self._get(constants.Int.DEC_NUM_INDEX)

    def get_bin_num(self) -> str:
        return self._get(constants.Int.BIN_NUM_INDEX)

    def get_str_code(self) -> str:
        return self._get(constants.Int.STR_CODE_INDEX)

    def get_rev_code(self) -> str:
        return self._get(constants.Int.REV_CODE_INDEX)

    def get_add_code(self) -> str:
        return self._get(constants.Int.ADD_CODE_INDEX)

    def print(self, kit: IntKit):
        """
        Print all number kit to the entries fields
        """
        self._write(constants.Int.DEC_NUM_INDEX, kit["dec_num"])
        self._write(constants.Int.BIN_NUM_INDEX, kit["bin_num"])
        self._write(constants.Int.STR_CODE_INDEX, kit["str_code"])
        self._write(constants.Int.REV_CODE_INDEX, kit["rev_code"])
        self._write(constants.Int.ADD_CODE_INDEX, kit["add_code"])

    def draw(self, **kwargs):
        self._list[0].grid(row=1, column=1, sticky=tk.W, padx=10, pady=(0, 10))
        self._list[0]["state"] = tk.NORMAL
        for i in range(1, constants.Int.NUMBER_OF_PARAMS):
            self._list[i]["state"] = tk.NORMAL
            self._list[i].grid(row=(1 + i), column=1)


class RealEntries(Entries):
    """
    List of entries fields in real mode
    """

    def __init__(self, window, calculate_func, copy_func):
        super().__init__(window, constants.Real.NUMBER_OF_PARAMS)
        self._set_settings_entries(constants.Real.MANTISSA_BIN_SIZE_INDEX, constants.Real.EXPONENT_BIN_SIZE_INDEX,
                                   constants.Real.SAVE_FIRST_DIGIT_INDEX)
        self._list[constants.Real.MANTISSA_BIN_SIZE_INDEX]["width"] = 5
        self.__set_mantissa_bin_size(constants.Real.DEFAULT_MANTISSA_BIN_SIZE)

        self._list[constants.Real.EXPONENT_BIN_SIZE_INDEX]["width"] = 5
        self.__set_exponent_bin_size(constants.Real.DEFAULT_EXPONENT_BIN_SIZE)

        self.__save: tk.IntVar = tk.IntVar(value=0)  # Controller of check-box value

        self._list[constants.Real.SAVE_FIRST_DIGIT_INDEX] = tk.Checkbutton(window,
                                                                           variable=self.__save)
        super()._bind_buttons(calculate_func, copy_func)

    def __set_mantissa_bin_size(self, mantissa_bin_size: int):
        self._list[constants.Real.MANTISSA_BIN_SIZE_INDEX].insert(0, str(mantissa_bin_size))

    def __set_exponent_bin_size(self, exponent_bin_size: int):
        self._list[constants.Real.EXPONENT_BIN_SIZE_INDEX].insert(0, str(exponent_bin_size))

    def clear_all_except(self, *args):
        super().clear_all_except(constants.Real.SAVE_FIRST_DIGIT_INDEX, *args)

    def _bind_enter(self, calculate_func):
        """
        Bind 'Enter' button
        """
        self._bind_enter_button(constants.Real.DEC_NUM_INDEX, calculate_func)
        self._bind_enter_button(constants.Real.FLOAT_FORMAT_INDEX, calculate_func)

    def _bind_delete(self):
        """
        Bind 'Delete' button
        """
        indexes = [constants.Real.DEC_NUM_INDEX, constants.Real.FLOAT_FORMAT_INDEX]
        for index in indexes:
            self._bind_delete_button(index)

    def _bind_ctrlc(self, copy_func):
        """
        Bind 'Ctrl'+'C'
        """
        self._bind_ctrlc_button(constants.Real.DEC_NUM_INDEX, copy_func)
        self._bind_ctrlc_button(constants.Real.FLOAT_FORMAT_INDEX, copy_func)

    def get_mantissa_bin_size(self) -> str:
        return self._get(constants.Real.MANTISSA_BIN_SIZE_INDEX)

    def get_exponent_bin_size(self) -> str:
        return self._get(constants.Real.EXPONENT_BIN_SIZE_INDEX)

    def get_save_first_digit(self) -> bool:
        return bool(self.__save.get())

    def get_dec_num(self) -> str:
        return self._get(constants.Real.DEC_NUM_INDEX)

    def get_bin_num(self) -> str:
        return self._get(constants.Real.BIN_NUM_INDEX)

    def get_real_format(self) -> str:
        return self._get(constants.Real.FLOAT_FORMAT_INDEX)

    def print(self, kit: RealKit):
        """
        Print all number kit to the entries fields
        """
        self._write(constants.Real.DEC_NUM_INDEX, kit["dec_num"])
        self._write(constants.Real.BIN_NUM_INDEX, kit["bin_num"])
        self._write(constants.Real.BIN_MANTISSA_INDEX, kit["bin_mantissa"])
        self._write(constants.Real.DEC_EXPONENT_INDEX, kit["dec_exponent"])
        self._write(constants.Real.DEC_CHARACTERISTIC_INDEX, kit["dec_characteristic"])
        self._write(constants.Real.BIN_CHARACTERISTIC_INDEX, kit["bin_characteristic"])
        self._write(constants.Real.FLOAT_FORMAT_INDEX, kit["real_format"])


class ButtonsRow:
    """
    Row with buttons 'clear', 'calculate' and 'copy'
    """

    @staticmethod
    def __get_image(name: str) -> ImageTk:
        try:
            image = PilImage.open(f"img/{name}.ico")
            image = image.resize((18, 18), PilImage.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            return None

    def __init__(self, window, del_func, copy_func, calc_func, row_ind):
        self.__frame: tk.Frame = tk.Frame(window)  # Frame for all three buttons

        self.calc_image: Optional[ImageTk] = ButtonsRow.__get_image("calc_icon32")

        self.del_image: Optional[ImageTk] = ButtonsRow.__get_image("del_icon32")

        self.copy_image: Optional[ImageTk] = ButtonsRow.__get_image("copy_icon32")

        self.__calc_button: tk.Button = tk.Button(self.__frame,
                                                  image=self.calc_image,
                                                  command=lambda: calc_func(row_ind))
        self.__copy_button: tk.Button = tk.Button(self.__frame,
                                                  image=self.copy_image,
                                                  command=lambda: copy_func(row_ind))

        self.__del_button: tk.Button = tk.Button(self.__frame,
                                                 image=self.del_image,
                                                 command=lambda: del_func())

        self.__calc_button.grid(row=0, column=0, padx=5)
        self.__copy_button.grid(row=0, column=1, padx=5)
        self.__del_button.grid(row=0, column=2, padx=5)

        # If files with button icons are not found
        if self.calc_image is None:
            self.__calc_button["width"] = 2
            self.__calc_button["text"] = "calc"

        if self.del_image is None:
            self.__del_button["width"] = 2
            self.__del_button["text"] = "del"

        if self.copy_image is None:
            self.__copy_button["width"] = 3
            self.__copy_button["text"] = "copy"

    def draw(self, row_num: int, column_num: int):
        self.__frame.grid(row=row_num, column=column_num, padx=(0, 25))

    def hide(self):
        self.__frame.grid_remove()


class Buttons:
    def __init__(self, window, del_func, copy_func, calc_func):
        self._list: List[ButtonsRow] = []
        self.__window = window
        self.__funcs = {"del_func": del_func,
                        "copy_func": copy_func,
                        "calc_func": calc_func}

    def append(self, index):
        self._list.append(ButtonsRow(self.__window, self.__funcs["del_func"], self.__funcs["copy_func"],
                                     self.__funcs["calc_func"], index))

    def draw(self, row: int = 2, column: int = 2):
        for i in range(len(self._list)):
            self._list[i].draw(row_num=(row + i), column_num=column)

    def hide(self):
        for item in self._list:
            item.hide()


class IntButtons(Buttons):
    def __init__(self, window, del_func, copy_func, calc_func):
        super().__init__(window, del_func, copy_func, calc_func)
        self.append(constants.Int.DEC_NUM_INDEX)
        self.append(constants.Int.BIN_NUM_INDEX)
        self.append(constants.Int.STR_CODE_INDEX)
        self.append(constants.Int.REV_CODE_INDEX)
        self.append(constants.Int.ADD_CODE_INDEX)


class RealButtons(Buttons):
    def __init__(self, window, del_func, copy_func, calc_func):
        super().__init__(window, del_func, copy_func, calc_func)
        self.append(constants.Real.DEC_NUM_INDEX)
        self.append(constants.Real.FLOAT_FORMAT_INDEX)

    def draw(self, **kwargs):
        self._list[0].draw(row_num=4, column_num=2)
        self._list[1].draw(row_num=10, column_num=2)
