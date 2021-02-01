# Файл с классами списков виджетов

import tkinter as tk

from PIL import Image as PilImage
from PIL import ImageTk

import config
import constants as c
import text


class Widgets:
    """Базовый класс для набора виджетов"""

    def __init__(self, window):
        self._num_type_menu = NumTypeMenu(window)
        self._entries_names = None
        self._entries = None
        self._buttons = None

    def set_drawing_funcs(self, draw_func, hide_func):
        """Устанавливает ф-ции для отрисовки и прятания виджетов"""
        if isinstance(self, IntWidgets):
            self._num_type_menu.set_funcs(self.draw, self.hide, draw_func, hide_func)
        elif isinstance(self, FloatWidgets):
            self._num_type_menu.set_funcs(draw_func, hide_func, self.draw, self.hide)

    @property
    def entries(self):
        return self._entries

    def draw(self):
        self._num_type_menu.draw()
        self._entries_names.draw()
        self._entries.draw()
        # self._buttons.draw()

    def hide(self):
        self._entries_names.hide()
        self._entries.hide()
        # self._buttons.hide()


class IntWidgets(Widgets):
    def __init__(self, window, calculate_func, copy_func):
        super().__init__(window)
        self._entries_names = IntLabels(window)
        self._entries = IntEntries(window, calculate_func, copy_func)
        self._buttons = IntButtons(window,
                                   del_func=lambda i: self._entries.clear_all_except(c.Int.BIN_SIZE_INDEX),
                                   copy_func=copy_func,
                                   calc_func=lambda i: self._entries.call_calc(i, calculate_func))


class FloatWidgets(Widgets):
    def __init__(self, window):
        super().__init__(window)
        self._num_type_menu = NumTypeMenu(window)
        self._entries_names = FloatLabels(window)
        self._entries = FloatEntries(window)


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
            print("Выбран тип int")
        elif type == c.Type.FLOAT:
            self.__funcs["hide_int"]()
            self.__funcs["draw_float"]()
            print("Выбран тип float")


class Lables:
    def __init__(self, window, names):
        self._list = []  # Список лэйблов
        for name in names:
            self._list.append(tk.Label(window,
                                       text=name + ":",
                                       font=("Arial", 12),
                                       anchor=tk.W))

    def draw(self, row=1, column=0):
        for i in range(len(self._list)):
            self._list[i].grid(row=i + row, column=column, sticky=tk.W, padx=20, pady=10)

    def hide(self):
        for item in self._list:
            item.grid_remove()


class IntLabels(Lables):
    """Список лэйблов при целочисленном режиме"""

    def __init__(self, window):
        super().__init__(window, text.int_labels_text)

    def draw(self, *kwargs):
        self._list[0].grid(row=1, column=0, sticky=tk.W, padx=20, pady=(10, 20))
        for i in range(1, 6):
            self._list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20, pady=10)


class FloatLabels(Lables):
    """Список лэйблов при режиме вещественных чисел"""

    def __init__(self, window):
        super().__init__(window, text.float_labels_text)


class IntEntries:
    """Список полей ввода-вывода при целочисленном режиме"""

    @staticmethod
    def call_calc(i, calculate_func):
        """Изменяем режим перевода на тот, в котором нажали Enter, и переводим"""
        config.translate_type = i
        calculate_func()

    def __init__(self, window, calculate_func, copy_func):
        self.__list = []  # Список полей для ввода
        self.__list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.__list[0].insert(0, "8")  # Число двоичных разрядов по умолчанию
        for i in range(1, c.Int.ADD_CODE_INDEX + 1):
            self.__list.append(tk.Entry(window, font=("Arial", 12), width=18))

        self.__bind_buttons(calculate_func, copy_func)

    def __bind_buttons(self, calculate_func, copy_func):
        self.__bind_enter(calculate_func)
        self.__bind_delete()
        self.__bind_ctrlc(copy_func)

    def __bind_enter(self, calculate_func):
        """Биндим на нажатие Enter в соотв. поле"""
        self.__list[c.Int.DEC_NUM_INDEX].bind("<Return>",
                                              lambda x: IntEntries.call_calc(c.Int.DEC_NUM_INDEX, calculate_func))
        self.__list[c.Int.BIN_NUM_INDEX].bind("<Return>",
                                              lambda x: IntEntries.call_calc(c.Int.BIN_NUM_INDEX, calculate_func))
        self.__list[c.Int.STR_CODE_INDEX].bind("<Return>",
                                               lambda x: IntEntries.call_calc(c.Int.STR_CODE_INDEX, calculate_func))
        self.__list[c.Int.REV_CODE_INDEX].bind("<Return>",
                                               lambda x: IntEntries.call_calc(c.Int.REV_CODE_INDEX, calculate_func))
        self.__list[c.Int.ADD_CODE_INDEX].bind("<Return>",
                                               lambda x: IntEntries.call_calc(c.Int.ADD_CODE_INDEX, calculate_func))

    def __bind_delete(self):
        """Биндим на нажатие Delete"""
        indexes = [c.Int.DEC_NUM_INDEX, c.Int.BIN_NUM_INDEX,
                   c.Int.STR_CODE_INDEX, c.Int.REV_CODE_INDEX,
                   c.Int.ADD_CODE_INDEX]
        for index in indexes:
            self.__list[index].bind("<Delete>", lambda x: self.clear_all_except(c.Int.BIN_SIZE_INDEX))

    def __bind_ctrlc(self, copy_func):
        """Биндим на нажатие Ctrl+C в соотв. поле"""
        self.__list[c.Int.DEC_NUM_INDEX].bind("<Control-c>",
                                              lambda x: copy_func(c.Int.DEC_NUM_INDEX))
        self.__list[c.Int.BIN_NUM_INDEX].bind("<Control-c>",
                                              lambda x: copy_func(c.Int.BIN_NUM_INDEX))
        self.__list[c.Int.STR_CODE_INDEX].bind("<Control-c>",
                                               lambda x: copy_func(c.Int.STR_CODE_INDEX))
        self.__list[c.Int.REV_CODE_INDEX].bind("<Control-c>",
                                               lambda x: copy_func(c.Int.REV_CODE_INDEX))
        self.__list[c.Int.ADD_CODE_INDEX].bind("<Control-c>",
                                               lambda x: copy_func(c.Int.ADD_CODE_INDEX))

    def clear_all_except(self, *args):
        """Очищает все поля кроме тех, которые указаны в аргументах"""
        for i in range(len(self.__list)):
            if i not in args:
                self.__list[i].delete(0, tk.END)

    def clear(self, *args):
        """Очищает поля, которые указаны в аргументах"""
        for i in args:
            self.__list[i].delete(0, tk.END)

    def __get(self, index):
        """Получение значения из поля по его индексу"""
        return str(self.__list[index].get())

    def get_bin_size(self):
        return self.__get(c.Int.BIN_SIZE_INDEX)

    def get_dec_num(self):
        return self.__get(c.Int.DEC_NUM_INDEX)

    def get_bin_num(self):
        return self.__get(c.Int.BIN_NUM_INDEX)

    def get_str_code(self):
        return self.__get(c.Int.STR_CODE_INDEX)

    def get_rev_code(self):
        return self.__get(c.Int.REV_CODE_INDEX)

    def get_add_code(self):
        return self.__get(c.Int.ADD_CODE_INDEX)

    def __write(self, index, value):
        """Запись значения в поля по его индексу"""
        self.__list[index].delete(0, tk.END)
        self.__list[index].insert(0, value)

    def print(self, kit):
        """Вывод всего комплекта чисел в поля ввода-вывода"""
        self.__write(c.Int.DEC_NUM_INDEX, kit["dec_num"])
        self.__write(c.Int.BIN_NUM_INDEX, kit["bin_num"])
        self.__write(c.Int.STR_CODE_INDEX, kit["str_code"])
        self.__write(c.Int.REV_CODE_INDEX, kit["rev_code"])
        self.__write(c.Int.ADD_CODE_INDEX, kit["add_code"])

    def draw(self):
        self.__list[0].grid(row=1, column=1, sticky=tk.W, padx=10, pady=(0, 10))
        for i in range(1, 6):
            self.__list[i].grid(row=(1 + i), column=1)

    def hide(self):
        for item in self.__list:
            item.grid_remove()


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
        self.calc_image = ButtonsRow.__get_image("calc_icon32")

        self.del_image = ButtonsRow.__get_image("del_icon32")

        self.copy_image = ButtonsRow.__get_image("copy_icon32")

        self.__calc_button = tk.Button(window,
                                       image=self.calc_image,
                                       command=lambda: calc_func(row_ind))
        self.__copy_button = tk.Button(window,
                                       image=self.copy_image,
                                       command=lambda: copy_func(row_ind))

        self.__del_button = tk.Button(window,
                                      image=self.del_image,
                                      command=lambda: del_func(row_ind))

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

    def draw(self, row_num, start_column_num):
        self.__calc_button.grid(row=row_num, column=start_column_num, padx=5)
        self.__copy_button.grid(row=row_num, column=start_column_num + 1, padx=5)
        self.__del_button.grid(row=row_num, column=start_column_num + 2, padx=5)

    def hide(self):
        self.__calc_button.grid_remove()
        self.__copy_button.grid_remove()
        self.__del_button.grid_remove()


class IntButtons:
    def __init__(self, window, del_func, copy_func, calc_func):
        self.__list = []  # Список рядов кнопок
        self.__list.append(ButtonsRow(window, del_func, copy_func, calc_func,
                                      c.Int.DEC_NUM_INDEX))
        self.__list.append(ButtonsRow(window, del_func, copy_func, calc_func,
                                      c.Int.BIN_NUM_INDEX))
        self.__list.append(ButtonsRow(window, del_func, copy_func, calc_func,
                                      c.Int.STR_CODE_INDEX))
        self.__list.append(ButtonsRow(window, del_func, copy_func, calc_func,
                                      c.Int.REV_CODE_INDEX))
        self.__list.append(ButtonsRow(window, del_func, copy_func, calc_func,
                                      c.Int.ADD_CODE_INDEX))

    def draw(self):
        for i in range(len(self.__list)):
            self.__list[i].draw(row_num=(2 + i), start_column_num=2)

    def hide(self):
        for item in self.__list:
            item.hide()


class FloatEntries:
    """Список полей ввода-вывода при режиме вещ. чисел"""

    def __init__(self, window):
        self.__list = []  # Список полей для ввода
        self.__list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.__list[0].insert(0, "8")  # Число двоичных разрядов по умолчанию
        for i in range(1, 10):
            self.__list.append(tk.Entry(window, font=("Arial", 12), width=18))

    def draw(self):
        self.__list[0].grid(row=1, column=1, sticky=tk.W, padx=10, pady=(0, 10))
        for i in range(1, 10):
            self.__list[i].grid(row=(1 + i), column=1)

    def hide(self):
        for item in self.__list:
            item.grid_remove()
