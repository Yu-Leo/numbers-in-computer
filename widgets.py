# Файл с классами списков виджетов

import tkinter as tk
from PIL import Image as PilImage
from PIL import ImageTk
import text
import config


class LabelsList:
    def __init__(self, window):
        self.list = []  # Список лэйблов
        for name in text.int_labels_text:
            self.list.append(tk.Label(window,
                                      text=name,
                                      font=("Arial", 12),
                                      anchor=tk.W))


class RadiobuttonsList:
    def __init__(self, window):
        self.numbers_type = tk.IntVar(value=0)  # Целые числа / вещественные
        self.translate_type = tk.IntVar(value=0)  # Тип перевода
        self.list = []  # Список радио-кнопок
        self.list.append(tk.Radiobutton(window,
                                        text=text.int_nums_text,
                                        variable=self.numbers_type,
                                        value=0,
                                        font="Arial 12"))
        self.list.append(tk.Radiobutton(window,
                                        text=text.float_nums_text,
                                        variable=self.numbers_type,
                                        value=1,
                                        font="Arial 12",
                                        state=tk.DISABLED))

        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=0,
                                        command=lambda:
                                        self.change_translate_type(0)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=1,
                                        command=lambda:
                                        self.change_translate_type(1)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=2,
                                        command=lambda:
                                        self.change_translate_type(2)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=3,
                                        command=lambda:
                                        self.change_translate_type(3)))
        self.list.append(tk.Radiobutton(window,
                                        variable=self.translate_type,
                                        value=4,
                                        command=lambda:
                                        self.change_translate_type(4)))

    def change_translate_type(self, i):
        config.translate_type = i


class EntriesList:
    def __init__(self, window):
        self.list = []  # Список полей для ввода
        self.list.append(tk.Entry(window, font=("Arial", 12), width=5))
        self.list[0].insert(0, "8")
        for i in range(1, text.entries_count):
            self.list.append(tk.Entry(window, font=("Arial", 12)))


class ButtonsList:
    def __init__(self, window, clear_func, calculate_func):
        clear_image = PilImage.open(r"img/clear_icon32.ico")
        clear_image = clear_image.resize((20, 20), PilImage.ANTIALIAS)
        self.clear_image = ImageTk.PhotoImage(clear_image)

        # self.clear_button = tk.Button(window, text=text.buttons_text[0],
        #                              width=200, command=clear_func,
        #                              image=self.clear_image, compound=tk.LEFT)

        self.clear_button = tk.Button(window, text=text.buttons_text[0],
                                      width=25, command=clear_func)

        self.calculate_button = tk.Button(window, text=text.buttons_text[1],
                                          width=25, command=calculate_func)


        self.copy_buttons_list = []  # Список кнопок для копирования значений
        copy_image = PilImage.open(r"img/copy_icon32.ico")
        copy_image = copy_image.resize((20, 20), PilImage.ANTIALIAS)
        self.copy_image = ImageTk.PhotoImage(copy_image)

        self.copy_buttons_list.append(tk.Button(window,
                                                image=self.copy_image))
