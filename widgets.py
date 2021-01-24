# Файл с классами списков виджетов

import tkinter as tk
from PIL import Image as PilImage
from PIL import ImageTk

import text
import config
import constants as c


class IntWidgets:
    def __init__(self, window, calculate_func, copy_func):
        self.__num_type_menu = NumTypeMenu(window)
        self.__entries_names = IntLabels(window)
        self.__entries = IntEntries(window, calculate_func)
        self.__buttons = IntButtons(window,
                                    del_func=lambda i: self.__entries.clear_all_except(c.Int.BIN_SIZE_INDEX),
                                    copy_func=copy_func,
                                    calc_func=lambda i: self.__entries.call_calc(i, calculate_func))

    @property
    def entries(self):
        return self.__entries

    def draw_int(self):
        """Отрисовка при целочисленном режиме"""
        self.__num_type_menu.draw()
        self.__entries_names.draw()
        self.__entries.draw()
        self.__buttons.draw()


class NumTypeMenu:
    """Меню целые / вещественные числа"""

    def __init__(self, window):
        self.__numbers_type = tk.IntVar(value=0)  # Контроллер значений радио-кнопок
        self.__int_type_button = tk.Radiobutton(window,
                                                text=text.int_nums_text,
                                                variable=self.__numbers_type,
                                                value=0,
                                                font="Arial 12")

        self.__float_type_button = tk.Radiobutton(window,
                                                  text=text.float_nums_text,
                                                  variable=self.__numbers_type,
                                                  value=1,
                                                  font="Arial 12",
                                                  state=tk.DISABLED)

    def draw(self):
        self.__int_type_button.grid(row=0, column=0)
        self.__float_type_button.grid(row=0, column=1)


class IntLabels:
    """Список лэйблов при целочисленном режиме"""

    def __init__(self, window):
        self.__list = []  # Список лэйблов
        for name in text.int_labels_text:
            self.__list.append(tk.Label(window,
                                        text=name + ":",
                                        font=("Arial", 12),

                                        anchor=tk.W))

    def draw(self):
        for i in range(6):
            self.__list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20,
                                pady=10)


class IntEntries:
    """Список полей ввода-вывода при целочисленном режиме"""

    @staticmethod
    def call_calc(i, calculate_func):
        """Изменяем режим перевода на тот, в котором нажали Enter, и переводим"""
        config.translate_type = i
        calculate_func()

    def __init__(self, window, calculate_func):
        self.__list = []  # Список полей для ввода
        self.__list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.__list[0].insert(0, "8")  # Число двоичных разрядов по умолчанию

        for i in range(1, c.Int.ADD_CODE_INDEX + 1):
            self.__list.append(tk.Entry(window, font=("Arial", 12), width=18))

        indexes = [c.Int.DEC_NUM_INDEX, c.Int.BIN_NUM_INDEX,
                   c.Int.STR_CODE_INDEX, c.Int.REV_CODE_INDEX,
                   c.Int.ADD_CODE_INDEX]
        for index in indexes:
            # Биндим на нажатие Delete в соотв. поле
            self.__list[index].bind("<Delete>", lambda x: self.clear_all_except(c.Int.BIN_SIZE_INDEX))

        # Биндим на нажатие Enter в соотв. поле
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

    def write(self, index, value):
        """Запись значения в поля по его индексу"""
        self.__list[index].delete(0, tk.END)
        self.__list[index].insert(0, value)

    def draw(self):
        self.__list[0].grid(row=1, column=1, sticky=tk.W, padx=10)
        for i in range(1, 6):
            self.__list[i].grid(row=(1 + i), column=1)


class ButtonsRow:
    """Ряд кнопок 'очистить', 'рассчитать', 'скопировать'."""

    @staticmethod
    def __get_image(name):
        image = PilImage.open(f"img/{name}.ico")
        image = image.resize((18, 18), PilImage.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def __init__(self, window, del_func, copy_func, calc_func, row_ind):
        self.del_image = ButtonsRow.__get_image("del_icon32")
        self.calc_image = ButtonsRow.__get_image("calc_icon32")
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

    def draw(self, row_num, start_column_num):
        self.__calc_button.grid(row=row_num, column=start_column_num, padx=5)
        self.__copy_button.grid(row=row_num, column=start_column_num + 1, padx=5)
        self.__del_button.grid(row=row_num, column=start_column_num + 2, padx=5)


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
