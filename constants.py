# File with application constant

class Int:
    TYPE_NUM = 0
    MIN_BIN_SIZE = 1  # Minimum number of binary digits
    MAX_BIN_SIZE = 100  # Maximum number of binary digits
    DEFAULT_BIN_SIZE = 8  # Default binary digits number

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
        :param bin_size: number of binary digits
        :returns: the maximum positive integer that can be represented
        the given number of binary digits.
        """
        return 2 ** (bin_size - 1) - 1

    @staticmethod
    def max_negative(bin_size):
        """
        :param bin_size: number of binary digits
        :returns: the maximum negative integer that can be represented
        the given number of binary digits.
        """
        return -1 * (2 ** (bin_size - 1))


class Float:
    TYPE_NUM = 1

    MIN_MANT_BIN_SIZE = 1  # Minimum number of binary digits for mantissa
    MAX_MANT_BIN_SIZE = 100  # Maximum number of binary digits for mantissa

    MIN_ORD_BIN_SIZE = 1  # Minimum number of binary digits for exponent
    MAX_ORD_BIN_SIZE = 100  # Maximum number of binary digits for exponent

    MAX_FLOAT_SIZE = 10  # Maximum number of decimal places

    DEFAULT_MANTISSA_BIN_SIZE = 10  # Default number of binary digits for mantissa
    DEFAULT_ORDER_BIN_SIZE = 5  # Default number of binary digits for exponent

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
