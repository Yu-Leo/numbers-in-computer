# Файл с функциями операций в режиме float

import pyperclip  # Модуль для работы с буфером

import config
import constants as c
from numbersKits import FloatKit


def calculate(entries):
    """Расчёт в режиме float"""
    float_calc(entries)


def float_calc(entries):
    mantissa_bin_size = get_mantissa_bin_size(entries)
    order_bin_size = get_order_bin_size(entries)
    save_first_digit = get_save_first_digit(entries)
    # Очистка от старых значений
    entries.clear_all_except(c.Float.MANTISSA_BIN_SIZE_INDEX,
                             c.Float.ORDER_BIN_SIZE_INDEX,
                             c.Float.SAVE_FIRST_DIGIT_INDEX,
                             config.translate_type)
    if config.translate_type == c.Float.DEC_NUM_INDEX:  # Исходное значение - число в десятичной с. с.
        dec_num = get_dec_num(entries)
        kit = FloatKit(dec_num=dec_num)
        kit.by_dec_num(mantissa_bin_size, order_bin_size, save_first_digit)
        entries.print(kit)

    elif config.translate_type == c.Float.FLOAT_FORMAT_INDEX:  # Исходное значение - число в вещ. представлении
        float_format = get_float_format(entries, mantissa_bin_size, order_bin_size, save_first_digit)
        kit = FloatKit(float_format=float_format)
        kit.by_float_format(mantissa_bin_size, order_bin_size, save_first_digit)
        entries.print(kit)
    else:
        raise Warning("Invalid translate_type")


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


def get_dec_num(entries):
    input_data = entries.get_dec_num()
    try:
        dec_num = float(input_data)
    except ValueError:
        raise ValueError
    return dec_num


def get_bin_num(entries):
    bin_num = entries.get_bin_num()
    if set(bin_num) != {"0", "1", "."}:  # Если строка не состоит только из 0 и 1
        raise TypeError
    return bin_num


def get_float_format(entries, mantissa, order, save):
    float_format = entries.get_float_format()
    if set(float_format) != {"0", "1"}:  # Если строка не состоит только из 0 и 1
        raise TypeError
    sum_len = 1 + order + (1 if save else 0) + mantissa  # Длина вещ. представления
    if len(float_format) != sum_len:
        raise ValueError
    return float_format


def copy_to_buffer(entries, index):
    """Скопировать значение из поля по его индексу"""
    if index == c.Float.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Float.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Float.FLOAT_FORMAT_INDEX:
        pyperclip.copy(entries.get_float_format())
