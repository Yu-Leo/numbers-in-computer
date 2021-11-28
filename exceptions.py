# File with application exceptions

class EntryContentError(ValueError):
    """Invalid values in entry fields"""

    def __init__(self, field, exception_type, message: str = ""):
        """
        :param field: field index
        :param exception_type:
        :param message: some comments
        """
        self.field = field
        self.exception_type = exception_type
        self.text = message


class IntEntryContentError(EntryContentError):
    def __init__(self, field, exception_type, message: str = ""):
        """
        :param field: field index
        :param exception_type:
        :param message: some comments
        """
        super().__init__(field, exception_type, message)


class FloatEntryContentError(EntryContentError):
    def __init__(self, field, exception_type, message: str = ""):
        """
        :param field: field index
        :param exception_type:
        :param message: some comments
        """
        super().__init__(field, exception_type, message)
