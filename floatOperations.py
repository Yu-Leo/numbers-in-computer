# Файл с функциями операций в режиме float

import pyperclip  # Модуль для работы с буфером

import constants as c


def calculate(entries):
    """Расчёт в режиме float"""
    try:
        float_calc(entries)
    except Exception:
        pass


def float_calc(entries):
    pass


def copy_to_buffer(entries, index):
    """Скопировать значение из поля по его индексу"""
    if index == c.Float.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Float.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Float.FLOAT_FORMAT_INDEX:
        pyperclip.copy(entries.get_float_format())
