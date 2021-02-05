# Файл с классами messagebox-ов

import tkinter.messagebox as mb

from constants import Exceptions as ConstEx
from exceptions import FloatEntryContentError as FloatError
from exceptions import IntEntryContentError as IntError
from text import int_exceptions, float_exceptions


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

    def __get_text_list(self, exception):
        """Возвращает нужный список фраз в зависимости от типа исключения"""
        if isinstance(exception, IntError):
            return int_exceptions
        elif isinstance(exception, FloatError):
            return float_exceptions
        else:
            raise Warning("Exception.exception_type error")

    def __init__(self, exception):
        text_list = self.__get_text_list(exception)

        if exception.exception_type == ConstEx.TYPE_ERROR:
            ErrorMb.__init__(self, title=text_list[exception.field].title,
                             message=text_list[exception.field].type_error)
        elif exception.exception_type == ConstEx.RANGE_ERROR:
            ErrorMb.__init__(self, title=text_list[exception.field].title,
                             message=text_list[exception.field].range_error)
        elif exception.exception_type == ConstEx.WARNING:
            WarningMb.__init__(self, title="", message="")
        else:
            raise Warning("Exception type error")
