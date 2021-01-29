# Файл с функциями переводом (+ ф-ция копирования в буфер)

import pyperclip  # Модуль для работы с буфером

import config
import constants as c
import exceptions as e
from messageboxes import Messageboxes as Mb
from numbersKits import IntKit


def int_calculate(entries):
    """Расчёт в целочисленном режиме"""
    try:
        int_calc(entries)
    except e.BinSizeTypeError:
        Mb.BinSizeTypeError.show()
        entries.clear_all_except()
    except e.BinSizeValueError:
        Mb.BinSizeValueError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)

    except e.DecNumTypeError:
        Mb.DecNumTypeError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
    except e.DecNumValueCodesWarning:
        Mb.DecNumValueCodesWarning.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX,
                                 c.Int.BIN_NUM_INDEX)

    except e.BinNumTypeError:
        Mb.BinNumTypeError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
    except e.BinNumValueCodesWarning:
        Mb.BinNumValueCodesWarning.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX,
                                 c.Int.BIN_NUM_INDEX)

    except e.StrCodeTypeError:
        Mb.StrCodeTypeError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
    except e.StrCodeValueError:
        Mb.StrCodeValueError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)

    except e.RevCodeTypeError:
        Mb.RevCodeTypeError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
    except e.RevCodeValueError:
        Mb.RevCodeValueError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
    except e.AddCodeTypeError:
        Mb.AddCodeTypeError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
    except e.AddCodeValueError:
        Mb.AddCodeValueError.show()
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX)


def int_calc(entries):
    """Перевод целых чисел"""
    bin_size = get_bin_size(entries)  # Числе двоичных разрядов
    # Очистка от старых значений
    entries.clear_all_except(c.Int.BIN_SIZE_INDEX, config.translate_type)

    if config.translate_type == c.Int.DEC_NUM_INDEX:  # Исходное значение - число в десятичной сс
        dec_num = get_dec_num(entries)
        kit = IntKit(dec_num=dec_num)
        kit.by_dec_num(bin_size)
        kit.print(entries)
        # Если невозможно рассчитать представления при данном числе двоичных разрядов

    elif config.translate_type == c.Int.BIN_NUM_INDEX:  # Исходное значение - число в двоичной сс
        bin_num = get_bin_num(entries)
        kit = IntKit(bin_num=bin_num)
        kit.by_bin_num(bin_size)
        kit.print(entries)
        # Если невозможно рассчитать представления при данном числе двоичных разрядов
        if kit.codes_error():
            raise e.BinNumValueCodesWarning

    elif config.translate_type == c.Int.STR_CODE_INDEX:  # Исходное значение - прямой код числа
        str_code = get_str_code(entries, bin_size)
        kit = IntKit(str_code=str_code)
        kit.by_str_code(bin_size)
        kit.print(entries)

    elif config.translate_type == c.Int.REV_CODE_INDEX:  # Исходное значение - обратный код числа
        rev_code = get_rev_code(entries, bin_size)
        kit = IntKit(rev_code=rev_code)
        kit.by_rev_code(bin_size)
        kit.print(entries)

    elif config.translate_type == c.Int.ADD_CODE_INDEX:  # Исходное значение - дополнительный код числа
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
        t_full = int(str_code, base=2)
    except ValueError:
        raise e.StrCodeTypeError
    if len(str_code) != bin_size:
        raise e.StrCodeValueError
    return str_code


def get_rev_code(entries, bin_size):
    rev_code = entries.get_rev_code()
    try:
        t_full = int(rev_code, base=2)
    except ValueError:
        raise e.RevCodeTypeError
    if len(rev_code) != bin_size:
        raise e.RevCodeValueError
    return rev_code


def get_add_code(entries, bin_size):
    add_code = entries.get_add_code()
    try:
        t_full = int(add_code, base=2)
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
        pyperclip.copy(entries.get_str_code())
    elif index == c.Int.REV_CODE_INDEX:
        pyperclip.copy(entries.get_rev_code())
    elif index == c.Int.ADD_CODE_INDEX:
        pyperclip.copy(entries.get_add_code())
