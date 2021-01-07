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
        self.choice = tk.IntVar(value=0)
        self.list = []
        for i in range(len(text.radiobuttons_text)):
            self.list.append(tk.Radiobutton(window,
                                            text=text.radiobuttons_text[i],
                                            variable=self.choice,
                                            value=i,
                                            font="Arial 12"))


class EntriesList:
    def __init__(self, window):
        self.list = []
        for i in range(text.entries_count):
            self.list.append(tk.Entry(window, font=("Arial", 12)))


class ButtonsList:
    def __init__(self, window):
        self.list = []
        for name in text.buttons_text:
            self.list.append(tk.Button(window, text=name, width=25))
