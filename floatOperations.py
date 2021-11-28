# File with operation's functions for float mode (and function for copy values to clipboard)

import pyperclip  # Module for working with clipboard

import config
import constants as c
import exceptions as e
import messageboxes as mb
from numbersKits import FloatKit


def calculate(entries):
    """
    Calculation in float mode with exceptions tracking

    :param entries: list of tkinter's entries objects
    """
    try:
        float_calc(entries)
    except e.FloatEntryContentError as exception:
        if exception.field == c.Float.MANTISSA_BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Float.EXPONENT_BIN_SIZE_INDEX)

        elif exception.field == c.Float.EXPONENT_BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Float.MANTISSA_BIN_SIZE_INDEX)

        elif exception.field == c.Float.DEC_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_except_settings()

        elif exception.field == c.Float.FLOAT_FORMAT_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_except_settings()


def float_calc(entries):
    """
    Calculation in float mode

    :param entries: list of tkinter's entries objects
    """
    mantissa_bin_size = get_mantissa_bin_size(entries)
    exponent_bin_size = get_exponent_bin_size(entries)
    save_first_digit = get_save_first_digit(entries)

    # Delete old values
    entries.clear_all_except(c.Float.MANTISSA_BIN_SIZE_INDEX,
                             c.Float.EXPONENT_BIN_SIZE_INDEX,
                             c.Float.SAVE_FIRST_DIGIT_INDEX,
                             config.translate_type)
    if config.translate_type == c.Float.DEC_NUM_INDEX:  # Source value - number in decimal notation
        dec_num = get_dec_num(entries)
        kit = FloatKit(dec_num=dec_num)
        kit.by_dec_num(mantissa_bin_size, exponent_bin_size, save_first_digit)
        entries.print(kit)

    elif config.translate_type == c.Float.FLOAT_FORMAT_INDEX:  # Source value - number in float representation
        float_format = get_float_format(entries, mantissa_bin_size, exponent_bin_size, save_first_digit)
        kit = FloatKit(float_format=float_format)
        kit.by_float_format(mantissa_bin_size, exponent_bin_size, save_first_digit)
        entries.print(kit)
    else:
        raise Warning("Invalid translate_type")


def get_mantissa_bin_size(entries):
    """
    :param entries: list of tkinter's entries objects
    :returns number of binary digits of the mantissa in integer type
    """
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


def get_exponent_bin_size(entries):
    """
    :param entries: list of tkinter's entries objects
    :returns number of binary digits of the exponent in integer type
    """
    str_exponent_bin_size = entries.get_exponent_bin_size()
    try:
        int_exponent_bin_size = int(str_exponent_bin_size)
    except ValueError:
        raise e.FloatEntryContentError(field=c.Float.MANTISSA_BIN_SIZE_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)

    if not (c.Float.MIN_ORD_BIN_SIZE <= int_exponent_bin_size <= c.Float.MAX_ORD_BIN_SIZE):
        raise e.FloatEntryContentError(field=c.Float.EXPONENT_BIN_SIZE_INDEX,
                                       exception_type=c.Exceptions.RANGE_ERROR)
    return int_exponent_bin_size


def get_save_first_digit(entries):
    """
    :param entries: list of tkinter's entries objects
    :returns value of checkbox 'save first digit'
    """
    return entries.get_save_first_digit()


def is_dec_num_correct(input_data):
    """
    Check, is number is correct real number
    :param input_data: verified data
    :returns is input_data contains correct real number
    """
    correct_symbols = {"-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ","}
    digits_and_punct_only = set(input_data).issubset(correct_symbols)
    one_punct = input_data.count(".") + input_data.count(",") <= 1
    return input_data != "" and digits_and_punct_only and one_punct


def replace_comma(input_data):
    """
    :returns input_data where the comma is replaced by a dot
    """
    comma_pos = input_data.find(",")
    if comma_pos != -1:
        input_data = input_data[:comma_pos] + "." + input_data[comma_pos + 1:]
    return input_data


def get_dec_num(entries):
    """
    :param entries: list of tkinter's entries objects
    :return: number in decimal notation in float type
    """
    input_data = entries.get_dec_num()

    if not is_dec_num_correct(input_data):
        raise e.FloatEntryContentError(field=c.Float.DEC_NUM_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)
    input_data = replace_comma(input_data)
    dec_num = float(input_data)
    return dec_num


def get_float_format(entries, mantissa, exponent, save):
    """
    :param entries: list of tkinter's entries objects
    :param mantissa: number of binary digits of the mantissa in integer type
    :param exponent: number of binary digits of the exponent in integer type
    :param save: is the first digit of the mantissa stored
    :return: number in float representation
    """

    float_format = entries.get_float_format()
    if not set(float_format).issubset({"0", "1"}) or float_format == "":  # If string include not only '0' and '1'
        raise e.FloatEntryContentError(field=c.Float.FLOAT_FORMAT_INDEX,
                                       exception_type=c.Exceptions.TYPE_ERROR)
    sum_len = 1 + exponent + (1 if save else 0) + mantissa  # Length of float representation
    if len(float_format) != sum_len:
        raise e.FloatEntryContentError(field=c.Float.FLOAT_FORMAT_INDEX,
                                       exception_type=c.Exceptions.RANGE_ERROR)
    return float_format


def copy_to_buffer(entries, index):
    """
    Copy value from entry to clipboard by its index
    :param entries: list of tkinter's entries objects
    :param index - index of entry field
    """
    if index == c.Float.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Float.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Float.FLOAT_FORMAT_INDEX:
        pyperclip.copy(entries.get_float_format())
