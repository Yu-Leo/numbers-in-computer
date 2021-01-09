# Файл с механикой перевода целых чисел (+ ф-ция копирования в буффер)

import config
import exceptions as e
import pyperclip  # Модуль для работы с буффером
import constants as c
from numbersKits import IntKit


def calculate(entries):
    """Основная ф-ция перевода целых чисел"""
    bin_size = get_bin_size(entries)  # Кол-во двоичных разрядов
    if config.translate_type == c.Int.DEC_NUM_INDEX:  # Исходное значение - число в десятичной сс
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX)
        dec_num = get_dec_num(entries)
        kit = IntKit(dec_num=dec_num)
        kit.by_dec_num(bin_size)
        kit.print(entries)
        if kit.codes_error():
            raise e.DecNumValueCodesWarning

    elif config.translate_type == c.Int.BIN_NUM_INDEX:  # Исходное значение - число в двоичной сс
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.BIN_NUM_INDEX)
        bin_num = get_bin_num(entries)
        kit = IntKit(bin_num=bin_num)
        kit.by_bin_num(bin_size)
        kit.print(entries)
        if kit.codes_error():
            raise e.BinNumValueCodesWarning

    elif config.translate_type == c.Int.STR_CODE_INDEX:  # Исходное значение - прямой код числа
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.STR_CODE_INDEX)
        str_code = get_str_code(entries, bin_size)
        kit = IntKit(str_code=str_code)
        kit.by_str_code(bin_size)
        kit.print(entries)

    elif config.translate_type == c.Int.REV_CODE_INDEX:  # Исходное значение - обратный код числа
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.REV_CODE_INDEX)
        rev_code = get_rev_code(entries, bin_size)
        kit = IntKit(rev_code=rev_code)
        kit.by_rev_code(bin_size)
        kit.print(entries)

    elif config.translate_type == c.Int.ADD_CODE_INDEX:  # Исходное значение - дополнительный код числа
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.ADD_CODE_INDEX)
        add_code = get_add_code(entries, bin_size)
        kit = IntKit(add_code=add_code)
        kit.by_add_code(bin_size)
        kit.print(entries)


def get_bin_size(entries):
    str_bin_size = entries.get_bin_size()
    try:
        int_bin_size = int(str_bin_size)
    except ValueError:
        raise e.BinSizeTypeError
    if not (1 <= int_bin_size <= c.Int.MAX_BIN_SIZE):
        raise e.BinSizeValueError
    return int_bin_size


def get_dec_num(entries):
    input_data = entries.get_dec_num()
    try:
        dec_num = int(input_data)
    except ValueError:
        raise e.DecNumTypeError
    return dec_num


def get_bin_num(entries):
    input_data = entries.get_bin_num()
    try:
        dec = int(input_data, base=2)
    except ValueError:
        raise e.BinNumTypeError
    return input_data


def get_str_code(entries, bin_size):
    str_code = entries.get_str_code()
    try:
        t_bin = int(str_code[1:], base=2)
        t_full = int(str_code, base=2)  # Если 0й символ не 0 или 1, вызовется ValueError
    except ValueError:
        raise e.StrCodeTypeError
    if len(str_code) != bin_size:
        raise e.StrCodeValueError
    return str_code


def get_rev_code(entries, bin_size):
    rev_code = entries.get_rev_code()
    try:
        t_bin = int(rev_code[1:], base=2)
        t_full = int(rev_code, base=2)  # Если 0й символ не 0 или 1, вызовется ValueError
    except ValueError:
        raise e.RevCodeTypeError
    if len(rev_code) != bin_size:
        raise e.RevCodeValueError
    return rev_code


def get_add_code(entries, bin_size):
    add_code = entries.get_add_code()
    try:
        t_bin = int(add_code[1:], base=2)
        t_full = int(add_code, base=2)  # Если 0й символ не 0 или 1, вызовется ValueError
    except ValueError:
        raise e.AddCodeTypeError
    if len(add_code) != bin_size:
        raise e.AddCodeValueError
    return add_code


def copy_val_to_buffer(entries, index):
    """Скопировать значение из поля по его индексу"""
    if index == c.Int.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Int.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Int.STR_CODE_INDEX:
        pyperclip.copy(entries.get_straight_code())
    elif index == c.Int.REV_CODE_INDEX:
        pyperclip.copy(entries.get_reversed_code())
    elif index == c.Int.ADD_CODE_INDEX:
        pyperclip.copy(entries.get_additional_code())
