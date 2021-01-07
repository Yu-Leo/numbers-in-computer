import tkinter as tk
import text


class LabelsList:
    def __init__(self, window):
        self.list = []
        for name in text.int_labels_text:
            self.list.append(tk.Label(window,
                                      text=name,
                                      font=("Arial", 12),
                                      anchor=tk.W))


class RadiobuttonsList:
    def __init__(self, window):
        self.numbers_type = tk.IntVar(value=0)
        self.translate_type = tk.IntVar(value=0)
        self.list = []
        for i in range(len(text.radiobuttons_text)):
            self.list.append(tk.Radiobutton(window,
                                            text=text.radiobuttons_text[i],
                                            variable=self.numbers_type,
                                            value=i,
                                            font="Arial 12"))

        for i in range(5):
            self.list.append(tk.Radiobutton(window,
                                            variable=self.translate_type,
                                            value=i))


class EntriesList:
    def __init__(self, window):
        self.list = []
        self.list.append(tk.Entry(window, font=("Arial", 12), width=5))
        for i in range(1, text.entries_count):
            self.list.append(tk.Entry(window, font=("Arial", 12)))


class ButtonsList:
    def __init__(self, window, clear_func, calculate_func):
        self.clear_button = tk.Button(window, text=text.buttons_text[0],
                                      width=25, command=clear_func)
        self.calculate_button = tk.Button(window, text=text.buttons_text[1],
                                      width=25, command=calculate_func)
