# File with operation's functions for real mode (and function for copy values to clipboard)

import pyperclip  # Module for working with clipboard

import exceptions as e
import tkgui.messageboxes as mb
from calculations import config, constants as c
from calculations.numbers_kits import RealKit


def calculate(entries):
    """
    Calculation in real mode with exceptions tracking

    :param entries: list of tkinter's entries objects
    """
    try:
        real_calc(entries)
    except e.RealEntryContentError as exception:
        if exception.field == c.Real.MANTISSA_BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Real.EXPONENT_BIN_SIZE_INDEX)

        elif exception.field == c.Real.EXPONENT_BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Real.MANTISSA_BIN_SIZE_INDEX)

        elif exception.field == c.Real.DEC_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_except_settings()

        elif exception.field == c.Real.FLOAT_FORMAT_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_except_settings()


def real_calc(entries):
    """
    Calculation in real mode

    :param entries: list of tkinter's entries objects
    """
    mantissa_bin_size = get_mantissa_bin_size(entries)
    exponent_bin_size = get_exponent_bin_size(entries)
    save_first_digit = get_save_first_digit(entries)

    # Delete old values
    entries.clear_all_except(c.Real.MANTISSA_BIN_SIZE_INDEX,
                             c.Real.EXPONENT_BIN_SIZE_INDEX,
                             c.Real.SAVE_FIRST_DIGIT_INDEX,
                             config.translate_type)
    if config.translate_type == c.Real.DEC_NUM_INDEX:  # Source value - number in decimal notation
        dec_num = get_dec_num(entries)
        kit = RealKit(dec_num=dec_num)
        kit.by_dec_num(mantissa_bin_size, exponent_bin_size, save_first_digit)
        entries.print(kit)

    elif config.translate_type == c.Real.FLOAT_FORMAT_INDEX:  # Source value - number in real representation
        real_format = get_real_format(entries, mantissa_bin_size, exponent_bin_size, save_first_digit)
        kit = RealKit(real_format=real_format)
        kit.by_float_format(mantissa_bin_size, exponent_bin_size, save_first_digit)
        entries.print(kit)
    else:
        raise Warning("Invalid translate_type")


def get_mantissa_bin_size(entries) -> int:
    """
    :param entries: list of tkinter's entries objects
    :return: number of binary digits of the mantissa
    """
    str_mantissa_bin_size = entries.get_mantissa_bin_size()
    try:
        int_mantissa_bin_size = int(str_mantissa_bin_size)
    except ValueError:
        raise e.RealEntryContentError(field=c.Real.MANTISSA_BIN_SIZE_INDEX,
                                      exception_type=c.Exceptions.TYPE_ERROR)

    if not (c.Real.MIN_MANT_BIN_SIZE <= int_mantissa_bin_size <= c.Real.MAX_MANT_BIN_SIZE):
        raise e.RealEntryContentError(field=c.Real.MANTISSA_BIN_SIZE_INDEX,
                                      exception_type=c.Exceptions.RANGE_ERROR)

    return int_mantissa_bin_size


def get_exponent_bin_size(entries) -> int:
    """
    :param entries: list of tkinter's entries objects
    :return: number of binary digits of the exponent
    """
    str_exponent_bin_size = entries.get_exponent_bin_size()
    try:
        int_exponent_bin_size = int(str_exponent_bin_size)
    except ValueError:
        raise e.RealEntryContentError(field=c.Real.MANTISSA_BIN_SIZE_INDEX,
                                      exception_type=c.Exceptions.TYPE_ERROR)

    if not (c.Real.MIN_EXP_BIN_SIZE <= int_exponent_bin_size <= c.Real.MAX_EXP_BIN_SIZE):
        raise e.RealEntryContentError(field=c.Real.EXPONENT_BIN_SIZE_INDEX,
                                      exception_type=c.Exceptions.RANGE_ERROR)
    return int_exponent_bin_size


def get_save_first_digit(entries) -> bool:
    """
    :param entries: list of tkinter's entries objects
    :return: value of checkbox 'save first digit'
    """
    return entries.get_save_first_digit()


def is_dec_num_correct(input_data: str) -> bool:
    """
    Check, is number is correct real number

    :param input_data: verified data
    :return: is input_data contains correct real number
    """
    correct_symbols = {"-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ","}
    digits_and_punct_only = set(input_data).issubset(correct_symbols)
    one_punct = input_data.count(".") + input_data.count(",") <= 1
    return input_data != "" and digits_and_punct_only and one_punct


def replace_comma(input_data: str) -> str:
    """
    :return: input_data where the comma is replaced by a dot
    """
    comma_pos = input_data.find(",")
    if comma_pos != -1:
        input_data = input_data[:comma_pos] + "." + input_data[comma_pos + 1:]
    return input_data


def get_dec_num(entries) -> float:
    """
    :param entries: list of tkinter's entries objects
    :return: number in decimal notation
    """
    input_data = entries.get_dec_num()

    if not is_dec_num_correct(input_data):
        raise e.RealEntryContentError(field=c.Real.DEC_NUM_INDEX,
                                      exception_type=c.Exceptions.TYPE_ERROR)
    input_data = replace_comma(input_data)
    dec_num = float(input_data)
    return dec_num


def get_real_format(entries, mantissa: int, exponent: int, save: bool) -> str:
    """
    :param entries: list of tkinter's entries objects
    :param mantissa: number of binary digits of the mantissa
    :param exponent: number of binary digits of the exponent
    :param save: is the first digit of the mantissa stored
    :return: number in real representation
    """

    real_format = entries.get_real_format()
    if not set(real_format).issubset({"0", "1"}) or real_format == "":  # If string include not only '0' and '1'
        raise e.RealEntryContentError(field=c.Real.FLOAT_FORMAT_INDEX,
                                      exception_type=c.Exceptions.TYPE_ERROR)
    sum_len = 1 + exponent + (1 if save else 0) + mantissa  # Length of real representation
    if len(real_format) != sum_len:
        raise e.RealEntryContentError(field=c.Real.FLOAT_FORMAT_INDEX,
                                      exception_type=c.Exceptions.RANGE_ERROR)
    return real_format


def copy_to_clipboard(entries, index):
    """
    Copy value from entry to clipboard by its index

    :param entries: list of tkinter's entries objects
    :param index - index of entry field
    """
    if index == c.Real.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == c.Real.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == c.Real.FLOAT_FORMAT_INDEX:
        pyperclip.copy(entries.get_real_format())
