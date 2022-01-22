# File with phrases that are used in the application interface in Russian

from calculations import constants as constants

int_labels_text = ["Число двоичных разрядов",
                   "Число в десятичной с.с.",
                   "Число в двоичной с.с.",
                   "Прямой код числа",
                   "Обратный код числа",
                   "Дополнительный код числа"]

real_labels_text = ["Число двоичных разрядов\nдля мантиссы",
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
real_nums_text = "Вещественные числа"
number_only = "В данное поле можно ввести только число."
bin_only = "В данное поле можно ввести только число, состоящее из 0 и 1."
range_exceeding = "Значение выходит за границы диапазона, заданного числом двоичных разрядов."


def error_in_field(field):
    return f'Ошибка в поле "{field}".'


class ExceptionTexts:
    def __init__(self, field_name: str = "", type_error=number_only, range_error=range_exceeding):
        self.title = error_in_field(field_name)
        self.type_error = type_error
        self.range_error = range_error


class Exceptions:
    """
    Phrases for messageboxes
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __getitem__(self, key: str) -> str:
        return self.dictionary.get(key, "ERROR")


int_dict = {constants.Int.BIN_SIZE_INDEX: ExceptionTexts(int_labels_text[0]),
            constants.Int.DEC_NUM_INDEX: ExceptionTexts(int_labels_text[1]),
            constants.Int.BIN_NUM_INDEX: ExceptionTexts(int_labels_text[2],
                                                        type_error=bin_only),
            constants.Int.STR_CODE_INDEX: ExceptionTexts(int_labels_text[3],
                                                         type_error=bin_only),
            constants.Int.REV_CODE_INDEX: ExceptionTexts(int_labels_text[4],
                                                         type_error=bin_only),
            constants.Int.ADD_CODE_INDEX: ExceptionTexts(int_labels_text[5],
                                                         type_error=bin_only)}

real_dict = {constants.Real.MANTISSA_BIN_SIZE_INDEX: ExceptionTexts(real_labels_text[0]),
             constants.Real.EXPONENT_BIN_SIZE_INDEX: ExceptionTexts(real_labels_text[1]),
             constants.Real.DEC_NUM_INDEX: ExceptionTexts(real_labels_text[3]),
             constants.Real.FLOAT_FORMAT_INDEX: ExceptionTexts(real_labels_text[9],
                                                               type_error=bin_only)}

int_exceptions = Exceptions(int_dict)
real_exceptions = Exceptions(real_dict)
