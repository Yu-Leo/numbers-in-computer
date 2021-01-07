import tkinter as tk

from windowParametes import WindowParameters
from widgets import *
from mechanics import calculate


class Window:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Numbers in computer")
        self.__parameters = WindowParameters()
        self.__root.geometry(self.__parameters.get_geometry())
        self.__root.resizable(*self.__parameters.get_resizable())
        self.__root.iconbitmap(self.__parameters.get_ico_path())

        self.choice2 = tk.IntVar(value=0)

        self.labels = LabelsList(self.__root)
        self.radiobuttons = RadiobuttonsList(self.__root)
        self.entries = EntriesList(self.__root)
        self.buttons = ButtonsList(self.__root, self.clear_entries,
                                   lambda: calculate(self.entries))

    def clear_entries(self):
        """Очищает все поля кроме задающих настройки"""
        for i in range(1, len(self.entries.list)):
            self.entries.list[i].delete(0, tk.END)

    def draw_widgets(self):
        self.radiobuttons.list[0].grid(row=0, column=0)
        self.radiobuttons.list[1].grid(row=0, column=2)

        for i in range(6):
            self.labels.list[i].grid(row=i + 1, column=0, sticky=tk.W, padx=20,
                                     pady=10)
        for i in range(5):
            self.radiobuttons.list[2 + i].grid(row=(2 + i), column=1)

        self.entries.list[0].grid(row=1, column=2, sticky=tk.W, padx=20)

        for i in range(1, 6):
            self.entries.list[i].grid(row=i + 1, column=2)

        self.buttons.clear_button.grid(row=7, column=0, sticky=tk.W, padx=20,
                                       pady=10)
        self.buttons.calculate_button.grid(row=7, column=2, padx=20, pady=10)

    def run(self):
        self.draw_widgets()
        self.__root.mainloop()


window = Window()
window.run()
