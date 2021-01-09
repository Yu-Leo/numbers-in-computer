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

    @staticmethod
    def MAX_POSITIVE(bin_size):
        """
        Максимальное положительное целое число, которое можно представить
        данным числом двоичных разрядов.
        """
        return 2 ** (bin_size - 1)

    @staticmethod
    def MAX_NEGATIVE(bin_size):
        """
        Максимальное отрицательное целое число, которое можно представить
        данным числом двоичных разрядов.
        """
        return -1 * (2 ** (bin_size - 1) - 1)
