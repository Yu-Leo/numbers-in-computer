# Файл с фразами, которые задействованы в интерфейсе, на русском языке

import constants as c

int_labels_text = ["Число двоичных разрядов",
                   "Число в десятичной с.с.",
                   "Число в двоичной с.с.",
                   "Прямой код числа",
                   "Обратный код числа",
                   "Дополнительный код числа"]

float_labels_text = ["Число двоичных разрядов\nдля мантиссы",
                     "Число двоичных разрядов\nдля порядка",
                     "Хранить старший разряд\nмантиссы",
                     "Число в десятичной с.с.",
                     "Число в двоичной с.с.",
                     "Мантисса в двоичной с.с.",
                     "Порядок в десятичной с.с.",
                     "Характеристика\nв десятичной с.с.",
                     "Характеристика\nв двоичной с.с.",
                     "Формат с плавающей запятой"]

int_nums_text = "Целые числа"
float_nums_text = "Вещественные числа"
bin_only = "В данное поле можно ввести только число, состоящее из 0 и 1."


class ExceptionTexts:
    def __init__(self, field_name="",
                 type_error="В данное поле можно ввести только число.",
                 range_error="Значение выходит за границы диапазона, заданного числом двоичных разрядов."):
        self.title = f'Ошибка в поле "{field_name}".'
        self.type_error = type_error
        self.range_error = range_error


class IntExceptions:
    """Фразы для messagebox-ов при вызове соответствующих исключений"""

    def __init__(self):
        pass

    def __getitem__(self, key):
        dictionary = {c.Int.BIN_SIZE_INDEX: ExceptionTexts(int_labels_text[0]),
                      c.Int.DEC_NUM_INDEX: ExceptionTexts(int_labels_text[1]),
                      c.Int.BIN_NUM_INDEX: ExceptionTexts(int_labels_text[2],
                                                          type_error=bin_only),
                      c.Int.STR_CODE_INDEX: ExceptionTexts(int_labels_text[3],
                                                           type_error=bin_only),
                      c.Int.REV_CODE_INDEX: ExceptionTexts(int_labels_text[4],
                                                           type_error=bin_only),
                      c.Int.ADD_CODE_INDEX: ExceptionTexts(int_labels_text[5],
                                                           type_error=bin_only)}
        return dictionary.get(key, "ERROR")


int_exceptions = IntExceptions()
