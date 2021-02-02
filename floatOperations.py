# Файл с функциями операций в режиме float

import pyperclip  # Модуль для работы с буфером

import config
import constants as c


def calculate(entries):
    """Расчёт в режиме float"""
    try:
        float_calc(entries)
    except Exception:
        pass


def float_calc(entries):
    mantissa_bin_size = get_mantissa_bin_size(entries)
    order_bin_size = get_order_bin_size(entries)
    save_first_digit = get_save_first_digit(entries)
    # Очистка от старых значений
    entries.clear_all_except(c.Float.MANTISSA_BIN_SIZE_INDEX,
                             c.Float.ORDER_BIN_SIZE_INDEX, config.translate_type)


def get_mantissa_bin_size(entries):
    str_mantissa_bin_size = entries.get_mantissa_bin_size()
    try:
        int_mantissa_bin_size = int(str_mantissa_bin_size)
    except ValueError:
        raise ValueError
    return int_mantissa_bin_size


def get_order_bin_size(entries):
    str_order_bin_size = entries.get_order_bin_size()
    try:
        int_order_bin_size = int(str_order_bin_size)
    except ValueError:
        raise ValueError
    return int_order_bin_size


def get_save_first_digit(entries):
    return entries.get_save_first_digit()


def copy_to_buffer(entries, index):
    """Скопировать значение из поля по его индексу"""
    if index == c.Float.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Float.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Float.FLOAT_FORMAT_INDEX:
        pyperclip.copy(entries.get_float_format())
