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
