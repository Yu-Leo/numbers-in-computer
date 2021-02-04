# Файл с исключениями


class EntryContentError(ValueError):
    """Недопустимые значения в полях ввода"""

    def __init__(self, field, exception_type, message=""):
        self.field = field  # Индекс поля
        self.exception_type = exception_type  # Тип "некорректности"
        self.text = message  # Доп. сообщение


class IntEntryContentError(EntryContentError):
    def __init__(self, field, exception_type, message=""):
        super().__init__(field, exception_type, message)


class FloatEntryContentError(EntryContentError):
    def __init__(self, field, exception_type, message=""):
        super().__init__(field, exception_type, message)
