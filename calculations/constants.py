# File with application constant

class Int:
    """
    Constants for int mode
    """

    TYPE_NUM = 0
    MIN_BIN_SIZE = 1  # Minimum number of binary digits
    MAX_BIN_SIZE = 100  # Maximum number of binary digits
    DEFAULT_BIN_SIZE = 8  # Default binary digits number

    BIN_SIZE_INDEX = 0  # Index of field 'bin size'
    DEC_NUM_INDEX = 1  # Index of field 'dec num'
    BIN_NUM_INDEX = 2  # Index of field 'bin num'
    STR_CODE_INDEX = 3  # Index of field 'str code'
    REV_CODE_INDEX = 4  # Index of field 'rev code'
    ADD_CODE_INDEX = 5  # Index of field 'add code'

    NUMBER_OF_PARAMS = 6

    @staticmethod
    def max_positive(bin_size: int) -> int:
        """
        :param bin_size: number of binary digits
        :return: the maximum positive integer that can be represented the given number of binary digits.
        """
        return 2 ** (bin_size - 1) - 1

    @staticmethod
    def max_negative(bin_size: int) -> int:
        """
        :param bin_size: number of binary digits
        :return: the maximum negative integer that can be represented the given number of binary digits.
        """
        return -1 * (2 ** (bin_size - 1))


class Real:
    """
    Constants for real mode
    """

    TYPE_NUM = 1

    MIN_MANT_BIN_SIZE = 1  # Minimum number of binary digits for mantissa
    MAX_MANT_BIN_SIZE = 100  # Maximum number of binary digits for mantissa

    MIN_EXP_BIN_SIZE = 1  # Minimum number of binary digits for exponent
    MAX_EXP_BIN_SIZE = 100  # Maximum number of binary digits for exponent

    MAX_FLOAT_SIZE = 10  # Maximum number of decimal places

    DEFAULT_MANTISSA_BIN_SIZE = 10  # Default number of binary digits for mantissa
    DEFAULT_EXPONENT_BIN_SIZE = 5  # Default number of binary digits for exponent

    MANTISSA_BIN_SIZE_INDEX = 0  # Index of field 'mantissa bin size'
    EXPONENT_BIN_SIZE_INDEX = 1  # Index of field 'exponent bin size'
    SAVE_FIRST_DIGIT_INDEX = 2  # Index of checkbox 'save first digit'
    DEC_NUM_INDEX = 3  # Index of field 'dec num'
    BIN_NUM_INDEX = 4  # Index of field 'bin num'
    BIN_MANTISSA_INDEX = 5  # Index of field 'bin mantissa'
    DEC_EXPONENT_INDEX = 6  # Index of field 'dec exponent'
    DEC_CHARACTERISTIC_INDEX = 7  # Index of field 'dec characteristic'
    BIN_CHARACTERISTIC_INDEX = 8  # Index of field 'bin characteristic'
    FLOAT_FORMAT_INDEX = 9  # Index of field 'float format'

    NUMBER_OF_PARAMS = 10


class Exceptions:
    """
    Constants for exceptions
    """
    
    TYPE_ERROR = 0
    RANGE_ERROR = 1
    WARNING = 2
