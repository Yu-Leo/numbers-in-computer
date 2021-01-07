# Файл с классами списков виджетов

import tkinter as tk
import text
import config


class Widgets:
    def __init__(self, window, calculate_func):
        self.num_type_menu = NumTypeMenu(window)
        self.int_entries_names = IntLabels(window)
        self.int_entries_radiobuttons = IntRadiobuttons(window)
        self.int_entries = IntEntries(window)
        self.actions_menu = ActionsMenu(window, self.int_entries.clear,
                                        lambda: calculate_func(self.int_entries))

    def draw_int(self):
        """Отрисовка при целочисленном режиме"""
        self.num_type_menu.draw()
        self.int_entries_names.draw()
        self.int_entries_radiobuttons.draw()
        self.int_entries.draw()
        self.actions_menu.draw()


class NumTypeMenu:
    """Меню целые / вещественные числа"""

    def __init__(self, window):
        self.numbers_type = tk.IntVar(value=0)  # Контроллер значений радио-кнопок
        self.int_type_button = tk.Radiobutton(window,
                                              text=text.int_nums_text,
                                              variable=self.numbers_type,
                                              value=0,
                                              font="Arial 12")

        self.float_type_button = tk.Radiobutton(window,
                                                text=text.float_nums_text,
                                                variable=self.numbers_type,
                                                value=1,
                                                font="Arial 12",
                                                state=tk.DISABLED)

    def draw(self):
        self.int_type_button.grid(row=0, column=0)
        self.float_type_button.grid(row=0, column=2)


class IntLabels:
    """Список лэйблов при целочисленном режиме"""

    def __init__(self, window):
        self.list = []  # Список лэйблов
        for name in text.int_labels_text:
            self.list.append(tk.Label(window,
                                      text=name,
                                      font=("Arial", 12),
                                      anchor=tk.W))

    def draw(self):
        for i in range(6):
            self.list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20,
                              pady=10)


class IntRadiobuttons:
    """Список радио-кнопок при целочисленном режиме"""

    @staticmethod
    def __change_translate_type(i):
        config.translate_type = i

    def __init__(self, window):
        self.translate_type = tk.IntVar(value=0)  # Тип перевода
        self.list = []  # Список радио-кнопок

        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=0,
                                        command=lambda:
                                        IntRadiobuttons.__change_translate_type(0)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=1,
                                        command=lambda:
                                        IntRadiobuttons.__change_translate_type(1)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=2,
                                        command=lambda:
                                        IntRadiobuttons.__change_translate_type(2)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=3,
                                        command=lambda:
                                        IntRadiobuttons.__change_translate_type(3)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=4,
                                        command=lambda:
                                        IntRadiobuttons.__change_translate_type(4)))


    def draw(self):
        for i in range(5):
            self.list[i].grid(row=(2 + i), column=1)


class IntEntries:
    """Список полей ввода-вывода при целочисленном режиме"""

    def __init__(self, window):
        self.list = []  # Список полей для ввода
        self.list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.list[0].insert(0, "8")
        for i in range(1, text.entries_count):
            self.list.append(tk.Entry(window, font=("Arial", 12)))

    def clear(self):
        """Очищает все поля, кроме задающих настройки"""
        for i in range(1, len(self.list)):
            self.list[i].delete(0, tk.END)

    def draw(self):
        self.list[0].grid(row=1, column=2, sticky=tk.W, padx=20)
        for i in range(1, 6):
            self.list[i].grid(row=(1 + i), column=2)


class ActionsMenu:
    """Меню кнопок очистить / рассчитать"""

    def __init__(self, window, clear_func, calculate_func):
        self.clear_button = tk.Button(window, text=text.buttons_text[0],
                                      width=25, command=clear_func)

        self.calculate_button = tk.Button(window, text=text.buttons_text[1],
                                          width=25, command=calculate_func)

    def draw(self):
        self.clear_button.grid(row=7, column=0, sticky=tk.W, padx=20, pady=10)
        self.calculate_button.grid(row=7, column=2, padx=20, pady=10)
