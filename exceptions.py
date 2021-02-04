# Файл с исключениями


class EntryContentError(ValueError):
    """Недопустимые значения в полях ввода"""

    def __init__(self, field, ex_type, message=""):
        self.field = field  # Индекс поля
        self.type = ex_type  # Тип "некорректности"
        self.text = message  # Доп. сообщение
