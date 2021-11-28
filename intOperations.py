# File with operation's functions for int mode (and function for copy values to clipboard)

import pyperclip  # Module for working with clipboard

import config
import constants as c
import exceptions as e
import messageboxes as mb
from numbersKits import IntKit


def calculate(entries):
    """
    Calculation in int mode with exceptions tracking

    :param entries: list of tkinter's entries objects
    """

    try:
        int_calc(entries)
    except e.IntEntryContentError as exception:
        if exception.field == c.Int.BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except()

        elif exception.field == c.Int.DEC_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            if exception.exception_type == c.Exceptions.TYPE_ERROR:
                entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
            elif exception.exception_type == c.Exceptions.WARNING:
                entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX,
                                         c.Int.BIN_NUM_INDEX)

        elif exception.field == c.Int.BIN_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            if exception.exception_type == c.Exceptions.TYPE_ERROR:
                entries.clear_all_except(c.Int.BIN_SIZE_INDEX)
            elif exception.exception_type == c.Exceptions.WARNING:
                entries.clear_all_except(c.Int.BIN_SIZE_INDEX, c.Int.DEC_NUM_INDEX,
                                         c.Int.BIN_NUM_INDEX)

        elif exception.field in (c.Int.STR_CODE_INDEX, c.Int.REV_CODE_INDEX, c.Int.ADD_CODE_INDEX):
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(c.Int.BIN_SIZE_INDEX)

        else:
            raise Warning("exception.field Error")


def int_calc(entries):
    """
    Calculation in int mode

    :param entries: list of tkinter's entries objects
    """

    bin_size = get_bin_size(entries)  # Number of binary digits
    # Delete old values
    entries.clear_all_except(c.Int.BIN_SIZE_INDEX, config.translate_type)

    if config.translate_type == c.Int.DEC_NUM_INDEX:  # Source value - number in decimal notation
        dec_num = get_dec_num(entries)
        kit = IntKit(dec_num=dec_num)
        kit.by_dec_num(bin_size)
        entries.print(kit)

    elif config.translate_type == c.Int.BIN_NUM_INDEX:  # Source value - number in binary notation
        bin_num = get_bin_num(entries)
        kit = IntKit(bin_num=bin_num)
        kit.by_bin_num(bin_size)
        entries.print(kit)
        # If it's impossible to calculate representations for a given number of binary digits
        if kit.codes_error():
            raise e.BinNumValueCodesWarning

    elif config.translate_type == c.Int.STR_CODE_INDEX:  # Source value - straight code of number
        str_code = get_str_code(entries, bin_size)
        kit = IntKit(str_code=str_code)
        kit.by_str_code(bin_size)
        entries.print(kit)

    elif config.translate_type == c.Int.REV_CODE_INDEX:  # Source value - reverse code of number
        rev_code = get_rev_code(entries, bin_size)
        kit = IntKit(rev_code=rev_code)
        kit.by_rev_code(bin_size)
        entries.print(kit)

    elif config.translate_type == c.Int.ADD_CODE_INDEX:  # Source value - additional code of number
        add_code = get_add_code(entries, bin_size)
        kit = IntKit(add_code=add_code)
        kit.by_add_code(bin_size)
        entries.print(kit)


def get_bin_size(entries):
    """
    :param entries: list of tkinter's entries objects
    :return: number of binary digits for representations of number in integer type
    """

    str_bin_size = entries.get_bin_size()
    try:
        int_bin_size = int(str_bin_size)
    except ValueError:
        raise e.IntEntryContentError(field=c.Int.BIN_SIZE_INDEX,
                                     exception_type=c.Exceptions.TYPE_ERROR)

    if not (c.Int.MIN_BIN_SIZE <= int_bin_size <= c.Int.MAX_BIN_SIZE):
        raise e.IntEntryContentError(field=c.Int.BIN_SIZE_INDEX,
                                     exception_type=c.Exceptions.RANGE_ERROR)
    return int_bin_size


def get_dec_num(entries):
    """
    :param entries: list of tkinter's entries objects
    :return: number in decimal notation in integer type
    """

    input_data = entries.get_dec_num()
    try:
        dec_num = int(input_data)
    except ValueError:
        raise e.IntEntryContentError(field=c.Int.DEC_NUM_INDEX,
                                     exception_type=c.Exceptions.TYPE_ERROR)
    return dec_num


def get_bin_num(entries):
    """
    :param entries: list of tkinter's entries objects
    :return: number in binary notation
    """

    bin_num = entries.get_bin_num()
    if set(bin_num) != {"0", "1"}:  # If string include not only '0' and '1'
        raise e.IntEntryContentError(field=c.Int.BIN_NUM_INDEX,
                                     exception_type=c.Exceptions.TYPE_ERROR)
    return bin_num


def get_str_code(entries, bin_size):
    """
    :param entries: list of tkinter's entries objects
    :param bin_size: number of binary digits for representations of number
    :return: number in straight code's representation
    """

    str_code = entries.get_str_code()
    if set(str_code) != {"0", "1"}:  # If string include not only '0' and '1'
        raise e.IntEntryContentError(field=c.Int.STR_CODE_INDEX,
                                     exception_type=c.Exceptions.TYPE_ERROR)
    if len(str_code) != bin_size or bin_size < 2:
        raise e.IntEntryContentError(field=c.Int.STR_CODE_INDEX,
                                     exception_type=c.Exceptions.RANGE_ERROR)
    return str_code


def get_rev_code(entries, bin_size):
    """
    :param entries: list of tkinter's entries objects
    :param bin_size: number of binary digits for representations of number
    :return: number in reversed code's representation
    """

    rev_code = entries.get_rev_code()
    if set(rev_code) != {"0", "1"}:  # If string include not only '0' and '1'
        raise e.IntEntryContentError(field=c.Int.REV_CODE_INDEX,
                                     exception_type=c.Exceptions.TYPE_ERROR)
    if len(rev_code) != bin_size or bin_size < 2:
        raise e.IntEntryContentError(field=c.Int.REV_CODE_INDEX,
                                     exception_type=c.Exceptions.RANGE_ERROR)
    return rev_code


def get_add_code(entries, bin_size):
    """
    :param entries: list of tkinter's entries objects
    :param bin_size: number of binary digits for representations of number
    :return: number in additional code's representation
    """

    add_code = entries.get_add_code()
    if set(add_code) != {"0", "1"}:  # If string include not only '0' and '1'
        raise e.IntEntryContentError(field=c.Int.ADD_CODE_INDEX,
                                     exception_type=c.Exceptions.TYPE_ERROR)
    if len(add_code) != bin_size or bin_size < 2:
        raise e.IntEntryContentError(field=c.Int.ADD_CODE_INDEX,
                                     exception_type=c.Exceptions.RANGE_ERROR)
    return add_code


def copy_to_buffer(entries, index):
    """
    Copy value from entry to clipboard by its index
    :param entries: list of tkinter's entries objects
    :param index - index of entry field
    """
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
