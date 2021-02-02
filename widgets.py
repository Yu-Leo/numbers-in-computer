# Файл с классами списков виджетов

import tkinter as tk

from PIL import Image as PilImage
from PIL import ImageTk

import config
import constants as c
import text


class Widgets:
    """Базовый класс для набора виджетов"""

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
    def __init__(self, window, calculate_func, copy_func):
        super().__init__()
        self._entries_names = IntLabels(window)
        self._entries = IntEntries(window, calculate_func, copy_func)
        self._buttons = IntButtons(window,
                                   del_func=lambda i: self._entries.clear_all_except(c.Int.BIN_SIZE_INDEX),
                                   copy_func=copy_func,
                                   calc_func=lambda i: self._entries.call_calc(i, calculate_func))


class FloatWidgets(Widgets):
    def __init__(self, window):
        super().__init__()
        self._entries_names = FloatLabels(window)
        self._entries = FloatEntries(window)
        self._buttons = FloatButtons(window)


class NumTypeMenu:
    """Меню целые / вещественные числа"""

    def __init__(self, window):
        self.window = window
        # Список ф-ций для управления отрисовкой виджетов
        self.__funcs = {"draw_int": lambda: None,
                        "hide_int": lambda: None,
                        "draw_float": lambda: None,
                        "hide_float": lambda: None}
        self.__numbers_type = tk.IntVar(value=0)  # Контроллер значений радио-кнопок
        self.__int_type_button = tk.Radiobutton(window,
                                                text=text.int_nums_text,
                                                variable=self.__numbers_type,
                                                value=0,
                                                font="Arial 12",
                                                command=self.__change_type)

        self.__float_type_button = tk.Radiobutton(window,
                                                  text=text.float_nums_text,
                                                  variable=self.__numbers_type,
                                                  value=1,
                                                  font="Arial 12",
                                                  command=self.__change_type)

    def set_funcs(self, draw_int, hide_int, draw_float, hide_float):
        """Инициализируем список ф-ций для управления отрисовкой виджетов"""
        self.__funcs["draw_int"] = draw_int
        self.__funcs["hide_int"] = hide_int
        self.__funcs["draw_float"] = draw_float
        self.__funcs["hide_float"] = hide_float

    def draw(self):
        self.__int_type_button.grid(row=0, column=0)
        self.__float_type_button.grid(row=0, column=1)

    def __change_type(self):
        """Смена типа чисел"""
        type = self.__numbers_type.get()
        config.numbers_type = type  # Устанавливаем тип чисел в конфигурационном файле
        if type == c.Type.INT:
            self.__funcs["hide_float"]()
            self.__funcs["draw_int"]()
        elif type == c.Type.FLOAT:
            self.__funcs["hide_int"]()
            self.__funcs["draw_float"]()


class Labels:
    def __init__(self, window, names):
        self._list = []  # Список лэйблов
        for name in names:
            self._list.append(tk.Label(window,
                                       text=name + ":",
                                       font=("Arial", 12),
                                       width=25,
                                       anchor=tk.W,
                                       justify=tk.LEFT))

    def draw(self, row=1, column=0):
        for i in range(len(self._list)):
            self._list[i].grid(row=i + row, column=column, sticky=tk.W, padx=20, pady=5)

    def hide(self):
        for item in self._list:
            item.grid_remove()


class IntLabels(Labels):
    """Список лэйблов при целочисленном режиме"""

    def __init__(self, window):
        super().__init__(window, text.int_labels_text)

    def draw(self, **kwargs):
        self._list[0].grid(row=1, column=0, sticky=tk.W, padx=20, pady=(10, 20))
        for i in range(1, 6):
            self._list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20, pady=10)


class FloatLabels(Labels):
    """Список лэйблов при режиме вещественных чисел"""

    def __init__(self, window):
        super().__init__(window, text.float_labels_text)


class Entries:
    def __init__(self, window, number_of_params):
        self._list = []  # Список полей для ввода
        for i in range(1, number_of_params + 1):
            self._list.append(tk.Entry(window, font=("Arial", 12), width=18))

    def draw(self, row=1, column=1):
        for i in range(len(self._list)):
            self._list[i].grid(row=(1 + i), column=1, sticky=tk.W)

    def hide(self):
        for item in self._list:
            item.grid_remove()

    def clear_all_except(self, *args):
        """Очищает все поля кроме тех, которые указаны в аргументах"""
        for i in range(len(self._list)):
            if i not in args:
                self._list[i].delete(0, tk.END)

    def clear(self, *args):
        """Очищает поля, которые указаны в аргументах"""
        for i in args:
            self._list[i].delete(0, tk.END)

    def _get(self, index):
        """Получение значения из поля по его индексу"""
        return str(self._list[index].get())

    def _write(self, index, value):
        """Запись значения в поля по его индексу"""
        self._list[index].delete(0, tk.END)
        self._list[index].insert(0, value)


class IntEntries(Entries):
    """Список полей ввода-вывода при целочисленном режиме"""

    @staticmethod
    def call_calc(i, calculate_func):
        """Изменяем режим перевода на тот, в котором нажали Enter, и переводим"""
        config.translate_type = i
        calculate_func()

    def __init__(self, window, calculate_func, copy_func):
        super().__init__(window, c.Int.NUMBER_OF_PARAMS)
        self._list[c.Int.BIN_SIZE_INDEX]["width"] = 5
        self.__set_bin_size(c.Int.DEFAULT_BIN_SIZE)

        self.__bind_buttons(calculate_func, copy_func)

    def __bind_buttons(self, calculate_func, copy_func):
        self.__bind_enter(calculate_func)
        self.__bind_delete()
        self.__bind_ctrlc(copy_func)

    def __bind_enter(self, calculate_func):
        """Биндим на нажатие Enter в соотв. поле"""
        self._list[c.Int.DEC_NUM_INDEX].bind("<Return>",
                                             lambda x: IntEntries.call_calc(c.Int.DEC_NUM_INDEX, calculate_func))
        self._list[c.Int.BIN_NUM_INDEX].bind("<Return>",
                                             lambda x: IntEntries.call_calc(c.Int.BIN_NUM_INDEX, calculate_func))
        self._list[c.Int.STR_CODE_INDEX].bind("<Return>",
                                              lambda x: IntEntries.call_calc(c.Int.STR_CODE_INDEX, calculate_func))
        self._list[c.Int.REV_CODE_INDEX].bind("<Return>",
                                              lambda x: IntEntries.call_calc(c.Int.REV_CODE_INDEX, calculate_func))
        self._list[c.Int.ADD_CODE_INDEX].bind("<Return>",
                                              lambda x: IntEntries.call_calc(c.Int.ADD_CODE_INDEX, calculate_func))

    def __bind_delete(self):
        """Биндим на нажатие Delete"""
        indexes = [c.Int.DEC_NUM_INDEX, c.Int.BIN_NUM_INDEX,
                   c.Int.STR_CODE_INDEX, c.Int.REV_CODE_INDEX,
                   c.Int.ADD_CODE_INDEX]
        for index in indexes:
            self._list[index].bind("<Delete>", lambda x: self.clear_all_except(c.Int.BIN_SIZE_INDEX))

    def __bind_ctrlc(self, copy_func):
        """Биндим на нажатие Ctrl+C в соотв. поле"""
        self._list[c.Int.DEC_NUM_INDEX].bind("<Control-c>",
                                             lambda x: copy_func(c.Int.DEC_NUM_INDEX))
        self._list[c.Int.BIN_NUM_INDEX].bind("<Control-c>",
                                             lambda x: copy_func(c.Int.BIN_NUM_INDEX))
        self._list[c.Int.STR_CODE_INDEX].bind("<Control-c>",
                                              lambda x: copy_func(c.Int.STR_CODE_INDEX))
        self._list[c.Int.REV_CODE_INDEX].bind("<Control-c>",
                                              lambda x: copy_func(c.Int.REV_CODE_INDEX))
        self._list[c.Int.ADD_CODE_INDEX].bind("<Control-c>",
                                              lambda x: copy_func(c.Int.ADD_CODE_INDEX))

    def __set_bin_size(self, bin_size):
        self._list[c.Int.BIN_SIZE_INDEX].insert(0, str(bin_size))

    def get_bin_size(self):
        return self._get(c.Int.BIN_SIZE_INDEX)

    def get_dec_num(self):
        return self._get(c.Int.DEC_NUM_INDEX)

    def get_bin_num(self):
        return self._get(c.Int.BIN_NUM_INDEX)

    def get_str_code(self):
        return self._get(c.Int.STR_CODE_INDEX)

    def get_rev_code(self):
        return self._get(c.Int.REV_CODE_INDEX)

    def get_add_code(self):
        return self._get(c.Int.ADD_CODE_INDEX)

    def print(self, kit):
        """Вывод всего комплекта чисел в поля ввода-вывода"""
        self._write(c.Int.DEC_NUM_INDEX, kit["dec_num"])
        self._write(c.Int.BIN_NUM_INDEX, kit["bin_num"])
        self._write(c.Int.STR_CODE_INDEX, kit["str_code"])
        self._write(c.Int.REV_CODE_INDEX, kit["rev_code"])
        self._write(c.Int.ADD_CODE_INDEX, kit["add_code"])

    def draw(self, **kwargs):
        self._list[0].grid(row=1, column=1, sticky=tk.W, padx=10, pady=(0, 10))
        for i in range(1, c.Int.NUMBER_OF_PARAMS):
            self._list[i].grid(row=(1 + i), column=1)


class FloatEntries(Entries):
    """Список полей ввода-вывода при режиме вещ. чисел"""

    def __init__(self, window):
        super().__init__(window, c.Float.NUMBER_OF_PARAMS)
        self._list[c.Float.MANTISSA_BIN_SIZE_INDEX]["width"] = 5
        self.__set_mantissa_bin_size(c.Float.DEFAULT_MANTISSA_BIN_SIZE)

        self._list[c.Float.ORDER_BIN_SIZE_INDEX]["width"] = 5
        self.__set_order_bin_size(c.Float.DEFAULT_ORDER_BIN_SIZE)

        self._list[c.Float.SAVE_FIRST_DIGIT_INDEX] = tk.Checkbutton(window)

    def __set_mantissa_bin_size(self, mantissa_bin_size):
        self._list[c.Float.MANTISSA_BIN_SIZE_INDEX].insert(0, str(mantissa_bin_size))

    def __set_order_bin_size(self, order_bin_size):
        self._list[c.Float.ORDER_BIN_SIZE_INDEX].insert(0, str(order_bin_size))


class ButtonsRow:
    """Ряд кнопок 'очистить', 'рассчитать', 'скопировать'."""

    @staticmethod
    def __get_image(name):
        try:
            image = PilImage.open(f"img/{name}.ico")
            image = image.resize((18, 18), PilImage.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            return None

    def __init__(self, window, del_func, copy_func, calc_func, row_ind):
        self.__frame = tk.Frame(window)  # Фрейм для всех 3х кнопок

        self.calc_image = ButtonsRow.__get_image("calc_icon32")

        self.del_image = ButtonsRow.__get_image("del_icon32")

        self.copy_image = ButtonsRow.__get_image("copy_icon32")

        self.__calc_button = tk.Button(self.__frame,
                                       image=self.calc_image,
                                       command=lambda: calc_func(row_ind))
        self.__copy_button = tk.Button(self.__frame,
                                       image=self.copy_image,
                                       command=lambda: copy_func(row_ind))

        self.__del_button = tk.Button(self.__frame,
                                      image=self.del_image,
                                      command=lambda: del_func(row_ind))

        self.__calc_button.grid(row=0, column=0, padx=5)
        self.__copy_button.grid(row=0, column=1, padx=5)
        self.__del_button.grid(row=0, column=2, padx=5)

        # Если файлы с иконками кнопок не найдены
        if self.calc_image is None:
            self.__calc_button["width"] = 2
            self.__calc_button["text"] = "calc"

        if self.del_image is None:
            self.__del_button["width"] = 2
            self.__del_button["text"] = "del"

        if self.copy_image is None:
            self.__copy_button["width"] = 3
            self.__copy_button["text"] = "copy"

    def draw(self, row_num, column_num):
        self.__frame.grid(row=row_num, column=column_num, padx=(0, 25))

    def hide(self):
        self.__frame.grid_remove()


class Buttons:
    def __init__(self, window, del_func, copy_func, calc_func):
        self._list = []
        self.__window = window
        self.__funcs = {"del_func": del_func,
                        "copy_func": copy_func,
                        "calc_func": calc_func}

    def append(self, index):
        self._list.append(ButtonsRow(self.__window, self.__funcs["del_func"], self.__funcs["copy_func"],
                                     self.__funcs["calc_func"], index))

    def draw(self, row=2, column=2):
        for i in range(len(self._list)):
            self._list[i].draw(row_num=(row + i), column_num=column)

    def hide(self):
        for item in self._list:
            item.hide()


class IntButtons(Buttons):
    def __init__(self, window, del_func, copy_func, calc_func):
        super().__init__(window, del_func, copy_func, calc_func)
        self.append(c.Int.DEC_NUM_INDEX)
        self.append(c.Int.BIN_NUM_INDEX)
        self.append(c.Int.STR_CODE_INDEX)
        self.append(c.Int.REV_CODE_INDEX)
        self.append(c.Int.ADD_CODE_INDEX)


class FloatButtons(Buttons):
    def __init__(self, window):
        del_func = copy_func = calc_func = None
        super().__init__(window, del_func, copy_func, calc_func)
        self.append(c.Float.DEC_NUM_INDEX)
        self.append(c.Float.BIN_NUM_INDEX)
        self.append(c.Float.FLOAT_FORMAT_INDEX)

    def draw(self, **kwargs):
        self._list[0].draw(row_num=4, column_num=2)
        self._list[1].draw(row_num=5, column_num=2)
        self._list[2].draw(row_num=10, column_num=2)
