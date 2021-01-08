# Файл с фразами, которые задействованны в интрефейсе, на русском языке

int_labels_text = ["Число двоичных разрядов:",
                   "Число (10):",
                   "Число (2):",
                   "Прямой код числа:",
                   "Обратный код числа",
                   "Дополнительный код числа"]

int_nums_text = "Целые числа"
float_nums_text = "Вещественные числа"

entries_count = 6

buttons_text = ["Очистить", "Рассчитать"]


class ExceptionTexts:
    def __init__(self, title="", type_error="", value_error=""):
        self.title = title
        self.type_error = type_error
        self.value_error = value_error


class Exceptions:
    """Фразы для messagebox-ов при вызове соответсвующих исключений"""
    bin_size = ExceptionTexts(title='Ошибка в поле "Число двоичных разрядов".',
                              type_error='Невозможно преобразовать в целое число.',
                              value_error='Значение выходит за границы заданного диапазона.')

    dec_num = ExceptionTexts(title='Ошибка в поле "Число (10)".',
                             type_error='Невозможно преобразовать в целое число.',
                             value_error='Значение выходит за границы диапазона, заданого числом двоичных разрядов.')
