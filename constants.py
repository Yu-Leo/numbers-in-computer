# Файл с константами для приложения

class Type:
    INT = 0
    FLOAT = 1


class Int:
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
