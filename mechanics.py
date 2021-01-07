import tkinter as tk
import config

def calculate(entries):
    if config.translate_type == 0:
        input_data = int(entries.list[1].get())
        for i in range(2, 5):
            entries.list[i].delete(0, tk.END)
        entries.list[2].insert(0, bin(input_data)[2:])