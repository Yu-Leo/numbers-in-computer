# File with classes of messageboxes

import tkinter.messagebox as mb

import exceptions
from calculations.constants import Exceptions as ConstEx
from text_ru import int_exceptions, real_exceptions


class WarningMb:
    """
    Messagebox with type 'warning'
    """

    def __init__(self, title: str, message: str):
        self.title: str = title
        self.message: str = message

    def show(self):
        mb.showwarning(self.title, self.message)


class ErrorMb:
    """
    Messagebox with type 'error'
    """

    def __init__(self, title: str, message: str):
        self.title: str = title
        self.message: str = message

    def show(self):
        mb.showerror(self.title, self.message)


class ExceptionMb(ErrorMb, WarningMb):
    """
    Messagebox for custom exceptions
    """

    def __get_text_list(self, exception: exceptions.EntryContentError):
        """
        :param exception: exception's object which needs to be displayed
        :return: the desired list of phrases depending on the type of exception
        """
        if isinstance(exception, exceptions.IntEntryContentError):
            return int_exceptions
        elif isinstance(exception, exceptions.RealEntryContentError):
            return real_exceptions
        else:
            raise Warning("Exception.exception_type error")

    def __init__(self, exception: exceptions.EntryContentError):
        """
        :param exception: exception's object which needs to be displayed
        """
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
