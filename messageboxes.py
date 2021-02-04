# Файл с классами messagebox-ов

import tkinter.messagebox as mb

from constants import Exceptions as ConstEx
from text import int_exceptions as intEx


class WarningMb:
    """Messagebox типа Warning"""

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showwarning(self.title, self.message)


class ErrorMb:
    """Messagebox типа Error"""

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showerror(self.title, self.message)


class ExceptionMb(ErrorMb, WarningMb):
    """Messagebox-ы самописных ошибок"""

    def __init__(self, exception):
        if exception.type == ConstEx.TYPE_ERROR:
            ErrorMb.__init__(self, title=intEx[exception.field].title,
                             message=intEx[exception.field].type_error)
        elif exception.type == ConstEx.RANGE_ERROR:
            ErrorMb.__init__(self, title=intEx[exception.field].title,
                             message=intEx[exception.field].range_error)
        elif exception.type == ConstEx.WARNING:
            WarningMb.__init__(self, title="", message="")
        else:
            raise Warning("Exception type error")