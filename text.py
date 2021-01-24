# Файл с фразами, которые задействованы в интерфейсе, на русском языке

int_labels_text = ["Число двоичных разрядов",
                   "Число в десятичной с.с.",
                   "Число в двоичной с.с.",
                   "Прямой код числа",
                   "Обратный код числа",
                   "Дополнительный код числа"]

int_nums_text = "Целые числа"
float_nums_text = "Вещественные числа"

entries_count = 6

buttons_text = ["Очистить"]


class ExceptionTexts:
    def __init__(self, field_name="",
                 type_error="Невозможно преобразовать в целое число.",
                 value_error="Значение выходит за границы диапазона, заданого числом двоичных разрядов."):
        self.title = f'Ошибка в поле "{field_name}".'
        self.type_error = type_error
        self.value_error = value_error


class Exceptions:
    """Фразы для messagebox-ов при вызове соответсвующих исключений"""
    bin_size = ExceptionTexts(field_name=int_labels_text[0])
    dec_num = ExceptionTexts(field_name=int_labels_text[1])
    bin_num = ExceptionTexts(field_name=int_labels_text[2])
    str_code = ExceptionTexts(field_name=int_labels_text[3])
    rev_code = ExceptionTexts(field_name=int_labels_text[4])
    add_code = ExceptionTexts(field_name=int_labels_text[5])
