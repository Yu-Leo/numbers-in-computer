# File with operation's functions for int mode (and function for copy values to clipboard)

import pyperclip  # Module for working with clipboard

import exceptions
import tkgui.messageboxes as mb
from calculations import config, constants as constants
from calculations.numbers_kits import IntKit
from tkgui.widgets import IntEntries


def calculate(entries: IntEntries):
    """
    Calculation in int mode with exceptions tracking

    :param entries: list of entries in int mode
    """

    try:
        int_calc(entries)
    except exceptions.IntEntryContentError as exception:
        if exception.field == constants.Int.BIN_SIZE_INDEX:
            mb.ExceptionMb(exception).show()
            entries.clear_all_except()

        elif exception.field == constants.Int.DEC_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            if exception.exception_type == constants.Exceptions.TYPE_ERROR:
                entries.clear_all_except(constants.Int.BIN_SIZE_INDEX)
            elif exception.exception_type == constants.Exceptions.WARNING:
                entries.clear_all_except(constants.Int.BIN_SIZE_INDEX, constants.Int.DEC_NUM_INDEX,
                                         constants.Int.BIN_NUM_INDEX)

        elif exception.field == constants.Int.BIN_NUM_INDEX:
            mb.ExceptionMb(exception).show()
            if exception.exception_type == constants.Exceptions.TYPE_ERROR:
                entries.clear_all_except(constants.Int.BIN_SIZE_INDEX)
            elif exception.exception_type == constants.Exceptions.WARNING:
                entries.clear_all_except(constants.Int.BIN_SIZE_INDEX, constants.Int.DEC_NUM_INDEX,
                                         constants.Int.BIN_NUM_INDEX)

        elif exception.field in (
                constants.Int.STR_CODE_INDEX, constants.Int.REV_CODE_INDEX, constants.Int.ADD_CODE_INDEX):
            mb.ExceptionMb(exception).show()
            entries.clear_all_except(constants.Int.BIN_SIZE_INDEX)

        else:
            raise Warning("exception.field Error")


def int_calc(entries: IntEntries):
    """
    Calculation in int mode

    :param entries: list of entries in int mode
    """

    bin_size = get_bin_size(entries)  # Number of binary digits

    entries.clear_all_except(constants.Int.BIN_SIZE_INDEX, config.translate_type)  # Delete old values

    if config.translate_type == constants.Int.DEC_NUM_INDEX:  # Source value - number in decimal notation
        dec_num = get_dec_num(entries)
        kit = IntKit(dec_num=dec_num)
        kit.by_dec_num(bin_size)
        entries.print(kit)

    elif config.translate_type == constants.Int.BIN_NUM_INDEX:  # Source value - number in binary notation
        bin_num = get_bin_num(entries)
        kit = IntKit(bin_num=bin_num)
        kit.by_bin_num(bin_size)
        entries.print(kit)
        # If it's impossible to calculate representations for a given number of binary digits
        if kit.codes_error():
            raise exceptions.BinNumValueCodesWarning

    elif config.translate_type == constants.Int.STR_CODE_INDEX:  # Source value - straight code of number
        str_code = get_str_code(entries, bin_size)
        kit = IntKit(str_code=str_code)
        kit.by_str_code(bin_size)
        entries.print(kit)

    elif config.translate_type == constants.Int.REV_CODE_INDEX:  # Source value - reverse code of number
        rev_code = get_rev_code(entries, bin_size)
        kit = IntKit(rev_code=rev_code)
        kit.by_rev_code(bin_size)
        entries.print(kit)

    elif config.translate_type == constants.Int.ADD_CODE_INDEX:  # Source value - additional code of number
        add_code = get_add_code(entries, bin_size)
        kit = IntKit(add_code=add_code)
        kit.by_add_code(bin_size)
        entries.print(kit)


def get_bin_size(entries: IntEntries) -> int:
    """
    :param entries: list of entries in int mode
    :return: number of binary digits for representations of number
    """

    str_bin_size = entries.get_bin_size()
    try:
        int_bin_size = int(str_bin_size)
    except ValueError:
        raise exceptions.IntEntryContentError(field=constants.Int.BIN_SIZE_INDEX,
                                              exception_type=constants.Exceptions.TYPE_ERROR)

    if not (constants.Int.MIN_BIN_SIZE <= int_bin_size <= constants.Int.MAX_BIN_SIZE):
        raise exceptions.IntEntryContentError(field=constants.Int.BIN_SIZE_INDEX,
                                              exception_type=constants.Exceptions.RANGE_ERROR)
    return int_bin_size


def get_dec_num(entries: IntEntries) -> int:
    """
    :param entries: list of entries in int mode
    :return: number in decimal notation
    """

    input_data = entries.get_dec_num()
    try:
        dec_num = int(input_data)
    except ValueError:
        raise exceptions.IntEntryContentError(field=constants.Int.DEC_NUM_INDEX,
                                              exception_type=constants.Exceptions.TYPE_ERROR)
    return dec_num


def get_bin_num(entries: IntEntries) -> str:
    """
    :param entries: list of entries in int mode
    :return: number in binary notation
    """

    bin_num = entries.get_bin_num()
    if set(bin_num) != {"0", "1"}:  # If string include not only '0' and '1'
        raise exceptions.IntEntryContentError(field=constants.Int.BIN_NUM_INDEX,
                                              exception_type=constants.Exceptions.TYPE_ERROR)
    return bin_num


def get_str_code(entries: IntEntries, bin_size: int) -> str:
    """
    :param entries: list of entries in int mode
    :param bin_size: number of binary digits for representations of number
    :return: number in straight code's representation
    """

    str_code = entries.get_str_code()
    if set(str_code) != {"0", "1"}:  # If string include not only '0' and '1'
        raise exceptions.IntEntryContentError(field=constants.Int.STR_CODE_INDEX,
                                              exception_type=constants.Exceptions.TYPE_ERROR)
    if len(str_code) != bin_size or bin_size < 2:
        raise exceptions.IntEntryContentError(field=constants.Int.STR_CODE_INDEX,
                                              exception_type=constants.Exceptions.RANGE_ERROR)
    return str_code


def get_rev_code(entries: IntEntries, bin_size: int) -> str:
    """
    :param entries: list of entries in int mode
    :param bin_size: number of binary digits for representations of number
    :return: number in reversed code's representation
    """

    rev_code = entries.get_rev_code()
    if set(rev_code) != {"0", "1"}:  # If string include not only '0' and '1'
        raise exceptions.IntEntryContentError(field=constants.Int.REV_CODE_INDEX,
                                              exception_type=constants.Exceptions.TYPE_ERROR)
    if len(rev_code) != bin_size or bin_size < 2:
        raise exceptions.IntEntryContentError(field=constants.Int.REV_CODE_INDEX,
                                              exception_type=constants.Exceptions.RANGE_ERROR)
    return rev_code


def get_add_code(entries: IntEntries, bin_size: int) -> str:
    """
    :param entries: list of entries in int mode
    :param bin_size: number of binary digits for representations of number
    :return: number in additional code's representation
    """

    add_code = entries.get_add_code()
    if set(add_code) != {"0", "1"}:  # If string include not only '0' and '1'
        raise exceptions.IntEntryContentError(field=constants.Int.ADD_CODE_INDEX,
                                              exception_type=constants.Exceptions.TYPE_ERROR)
    if len(add_code) != bin_size or bin_size < 2:
        raise exceptions.IntEntryContentError(field=constants.Int.ADD_CODE_INDEX,
                                              exception_type=constants.Exceptions.RANGE_ERROR)
    return add_code


def copy_to_clipboard(entries: IntEntries, index):
    """
    Copy value from entry to clipboard by its index

    :param entries: list of entries in int mode
    :param index - index of entry field
    """
    if index == constants.Int.DEC_NUM_INDEX:
        pyperclip.copy(entries.get_dec_num())
    elif index == constants.Int.BIN_NUM_INDEX:
        pyperclip.copy(entries.get_bin_num())
    elif index == constants.Int.STR_CODE_INDEX:
        pyperclip.copy(entries.get_str_code())
    elif index == constants.Int.REV_CODE_INDEX:
        pyperclip.copy(entries.get_rev_code())
    elif index == constants.Int.ADD_CODE_INDEX:
        pyperclip.copy(entries.get_add_code())
