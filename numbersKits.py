# Файл с классами наборов чисел в различных системах счисления и представлениях

import constants as c


class IntKit:
    def __init__(self, dec_num=0, bin_num="0", str_code="0", rev_code="0", add_code="0"):
        self.__dec_num = dec_num  # Число в 10й сс
        self.__bin_num = bin_num  # Число в 2й сс
        self.__str_code = str_code  # Прямой код числа
        self.__rev_code = rev_code  # Обратный код числа
        self.__add_code = add_code  # Дополнительный код числа

    def __getitem__(self, key):
        kit_dict = {"dec_num": self.__dec_num,
                    "bin_num": self.__bin_num,
                    "str_code": self.__str_code,
                    "rev_code": self.__rev_code,
                    "add_code": self.__add_code}
        return kit_dict.get(key, "ERROR")

    def by_dec_num(self, bin_size):
        """Перевод во все представления по числу в 10й сс"""
        if self.__dec_num >= 0:  # Положительное число
            self.__bin_num = self.__abs_bin_by_dec()
            if self.__dec_num > c.Int.max_positive(bin_size):  # Вне допустимого диапазона
                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX,
                                         c.Int.REV_CODE_INDEX,
                                         c.Int.ADD_CODE_INDEX)
            else:
                self.__str_code = self.__rev_code = self.__add_code = self.__straight_by_bin(bin_size)

        else:  # Отрицательное число
            self.__abs_bin_num = self.__abs_bin_by_dec()
            self.__bin_num = self.__abs_bin_num if self.__dec_num > 0 else "-"
            if self.__dec_num < c.Int.max_negative(bin_size):  # Вне допустимого диапазона
                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX,
                                         c.Int.REV_CODE_INDEX,
                                         c.Int.ADD_CODE_INDEX)
            elif self.__dec_num == c.Int.max_negative(bin_size):  # На границе диапазона
                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX, c.Int.REV_CODE_INDEX)
                self.__add_code = self.__get_add_for_lower_bound(bin_size)
            else:
                self.__str_code = self.__straight_by_bin(bin_size)
                self.__rev_code = self.__reversed_by_straight()
                self.__add_code = self.__additional_by_reversed()

    def by_bin_num(self, bin_size):
        """Перевод во все представления по числу в 2й сс"""
        self.__dec_num = int(self.__bin_num, base=2)
        self.by_dec_num(bin_size)

    def by_str_code(self, bin_size):
        """Перевод во все представления по прямому коду числа"""
        self.__bin_num = self.__bin_by_straight()
        self.by_bin_num(bin_size)

    def by_rev_code(self, bin_size):
        """Перевод во все представления по обратному коду числа"""
        self.__str_code = self.__straight_by_reversed()
        self.by_str_code(bin_size)

    def by_add_code(self, bin_size):
        """Перевод во все представления по дополнительному коду числа"""
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
        """Модуль числа в двоичной с.с."""
        return bin(abs(self.__dec_num))[2:]

    def __straight_by_bin(self, bin_size):
        if self.__dec_num >= 0:  # Положительное число
            return self.__bin_num.rjust(bin_size, "0")
        return "1" + self.__abs_bin_num.rjust(bin_size - 1, "0")

    def __reversed_by_straight(self):
        if self.__str_code[0] == "0":  # Положительное число
            return self.__str_code
        rev_code = self.__str_code[0]
        for i in range(1, len(self.__str_code)):
            rev_code += ("1" if self.__str_code[i] == "0" else "0")
        return rev_code

    def __additional_by_reversed(self):
        if self.__rev_code[0] == "0":  # Положительное число
            return self.__rev_code
        return bin_sum(self.__rev_code, "1")

    def __bin_by_straight(self):
        sign = "-" if self.__str_code[0] == "1" else ""
        return sign + self.__str_code[1:]

    def __straight_by_reversed(self):
        if self.__rev_code[0] == "0":  # Положительное число
            return self.__rev_code
        str_code = self.__rev_code[0]
        for i in range(1, len(self.__rev_code)):
            str_code += ("1" if self.__rev_code[i] == "0" else "0")
        return str_code

    def __straight_by_additional(self):
        if self.__add_code[0] == "0":  # Положительное число
            return self.__add_code
        str_code = self.__add_code[0]
        for i in range(1, len(self.__add_code)):
            str_code += ("1" if self.__add_code[i] == "0" else "0")
        return bin_sum(str_code, "1")

    def __get_add_for_lower_bound(self, bin_size):
        """
        Возвращает доп. код для числа, которое является нижней границей
        допустимого диапазона.
        """
        if bin_size == 1 and self.__dec_num == -1:  # Частный случай
            return "1"
        # Доп. код = обратный код числа, меньшего данного на 1 по модулю
        one_less_by_abs = IntKit(dec_num=self.__dec_num + 1)
        one_less_by_abs.by_dec_num(bin_size)
        return one_less_by_abs.__rev_code


class FloatKit:

    @staticmethod
    def get_dec_parts(a: float):
        """Возвращает целую в вещ. части числа в десятичной с. с."""
        int_part = int(a)
        float_part = a - int_part
        return int_part, float_part

    @staticmethod
    def get_bin_float_part(dec_float_part):
        """Перевод вещественной части числа из десятичной с.с. в двоичную"""
        if abs(dec_float_part - 0) <= 0.001:  # Дробная часть == 0
            return "0"
        res = ""
        while abs(dec_float_part - int(dec_float_part)) >= 0.001:
            dec_float_part *= 2
            res += str(int(dec_float_part))
            dec_float_part = dec_float_part - int(dec_float_part)

            if len(res) > c.Float.MAX_FLOAT_SIZE:
                break  # Если кол-во знаков после запятой больше, чем max
        return res

    @staticmethod
    def get_dec_float_part(bin_float_part):
        """Перевод вещественной части числа из двоичной с.с. в десятичную"""
        res = 0
        for i in range(len(bin_float_part)):
            res += int(bin_float_part[i]) * 2 ** (-(i + 1))
        return res

    def __init__(self, dec_num=0.0, bin_num="0", float_format="0"):
        self.__dec_num = dec_num  # Число в 10й сс
        self.__bin_num = bin_num  # Число в 2й сс
        self.__bin_mantissa = "0"
        self.__dec_order = 0
        self.__dec_characteristic = "0"
        self.__bin_characteristic = "0"
        self.__float_format = float_format
        self.__sign = "0"

    def __getitem__(self, key):
        kit_dict = {"dec_num": self.__dec_num,
                    "bin_num": self.__bin_num,
                    "bin_mantissa": self.__bin_mantissa,
                    "dec_order": self.__dec_order,
                    "dec_characteristic": self.__dec_characteristic,
                    "bin_characteristic": self.__bin_characteristic,
                    "float_format": self.__float_format}
        return kit_dict.get(key, "ERROR")

    def by_dec_num(self, mantissa_bin_size, order_bin_size, save_first_digit):
        """Расчёт по числу в десятичной с. с."""
        self.__sign = ("1" if self.__dec_num < 0 else "0")
        dec_int_part, dec_float_part = FloatKit.get_dec_parts(abs(self.__dec_num))
        bin_int_part = ("-" if self.__sign == "1" else "") + bin(dec_int_part)[2:]
        bin_float_part = FloatKit.get_bin_float_part(dec_float_part)
        self.__bin_num = bin_int_part + "." + bin_float_part
        self.__bin_mantissa, self.__dec_order = self.__get_mantissa_and_order_by_bin()
        self.__dec_characteristic = self.__dec_order + mantissa_bin_size + order_bin_size
        self.__bin_characteristic = str(bin(self.__dec_characteristic)[2:].rjust(order_bin_size, "0"))
        self.__float_format = self.__get_float_format_by_all(mantissa_bin_size, order_bin_size, save_first_digit)

    def by_float_format(self, mantissa_bin_size, order_bin_size, save_first_digit):
        """Расчёт по числу в Формате с плавающей запятой"""
        self.__sign = self.__float_format[0]
        self.__bin_characteristic = self.__float_format[1:order_bin_size + 1]
        self.__dec_characteristic = int(self.__bin_characteristic, base=2)
        self.__dec_order = self.__dec_characteristic - (mantissa_bin_size + order_bin_size)
        self.__bin_mantissa = self.__get_mantissa_by_float(order_bin_size, save_first_digit)
        self.__bin_num = self.__get_bin_by_mantissa()
        self.__dec_num = self.__get_dec_by_bin()

    def __get_mantissa_and_order_by_bin(self):
        """Возвращает мантиссу и порядок числа по его дв. представлению"""
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

    def __get_float_format_by_all(self, mant_size, order_size, save):
        """Возвращает число в формате с плавающей точкой"""
        sign = self.__sign
        order = self.__bin_characteristic
        first_digit = "1" if save else ""
        if sign == "1":
            mantissa = self.__bin_mantissa[3:]
        else:
            mantissa = self.__bin_mantissa[2:]
        res = sign + order + first_digit + mantissa
        sum_size = 1 + mant_size + (1 if save else 0) + order_size
        return res.ljust(sum_size, "0")[:sum_size]

    def __get_mantissa_by_float(self, order_bin_size, save_first_digit):
        """Мантисса по вещ. представлению"""
        float_mantissa = self.__float_format[order_bin_size + 1:].rstrip("0")
        if save_first_digit:
            mant = ("1." + float_mantissa[1:]).ljust(4, "0")
        else:
            mant = ("1." + float_mantissa).ljust(4, "0")
        if self.__sign == "1":
            return "-" + mant
        else:
            return mant

    def __get_bin_by_mantissa(self):
        """Число в двоичной с.с. по мантиссе"""
        order = self.__dec_order
        sign = "-" if self.__sign == "1" else ""
        dot_pos = self.__bin_mantissa.find(".")
        full_mantissa = self.__bin_mantissa[:dot_pos] + self.__bin_mantissa[dot_pos + 1:]
        if self.__sign == "1":
            full_mantissa = full_mantissa[1:]
        if order >= 0:
            dot_pos = 1 + order
            full_mantissa = full_mantissa.ljust(dot_pos + 1, "0")
            left_part = full_mantissa[:dot_pos]
            right_part = full_mantissa[dot_pos:]
            return sign + left_part + "." + right_part
        else:
            full_mantissa = ("0" * abs(order)) + full_mantissa
            return sign + full_mantissa[0] + "." + full_mantissa[1:]

    def __get_dec_by_bin(self):
        """Число в десятичной с. с. по двоичному представлению"""
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
    """Сложение двух чисел в двоичной системе"""
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
