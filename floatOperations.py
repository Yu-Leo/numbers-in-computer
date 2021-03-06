# Файл с функциями операций в режиме float

import pyperclip  # Модуль для работы с буфером

import config
import constants as c
import exceptions as e
import messageboxes as mb
from numbersKits import FloatKit


def calculate(entries):
    """Расчёт в режиме float"""
    try:
        float_calc(entries)
    except e.FloatEntryContentError as exception:
        if exception.field == c.Float.MANTISSA_BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Float.ORDER_BIN_SIZE_INDEX)

        elif exception.field == c.Float.ORDER_BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Float.MANTISSA_BIN_SIZE_INDEX)

        elif exception.field == c.Float.DEC_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_except_settings()

        elif exception.field == c.Float.FLOAT_FORMAT_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_except_settings()


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
        raise e.FloatEntryContentError(field=c.Float.MANTISSA_BIN_SIZE_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)

    if not (c.Float.MIN_MANT_BIN_SIZE <= int_mantissa_bin_size <= c.Float.MAX_MANT_BIN_SIZE):
        raise e.FloatEntryContentError(field=c.Float.MANTISSA_BIN_SIZE_INDEX,
                                       exception_type=c.Exceptions.RANGE_ERROR)

    return int_mantissa_bin_size


def get_order_bin_size(entries):
    str_order_bin_size = entries.get_order_bin_size()
    try:
        int_order_bin_size = int(str_order_bin_size)
    except ValueError:
        raise e.FloatEntryContentError(field=c.Float.MANTISSA_BIN_SIZE_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)

    if not (c.Float.MIN_ORD_BIN_SIZE <= int_order_bin_size <= c.Float.MAX_ORD_BIN_SIZE):
        raise e.FloatEntryContentError(field=c.Float.ORDER_BIN_SIZE_INDEX,
                                       exception_type=c.Exceptions.RANGE_ERROR)
    return int_order_bin_size


def get_save_first_digit(entries):
    return entries.get_save_first_digit()


def is_dec_num_correct(input_data):
    """Проверка на то, является ли строка корректным вещ. числом"""
    correct_symbols = {"-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ","}
    digits_and_punct_only = set(input_data).issubset(correct_symbols)
    one_punct = input_data.count(".") + input_data.count(",") <= 1
    return input_data != "" and digits_and_punct_only and one_punct


def replace_comma(input_data):
    """Возвращает строку с заменённой на точку запятой, если она там была"""
    comma_pos = input_data.find(",")
    if comma_pos != -1:
        input_data = input_data[:comma_pos] + "." + input_data[comma_pos + 1:]
    return input_data


def get_dec_num(entries):
    input_data = entries.get_dec_num()

    if not is_dec_num_correct(input_data):
        raise e.FloatEntryContentError(field=c.Float.DEC_NUM_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)
    input_data = replace_comma(input_data)
    dec_num = float(input_data)
    return dec_num


def get_float_format(entries, mantissa, order, save):
    float_format = entries.get_float_format()
    if not set(float_format).issubset({"0", "1"}) or float_format == "":  # Если строка не состоит только из 0 и 1
        raise e.FloatEntryContentError(field=c.Float.FLOAT_FORMAT_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)
    sum_len = 1 + order + (1 if save else 0) + mantissa  # Длина вещ. представления
    if len(float_format) != sum_len:
        raise e.FloatEntryContentError(field=c.Float.FLOAT_FORMAT_INDEX,
                                       exception_type=c.Exceptions.RANGE_ERROR)
    return float_format


def copy_to_buffer(entries, index):
    """Скопировать значение из поля по его индексу"""
    if index == c.Float.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Float.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Float.FLOAT_FORMAT_INDEX:
        pyperclip.copy(entries.get_float_format())
