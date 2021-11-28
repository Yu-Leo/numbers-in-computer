# File with classes of sets of numbers in various number systems and representations

import constants as c


class IntKit:
    def __init__(self, dec_num=0, bin_num="0", str_code="0", rev_code="0", add_code="0"):
        self.__dec_num = dec_num  # Number in decimal notation
        self.__bin_num = bin_num  # Number in binary notation
        self.__str_code = str_code  # Straight number's code
        self.__rev_code = rev_code  # Reverse number's code
        self.__add_code = add_code  # Additional number's code

    def __getitem__(self, key):
        kit_dict = {"dec_num": self.__dec_num,
                    "bin_num": self.__bin_num,
                    "str_code": self.__str_code,
                    "rev_code": self.__rev_code,
                    "add_code": self.__add_code}
        return kit_dict.get(key, "ERROR")

    def by_dec_num(self, bin_size):
        """
        :param bin_size: number of binary digits for representations of number
        Translation into all representations by number in decimal notation
        """
        if self.__dec_num >= 0:  # Positive number
            self.__bin_num = self.__abs_bin_by_dec()
            if self.__dec_num > c.Int.max_positive(bin_size):  # Out of range
                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX,
                                         c.Int.REV_CODE_INDEX,
                                         c.Int.ADD_CODE_INDEX)
            else:
                self.__str_code = self.__rev_code = self.__add_code = self.__straight_by_bin(bin_size)

        else:  # Negative number
            self.__abs_bin_num = self.__abs_bin_by_dec()
            self.__bin_num = self.__abs_bin_num if self.__dec_num > 0 else "-"
            if self.__dec_num < c.Int.max_negative(bin_size):  # Out of range
                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX,
                                         c.Int.REV_CODE_INDEX,
                                         c.Int.ADD_CODE_INDEX)
            elif self.__dec_num == c.Int.max_negative(bin_size):  # At the bexponent of the range
                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX, c.Int.REV_CODE_INDEX)
                self.__add_code = self.__get_add_for_lower_bound(bin_size)
            else:
                self.__str_code = self.__straight_by_bin(bin_size)
                self.__rev_code = self.__reversed_by_straight()
                self.__add_code = self.__additional_by_reversed()

    def by_bin_num(self, bin_size):
        """
        :param bin_size: number of binary digits for representations of number
        Translation into all representations by number in binary notation
        """
        self.__dec_num = int(self.__bin_num, base=2)
        self.by_dec_num(bin_size)

    def by_str_code(self, bin_size):
        """
        :param bin_size: number of binary digits for representations of number
        Translation into all representations by number's straight code
        """
        self.__bin_num = self.__bin_by_straight()
        self.by_bin_num(bin_size)

    def by_rev_code(self, bin_size):
        """
        :param bin_size: number of binary digits for representations of number
        Translation into all representations by number's reverse code
        """
        self.__str_code = self.__straight_by_reversed()
        self.by_str_code(bin_size)

    def by_add_code(self, bin_size):
        """
        :param bin_size: number of binary digits for representations of number
        Translation into all representations by number's additional code
        """
        self.__str_code = self.__straight_by_additional()
        self.by_str_code(bin_size)

    def codes_error(self):
        return self.__str_code == "-"

    def __fill_codes_errors(self, *args):
        if c.Int.STR_CODE_INDEX in args:
            self.__str_code = "-"
        if c.Int.REV_CODE_INDEX in args:
            self.__rev_code = "-"
        if c.Int.ADD_CODE_INDEX in args:
            self.__add_code = "-"

    def __abs_bin_by_dec(self):
        """
        :returns the modulus of a number in binary notation
        """
        return bin(abs(self.__dec_num))[2:]

    def __straight_by_bin(self, bin_size):
        """
        :param bin_size: number of binary digits for representations of number
        :return: straight code of number by its binary notation
        """
        if self.__dec_num >= 0:  # Positive number
            return self.__bin_num.rjust(bin_size, "0")
        return "1" + self.__abs_bin_num.rjust(bin_size - 1, "0")

    def __reversed_by_straight(self):
        """
        :return: reversed code of number by its straight code
        """
        if self.__str_code[0] == "0":  # Positive number
            return self.__str_code
        rev_code = self.__str_code[0]
        for i in range(1, len(self.__str_code)):
            rev_code += ("1" if self.__str_code[i] == "0" else "0")
        return rev_code

    def __additional_by_reversed(self):
        """
        :return: additional code of number by its reversed code
        """
        if self.__rev_code[0] == "0":  # Positive number
            return self.__rev_code
        return bin_sum(self.__rev_code, "1")

    def __bin_by_straight(self):
        """
        :return: binary notation of number by its straight code
        """
        sign = "-" if self.__str_code[0] == "1" else ""
        return sign + self.__str_code[1:]

    def __straight_by_reversed(self):
        """
        :return: straight code of number by its reversed code
        """
        if self.__rev_code[0] == "0":  # Positive number
            return self.__rev_code
        str_code = self.__rev_code[0]
        for i in range(1, len(self.__rev_code)):
            str_code += ("1" if self.__rev_code[i] == "0" else "0")
        return str_code

    def __straight_by_additional(self):
        """
        :return: straight code of number by its additional code
        """
        if self.__add_code[0] == "0":  # Positive number
            return self.__add_code
        str_code = self.__add_code[0]
        for i in range(1, len(self.__add_code)):
            str_code += ("1" if self.__add_code[i] == "0" else "0")
        return bin_sum(str_code, "1")

    def __get_add_for_lower_bound(self, bin_size):
        """
        :returns additional code of number that is the lower bound acceptable range
        """
        if bin_size == 1 and self.__dec_num == -1:  # A special case
            return "1"
        # Additional code = reverse code of number, witch smaller than this on 1 modulo
        one_less_by_abs = IntKit(dec_num=self.__dec_num + 1)
        one_less_by_abs.by_dec_num(bin_size)
        return one_less_by_abs.__rev_code


class FloatKit:

    @staticmethod
    def get_dec_parts(a: float):
        int_part = int(a)
        float_part = a - int_part
        return int_part, float_part

    @staticmethod
    def get_bin_float_part(dec_float_part):
        """
        :param dec_float_part: float part of number in decimal notation
        Translate float part of number from decimal notation into binary notation
        """
        if abs(dec_float_part - 0) <= 0.001:  # float part == 0
            return "0"
        res = ""
        while abs(dec_float_part - int(dec_float_part)) >= 0.001:
            dec_float_part *= 2
            res += str(int(dec_float_part))
            dec_float_part = dec_float_part - int(dec_float_part)

            if len(res) > c.Float.MAX_FLOAT_SIZE:
                break  # If the number of decimal places is greater than maximum
        return res

    @staticmethod
    def get_dec_float_part(bin_float_part):
        """
        :param bin_float_part: float part of number in binary notation
        Translate float part of number from binary notation into decimal notation
        """
        res = 0
        for i in range(len(bin_float_part)):
            res += int(bin_float_part[i]) * 2 ** (-(i + 1))
        return res

    def __init__(self, dec_num=0.0, bin_num="0", float_format="0"):
        self.__dec_num = dec_num  # Number in decimal notation
        self.__bin_num = bin_num  # Number in binary notation
        self.__bin_mantissa = "0"
        self.__dec_exponent = 0
        self.__dec_characteristic = "0"
        self.__bin_characteristic = "0"
        self.__float_format = float_format
        self.__sign = "0"

    def __getitem__(self, key):
        kit_dict = {"dec_num": self.__dec_num,
                    "bin_num": self.__bin_num,
                    "bin_mantissa": self.__bin_mantissa,
                    "dec_exponent": self.__dec_exponent,
                    "dec_characteristic": self.__dec_characteristic,
                    "bin_characteristic": self.__bin_characteristic,
                    "float_format": self.__float_format}
        return kit_dict.get(key, "ERROR")

    def by_dec_num(self, mantissa_bin_size, exponent_bin_size, save_first_digit):
        self.__sign = ("1" if self.__dec_num < 0 else "0")
        dec_int_part, dec_float_part = FloatKit.get_dec_parts(abs(self.__dec_num))
        bin_int_part = ("-" if self.__sign == "1" else "") + bin(dec_int_part)[2:]
        bin_float_part = FloatKit.get_bin_float_part(dec_float_part)
        self.__bin_num = bin_int_part + "." + bin_float_part
        self.__bin_mantissa, self.__dec_exponent = self.__get_mantissa_and_exponent_by_bin()
        self.__dec_characteristic = self.__dec_exponent + mantissa_bin_size + exponent_bin_size
        self.__bin_characteristic = str(bin(self.__dec_characteristic)[2:].rjust(exponent_bin_size, "0"))
        self.__float_format = self.__get_float_format_by_all(mantissa_bin_size, exponent_bin_size, save_first_digit)

    def by_float_format(self, mantissa_bin_size, exponent_bin_size, save_first_digit):
        self.__sign = self.__float_format[0]
        self.__bin_characteristic = self.__float_format[1:exponent_bin_size + 1]
        self.__dec_characteristic = int(self.__bin_characteristic, base=2)
        self.__dec_exponent = self.__dec_characteristic - (mantissa_bin_size + exponent_bin_size)
        self.__bin_mantissa = self.__get_mantissa_by_float(exponent_bin_size, save_first_digit)
        self.__bin_num = self.__get_bin_by_mantissa()
        self.__dec_num = self.__get_dec_by_bin()

    def __get_mantissa_and_exponent_by_bin(self):
        bin_num = self.__bin_num
        sign = "-" if self.__sign == "1" else ""
        if self.__sign == "1":
            bin_num = bin_num[1:]
        dot_pos = bin_num.find(".")
        bin_num = bin_num[:dot_pos] + bin_num[dot_pos + 1:]
        if bin_num[0] == "1":
            return (sign + "1." + bin_num[1:]).rstrip("0"), dot_pos - 1
        elif bin_num[0] == "0":
            one_pos = bin_num.find("1")
            mant = bin_num[:one_pos + 1] + "." + bin_num[one_pos + 1:]
            mant = mant.lstrip("0")
            mant = mant.ljust(4, "0")
            return sign + mant, -one_pos

    def __get_float_format_by_all(self, mant_size, exponent_size, save):
        sign = self.__sign
        exponent = self.__bin_characteristic
        first_digit = "1" if save else ""
        if sign == "1":
            mantissa = self.__bin_mantissa[3:]
        else:
            mantissa = self.__bin_mantissa[2:]
        res = sign + exponent + first_digit + mantissa
        sum_size = 1 + mant_size + (1 if save else 0) + exponent_size
        return res.ljust(sum_size, "0")[:sum_size]

    def __get_mantissa_by_float(self, exponent_bin_size, save_first_digit):
        float_mantissa = self.__float_format[exponent_bin_size + 1:].rstrip("0")
        if save_first_digit:
            mant = ("1." + float_mantissa[1:]).ljust(4, "0")
        else:
            mant = ("1." + float_mantissa).ljust(4, "0")
        if self.__sign == "1":
            return "-" + mant
        else:
            return mant

    def __get_bin_by_mantissa(self):
        exponent = self.__dec_exponent
        sign = "-" if self.__sign == "1" else ""
        dot_pos = self.__bin_mantissa.find(".")
        full_mantissa = self.__bin_mantissa[:dot_pos] + self.__bin_mantissa[dot_pos + 1:]
        if self.__sign == "1":
            full_mantissa = full_mantissa[1:]
        if exponent >= 0:
            dot_pos = 1 + exponent
            full_mantissa = full_mantissa.ljust(dot_pos + 1, "0")
            left_part = full_mantissa[:dot_pos]
            right_part = full_mantissa[dot_pos:]
            return sign + left_part + "." + right_part
        else:
            full_mantissa = ("0" * abs(exponent)) + full_mantissa
            return sign + full_mantissa[0] + "." + full_mantissa[1:]

    def __get_dec_by_bin(self):
        if self.__bin_num[0] == "-":
            sign = -1
            bin_num = self.__bin_num[1:]
        else:
            sign = 1
            bin_num = self.__bin_num
        dot_pos = bin_num.find(".")

        bin_int_part = bin_num[:dot_pos]
        bin_float_part = bin_num[dot_pos + 1:]
        dec_int_past = int(bin_int_part, base=2)
        dec_float_part = FloatKit.get_dec_float_part(bin_float_part)
        return sign * (dec_int_past + dec_float_part)


def bin_sum(a, b):
    """
    Addition of two numbers in binary system
    """
    add_digit = False
    n = max(len(a), len(b))
    a = a.rjust(n, "0")
    b = b.rjust(n, "0")
    res = a
    for i in range(n - 1, 0, -1):
        if a[i] != b[i]:
            if add_digit:
                res = res[:i] + "0" + res[i + 1:]
            else:
                res = res[:i] + "1" + res[i + 1:]
        else:
            if add_digit:
                res = res[:i] + "1" + res[i + 1:]
            else:
                res = res[:i] + "0" + res[i + 1:]
            add_digit = a[i] == "1"
    if add_digit:
        res = "1" + res
    return res
