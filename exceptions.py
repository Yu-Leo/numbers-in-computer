# Файл с исключениями


class EntryContentError(ValueError):
    """Недопустимые значения в полях ввода"""

    def __init__(self, field, category, message=""):
        self.field = field
        self.type = category
        self.text = message
