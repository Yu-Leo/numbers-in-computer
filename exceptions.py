# File with application exceptions

class EntryContentError(ValueError):
    """Invalid values in entry fields"""

    def __init__(self, field, exception_type, message=""):
        self.field = field  # Field index
        self.exception_type = exception_type
        self.text = message  # Some comments


class IntEntryContentError(EntryContentError):
    def __init__(self, field, exception_type, message=""):
        super().__init__(field, exception_type, message)


class FloatEntryContentError(EntryContentError):
    def __init__(self, field, exception_type, message=""):
        super().__init__(field, exception_type, message)
