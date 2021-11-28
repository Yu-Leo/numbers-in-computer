# File with phrases that are used in the application interface in Russian language

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
number_only = "В данное поле можно ввести только число."
bin_only = "В данное поле можно ввести только число, состоящее из 0 и 1."
range_exceeding = "Значение выходит за границы диапазона, заданного числом двоичных разрядов."


def error_in_field(field):
    return f'Ошибка в поле "{field}".'


class ExceptionTexts:
    def __init__(self, field_name="", type_error=number_only, range_error=range_exceeding):
        self.title = error_in_field(field_name)
        self.type_error = type_error
        self.range_error = range_error


class Exceptions:
    """
    Phrases for messageboxes
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __getitem__(self, key):
        return self.dictionary.get(key, "ERROR")


int_dict = {c.Int.BIN_SIZE_INDEX: ExceptionTexts(int_labels_text[0]),
            c.Int.DEC_NUM_INDEX: ExceptionTexts(int_labels_text[1]),
            c.Int.BIN_NUM_INDEX: ExceptionTexts(int_labels_text[2],
                                                type_error=bin_only),
            c.Int.STR_CODE_INDEX: ExceptionTexts(int_labels_text[3],
                                                 type_error=bin_only),
            c.Int.REV_CODE_INDEX: ExceptionTexts(int_labels_text[4],
                                                 type_error=bin_only),
            c.Int.ADD_CODE_INDEX: ExceptionTexts(int_labels_text[5],
                                                 type_error=bin_only)}

float_dict = {c.Float.MANTISSA_BIN_SIZE_INDEX: ExceptionTexts(float_labels_text[0]),
              c.Float.EXPONENT_BIN_SIZE_INDEX: ExceptionTexts(float_labels_text[1]),
              c.Float.DEC_NUM_INDEX: ExceptionTexts(float_labels_text[3]),
              c.Float.FLOAT_FORMAT_INDEX: ExceptionTexts(float_labels_text[9],
                                                         type_error=bin_only)}

int_exceptions = Exceptions(int_dict)
float_exceptions = Exceptions(float_dict)
