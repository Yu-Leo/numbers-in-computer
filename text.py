# Файл с фразами, которые задействованы в интерфейсе, на русском языке

int_labels_text = ["Число двоичных разрядов",
                   "Число в десятичной с.с.",
                   "Число в двоичной с.с.",
                   "Прямой код числа",
                   "Обратный код числа",
                   "Дополнительный код числа"]

float_labels_text = ["Число двоичных разрядов\nдля мантиссы",
                     "Число двоичных разрядов\nдля порядка",
                     "Хранить старший разряд мантиссы",
                     "Число в десятичной с.с.",
                     "Число в двоичной с.с.",
                     "Мантисса в двоичной с.с.",
                     "Порядок в десятичной с.с.",
                     "Характеристика в десятичной с.с.",
                     "Характеристика в двоичной с.с.",
                     "Формат с плавающей запятой"]

int_nums_text = "Целые числа"
float_nums_text = "Вещественные числа"


class ExceptionTexts:
    def __init__(self, field_name="",
                 type_error="В данное поле можно ввести только число.",
                 value_error="Значение выходит за границы диапазона, заданного числом двоичных разрядов."):
        self.title = f'Ошибка в поле "{field_name}".'
        self.type_error = type_error
        self.value_error = value_error


class Exceptions:
    """Фразы для messagebox-ов при вызове соответствующих исключений"""
    bin_size = ExceptionTexts(field_name=int_labels_text[0])
    dec_num = ExceptionTexts(field_name=int_labels_text[1])
    bin_num = ExceptionTexts(type_error="В данное поле можно ввести только число, состоящее из 0 и 1.",
                             field_name=int_labels_text[2])
    str_code = ExceptionTexts(type_error="В данное поле можно ввести только число, состоящее из 0 и 1.",
                              field_name=int_labels_text[3])
    rev_code = ExceptionTexts(type_error="В данное поле можно ввести только число, состоящее из 0 и 1.",
                              field_name=int_labels_text[4])
    add_code = ExceptionTexts(type_error="В данное поле можно ввести только число, состоящее из 0 и 1.",
                              field_name=int_labels_text[5])
