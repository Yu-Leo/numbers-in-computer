# Файл с messagebox-ами

import tkinter.messagebox as mb
from text import Exceptions


class Warning:
    """Мessagebox типа Warning"""

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showwarning(self.title, self.message)


class Error:
    """Мessagebox типа Error"""

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showerror(self.title, self.message)


class Messageboxes:
    """Мessagebox-ы самописных ошибок"""
    BinSizeTypeError = Error(title=Exceptions.bin_size.title,
                             message=Exceptions.bin_size.type_error)

    BinSizeValueError = Error(title=Exceptions.bin_size.title,
                              message=Exceptions.bin_size.value_error)

    DecNumTypeError = Error(title=Exceptions.dec_num.title,
                            message=Exceptions.dec_num.type_error)

    DecNumValueCodesWarning = Warning(title=Exceptions.dec_num.title,
                                      message=Exceptions.dec_num.value_error)

    BinNumTypeError = Error(title=Exceptions.bin_num.title,
                            message=Exceptions.bin_num.type_error)

    BinNumValueCodesWarning = Warning(title=Exceptions.bin_num.title,
                                      message=Exceptions.bin_num.value_error)

    StrCodeTypeError = Error(title=Exceptions.str_code.title,
                             message=Exceptions.str_code.type_error)

    StrCodeValueError = Error(title=Exceptions.str_code.title,
                              message=Exceptions.str_code.value_error)
