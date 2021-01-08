import tkinter.messagebox as mb
from text import Exceptions


class Warning:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showwarning(self.title, self.message)


class Error:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showerror(self.title, self.message)


class Messageboxes:
    BinSizeTypeError = Error(title=Exceptions.bin_size.title,
                             message=Exceptions.bin_size.type_error)

    BinSizeValueError = Error(title=Exceptions.bin_size.title,
                              message=Exceptions.bin_size.value_error)

    DecNumTypeError = Error(title=Exceptions.dec_num.title,
                            message=Exceptions.dec_num.type_error)

    DecNumValueError = Error(title=Exceptions.dec_num.title,
                             message=Exceptions.dec_num.value_error)
