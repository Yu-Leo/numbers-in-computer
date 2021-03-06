# Файл с константами для приложения

class Int:
    TYPE_NUM = 0
    MIN_BIN_SIZE = 1  # Минимальное число двоичных разрядов
    MAX_BIN_SIZE = 100  # Максимальное число двоичных разрядов
    DEFAULT_BIN_SIZE = 8  # Число двоичных разрядов по умолчанию

    BIN_SIZE_INDEX = 0
    DEC_NUM_INDEX = 1
    BIN_NUM_INDEX = 2
    STR_CODE_INDEX = 3
    REV_CODE_INDEX = 4
    ADD_CODE_INDEX = 5

    NUMBER_OF_PARAMS = 6

    @staticmethod
    def max_positive(bin_size):
        """
        Максимальное положительное целое число, которое можно представить
        данным числом двоичных разрядов.
        """
        return 2 ** (bin_size - 1) - 1

    @staticmethod
    def max_negative(bin_size):
        """
        Максимальное отрицательное целое число, которое можно представить
        данным числом двоичных разрядов.
        """
        return -1 * (2 ** (bin_size - 1))


class Float:
    TYPE_NUM = 1

    MIN_MANT_BIN_SIZE = 1  # Минимальное число двоичных разрядов для мантиссы
    MAX_MANT_BIN_SIZE = 100  # Максимальное число двоичных разрядов для мантиссы

    MIN_ORD_BIN_SIZE = 1  # Минимальное число двоичных разрядов для порядка
    MAX_ORD_BIN_SIZE = 100  # Максимальное число двоичных разрядов для порядка

    MAX_FLOAT_SIZE = 10  # Максимальное кол-во знаков после запятой

    DEFAULT_MANTISSA_BIN_SIZE = 10  # Число двоичных разрядов для мантиссы по умолчанию
    DEFAULT_ORDER_BIN_SIZE = 5  # Число двоичных разрядов для порядка по умолчанию

    MANTISSA_BIN_SIZE_INDEX = 0
    ORDER_BIN_SIZE_INDEX = 1
    SAVE_FIRST_DIGIT_INDEX = 2
    DEC_NUM_INDEX = 3
    BIN_NUM_INDEX = 4
    BIN_MANTISSA_INDEX = 5
    DEC_ORDER_INDEX = 6
    DEC_CHARACTERISTIC_INDEX = 7
    BIN_CHARACTERISTIC_INDEX = 8
    FLOAT_FORMAT_INDEX = 9

    NUMBER_OF_PARAMS = 10


class Exceptions:
    TYPE_ERROR = 0
    RANGE_ERROR = 1
    WARNING = 2
