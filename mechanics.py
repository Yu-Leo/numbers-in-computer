# Файл с механикой работы приложения

import config
import exceptions as e
import pyperclip  # Модуль для работы с буффером
import const as c

MAX_BIN_SIZE = 100  # Максимальное кол-во двоичных разрядов


def copy_val_to_buffer(entries, index):
    """Скопировать значение из поля по его индексу"""
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
    """Основная ф-ция перевода"""
    bin_size = get_bin_size(entries)  # Кол-во двоичных разрядов

    if config.translate_type == c.Int.DEC_NUM_INDEX:  # Исходное значение - число в десятичной сс
        entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX)
        dec_num = get_dec_num(entries)
        answer = get_all_by_dec_num(bin_size, dec_num)
        for i in range(c.Int.BIN_NUM_INDEX, c.Int.ADDITIONAL_CODE_INDEX + 1):
            entries.write(i, answer[i])

        if codes_error(answer):
            raise e.DecNumValueCodesWarning


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


def get_all_by_dec_num(bin_size, dec_num):
    """Перевод во все представления по числу в 10й сс"""
    if dec_num >= 0:
        bin_num = bin(dec_num)[2:]
        if dec_num > 2 ** (bin_size - 1):
            all_codes = "-"
        else:
            all_codes = bin_num.rjust(bin_size, "0")

        straight_code = reversed_code = additional_code = all_codes

    else:  # dec_num < 0
        bin_num = "-" + bin(dec_num)[3:]
        if dec_num < -1 * (2 ** (bin_size - 1) - 1):
            all_codes = "-"
            straight_code = reversed_code = additional_code = all_codes
        else:
            straight_code = "1" + bin_num[1:].rjust(bin_size - 1, "0")
            reversed_code = get_reversed_by_straight(straight_code)
            additional_code = get_additional_by_reversed(reversed_code)

    return {c.Int.BIN_NUM_INDEX: bin_num,
            c.Int.STRAIGHT_CODE_INDEX: straight_code,
            c.Int.REVERSED_CODE_INDEX: reversed_code,
            c.Int.ADDITIONAL_CODE_INDEX: additional_code}


def get_reversed_by_straight(straight_code):
    rev_code = straight_code[0]
    for i in range(1, len(straight_code)):
        rev_code += ("1" if straight_code[i] == "0" else "0")
    return rev_code


def get_additional_by_reversed(reversed_code):
    return bin_sum(reversed_code, "1")


def bin_sum(a, b):
    """Сложение двух чисел в двоичной системе"""
    add_digit = False
    n = max(len(a), len(b))
    a = a.rjust(n, "0")
    b = b.rjust(n, "0")
    s = a
    for i in range(n - 1, 0, -1):
        if a[i] != b[i]:
            if add_digit:
                s = s[:i] + "0" + s[i + 1:]
            else:
                s = s[:i] + "1" + s[i + 1:]
        else:
            if add_digit:
                s = s[:i] + "1" + s[i + 1:]
            else:
                s = s[:i] + "0" + s[i + 1:]
            add_digit = a[i] == "1"
    if add_digit:
        s = "1" + s
    return s


def codes_error(answer):
    return answer[c.Int.STRAIGHT_CODE_INDEX] == "-"
