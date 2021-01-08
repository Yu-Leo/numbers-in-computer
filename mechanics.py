# Файл с механикой работы приложения

import tkinter as tk
import config
import exceptions as e
import pyperclip  # Модуль для работы с буффером
import const as c

MAX_BIN_SIZE = 100  # Максимальное кол-во двоичных разрядов


def copy_val_to_buffer(entries, index):
    if index == c.Int.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Int.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Int.STRAIGHT_CODE_INDEX:
        pyperclip.copy(entries.get_straight_code())
    elif index == c.Int.REVERSED_CODE_INDEX:
        pyperclip.copy(entries.get_reversed_code())
    elif index == c.Int.ADDITIONAL_CODE_INDEX:
        pyperclip.copy(entries.get_additional_code())


def calculate(entries):
    bin_size = get_bin_size(entries)  # Кол-во двоичных разрядов

    if config.translate_type == c.Int.DEC_NUM_INDEX:  # Исходное значение - число в десятичной сс
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX)
        dec_num = get_dec_num(entries)
        bin_num = bin(dec_num)[2:]
        entries.write(c.Int.BIN_NUM_INDEX, bin_num)

        if dec_num >= 0:
            if dec_num > 2 ** (bin_size - 1):
                raise e.DecNumValueError
            for i in range(c.Int.STRAIGHT_CODE_INDEX, c.Int.ADDITIONAL_CODE_INDEX + 1):
                entries.write(i, bin_num.rjust(bin_size, "0"))


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
