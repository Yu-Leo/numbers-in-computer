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
    def __init__(self, field_name="",
                 type_error="Невозможно преобразовать в целое число.",
                 value_error="Значение выходит за границы диапазона, заданого числом двоичных разрядов."):
        self.title = f'Ошибка в поле "{field_name}".'
        self.type_error = type_error
        self.value_error = value_error


class Exceptions:
    """Фразы для messagebox-ов при вызове соответсвующих исключений"""
    bin_size = ExceptionTexts(field_name='Число двоичных разрядов')
    dec_num = ExceptionTexts(field_name='Число (10)')
    bin_num = ExceptionTexts(field_name='Число (2)')
    str_code = ExceptionTexts(field_name='Прямой код числа')
    rev_code = ExceptionTexts(field_name='Обратный код числа')
    add_code = ExceptionTexts(field_name='Дополнительный код числа')
