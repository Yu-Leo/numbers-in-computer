# Файл с механикой работы приложения

import tkinter as tk
import config
import exceptions as e

MAX_BIN_SIZE = 100  # Максимальное кол-во двоичных разрядов


def get_bin_size(entries):
    str_bin_size = entries.get_bin_size()
    try:
        int_bin_size = int(str_bin_size)
    except ValueError:
        raise e.BinSizeTypeError

    if not (1 <= int_bin_size <= MAX_BIN_SIZE):
        raise e.BinSizeValueError

    return int_bin_size


def get_dec_num(entries):
    input_data = entries.get_dec_num()
    try:
        dec_num = int(input_data)
    except ValueError:
        raise e.DecNumTypeError
    return dec_num


def calculate(entries):
    bin_size = get_bin_size(entries)  # Кол-во двоичных разрядов

    if config.translate_type == 0:  # Исходное значение - число в десятичной сс
        entries.clear_all_except(0, 1)
        dec_num = get_dec_num(entries)
        bin_num = bin(dec_num)[2:]
        entries.write(2, bin_num)

        if dec_num >= 0:
            if dec_num > 2 ** (bin_size - 1):
                raise e.DecNumValueError
            for i in range(3, 6):
                entries.write(i, bin_num.rjust(bin_size, "0"))
