# Файл с классами списков виджетов

import tkinter as tk
import text
import config


class Widgets:
    def __init__(self, window, calculate_func):
        self.__num_type_menu = NumTypeMenu(window)
        self.__int_entries_names = IntLabels(window)
        self.__int_entries_radiobuttons = IntRadiobuttons(window)
        self.__int_entries = IntEntries(window)
        self.__actions_menu = ActionsMenu(window,
                                          lambda: self.__int_entries.clear_all_except(0),
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
                                          IntRadiobuttons.__change_translate_type(0)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=1,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(1)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=2,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(2)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=3,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(3)))
        self.__list.append(tk.Radiobutton(window,
                                          variable=self.__translate_type,
                                          value=4,
                                          command=lambda:
                                          IntRadiobuttons.__change_translate_type(4)))

    def draw(self):
        for i in range(5):
            self.__list[i].grid(row=(2 + i), column=1)


class IntEntries:
    """Список полей ввода-вывода при целочисленном режиме"""

    def __init__(self, window):
        self.__list = []  # Список полей для ввода
        self.__list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.__list[0].insert(0, "8")
        for i in range(1, text.entries_count):
            self.__list.append(tk.Entry(window, font=("Arial", 12)))

    def clear_all_except(self, *args):
        """Очищает все поля кроме тех, которые указаны в аргументах"""
        for i in range(len(self.__list)):
            if i not in args:
                self.__list[i].delete(0, tk.END)

    def __get(self, index):
        return str(self.__list[index].get())

    def get_bin_size(self):
        return self.__get(0)

    def get_dec_num(self):
        return self.__get(1)

    def get_bin_num(self):
        return self.__get(2)

    def get_straight_code(self):
        return self.__get(3)

    def get_reversed_code(self):
        return self.__get(4)

    def get_additional_code(self):
        return self.__get(5)

    def write(self, index, value):
        self.__list[index].delete(0, tk.END)
        self.__list[index].insert(0, value)

    def draw(self):
        self.__list[0].grid(row=1, column=2, sticky=tk.W, padx=20)
        for i in range(1, 6):
            self.__list[i].grid(row=(1 + i), column=2)


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
