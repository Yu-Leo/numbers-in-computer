# Файл с исключениями


class EntryContentError(ValueError):
    """Недопустимые значения в полях ввода"""

    def __init__(self, field, category, message=""):
        self.field = field  # Индекс поля
        self.type = category  # Тип "некорректности"
        self.text = message  # Доп. сообщение