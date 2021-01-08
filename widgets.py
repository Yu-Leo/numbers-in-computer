# Файл с классами списков виджетов

import tkinter as tk
from PIL import Image as PilImage
from PIL import ImageTk

import text
import config
import const as c


class Widgets:
    def __init__(self, window, calculate_func, copy_func):
        self.__num_type_menu = NumTypeMenu(window)
        self.__int_entries_names = IntLabels(window)
        self.__int_entries_radiobuttons = IntRadiobuttons(window)
        self.__int_entries = IntEntries(window, calculate_func)
        self.__int_copy_buttons = IntCopyButtons(window, copy_func)
        self.__actions_menu = ActionsMenu(window,
                                          lambda: self.__int_entries.clear_all_except(c.Int.BIN_SIZE_INDEX),
                                          calculate_func)

    @property
    def int_entries(self):
        return self.__int_entries

    def draw_int(self):
        """Отрисовка при целочисленном режиме"""
        self.__num_type_menu.draw()
        self.__int_entries_names.draw()
        self.__int_entries_radiobuttons.draw()
        self.__int_entries.draw()
        self.__actions_menu.draw()
        self.__int_copy_buttons.draw()


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
        self.__float_type_button.grid(row=0, column=2)


class IntLabels:
    """Список лэйблов при целочисленном режиме"""

    def __init__(self, window):
        self.__list = []  # Список лэйблов
        for name in text.int_labels_text:
            self.__list.append(tk.Label(window,
                                        text=name,
                                        font=("Arial", 12),
                                        anchor=tk.W))

    def draw(self):
        for i in range(6):
            self.__list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20,
                                pady=10)


class IntRadiobuttons:
    """Список радио-кнопок при целочисленном режиме"""

    @staticmethod
    def __change_translate_type(i):
        config.translate_type = i

    def __init__(self, window):
        self.__translate_type = tk.IntVar(value=0)  # Тип перевода
        self.__list = []  # Список радио-кнопок

        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=0,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(c.Int.DEC_NUM_INDEX)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=1,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(c.Int.BIN_NUM_INDEX)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=2,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(c.Int.STRAIGHT_CODE_INDEX)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=3,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(c.Int.REVERSED_CODE_INDEX)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=4,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(c.Int.ADDITIONAL_CODE_INDEX)))

    def draw(self):
        for i in range(5):
            self.__list[i].grid(row=(2 + i), column=1)


class IntEntries:
    """Список полей ввода-вывода при целочисленном режиме"""

    def __call_calc(self, i, calculate_func):
        """Если режим перевода совпадает с полем, в котором нажали Enter, переводим"""
        if config.translate_type == i:
            calculate_func()

    def __init__(self, window, calculate_func):
        self.__list = []  # Список полей для ввода
        self.__list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.__list[0].insert(0, "8")  # Число двоичных разрядов поумолчанию

        for i in range(1, text.entries_count):
            self.__list.append(tk.Entry(window, font=("Arial", 12)))

        # Биндим на нажатие Enter в соотв. поле
        self.__list[c.Int.DEC_NUM_INDEX].bind("<Return>",
                                              lambda x: self.__call_calc(c.Int.DEC_NUM_INDEX, calculate_func))
        self.__list[c.Int.BIN_NUM_INDEX].bind("<Return>",
                                              lambda x: self.__call_calc(c.Int.BIN_NUM_INDEX, calculate_func))
        self.__list[c.Int.STRAIGHT_CODE_INDEX].bind("<Return>",
                                                    lambda x: self.__call_calc(c.Int.STRAIGHT_CODE_INDEX,
                                                                               calculate_func))
        self.__list[c.Int.REVERSED_CODE_INDEX].bind("<Return>",
                                                    lambda x: self.__call_calc(c.Int.REVERSED_CODE_INDEX,
                                                                               calculate_func))
        self.__list[c.Int.ADDITIONAL_CODE_INDEX].bind("<Return>",
                                                      lambda x: self.__call_calc(c.Int.ADDITIONAL_CODE_INDEX,
                                                                                 calculate_func))

    def clear_all_except(self, *args):
        """Очищает все поля кроме тех, которые указаны в аргументах"""
        for i in range(len(self.__list)):
            if i not in args:
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

    def get_straight_code(self):
        return self.__get(c.Int.STRAIGHT_CODE_INDEX)

    def get_reversed_code(self):
        return self.__get(c.Int.REVERSED_CODE_INDEX)

    def get_additional_code(self):
        return self.__get(c.Int.ADDITIONAL_CODE_INDEX)

    def write(self, index, value):
        """Запись значения в поля по его индексу"""
        self.__list[index].delete(0, tk.END)
        self.__list[index].insert(0, value)

    def draw(self):
        self.__list[0].grid(row=1, column=2, sticky=tk.W, padx=20)
        for i in range(1, 6):
            self.__list[i].grid(row=(1 + i), column=2)


class IntCopyButtons:
    def __init__(self, window, copy_func):
        self.__list = []  # Список кнопок
        self.copy_image = self.__get_copy_image()
        self.__list.append(tk.Button(window,
                                     image=self.copy_image,
                                     command=lambda: copy_func(c.Int.DEC_NUM_INDEX)))
        self.__list.append(tk.Button(window,
                                     image=self.copy_image,
                                     command=lambda: copy_func(c.Int.BIN_NUM_INDEX)))
        self.__list.append(tk.Button(window,
                                     image=self.copy_image,
                                     command=lambda: copy_func(c.Int.STRAIGHT_CODE_INDEX)))
        self.__list.append(tk.Button(window,
                                     image=self.copy_image,
                                     command=lambda: copy_func(c.Int.REVERSED_CODE_INDEX)))
        self.__list.append(tk.Button(window,
                                     image=self.copy_image,
                                     command=lambda: copy_func(c.Int.ADDITIONAL_CODE_INDEX)))

    def __get_copy_image(self):
        image = PilImage.open(r"img/copy_icon32.ico")
        image = image.resize((18, 18), PilImage.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def draw(self):
        for i in range(5):
            self.__list[i].grid(row=(2 + i), column=3)


class ActionsMenu:
    """Меню кнопок очистить / рассчитать"""

    def __init__(self, window, clear_func, calculate_func):
        self.__clear_button = tk.Button(window, text=text.buttons_text[0],
                                        width=25, command=clear_func)

        self.__calculate_button = tk.Button(window, text=text.buttons_text[1],
                                            width=25, command=calculate_func)

    def draw(self):
        self.__clear_button.grid(row=7, column=0, sticky=tk.W, padx=20, pady=10)
        self.__calculate_button.grid(row=7, column=2, padx=20, pady=10)
