# Файл с классами наборов чисел в различных системах счисления и представлениях

import constants as c


class IntKit:
    def __init__(self, dec_num=0, bin_num="0", str_code="0", rev_code="0", add_code="0"):
        self.__dec_num = dec_num  # Число в 10й сс
        self.__bin_num = bin_num  # Число в 2й сс
        self.__str_code = str_code  # Прямой код числа
        self.__rev_code = rev_code  # Обратный код числа
        self.__add_code = add_code  # Дополнительный код числа

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
                # Доп. код = обратный код числа, меньшего данного на 1 по модулю
                one_less_by_abs = IntKit(dec_num=self.__dec_num + 1)
                one_less_by_abs.by_dec_num(bin_size)

                self.__fill_codes_errors(self, c.Int.STR_CODE_INDEX,
                                         c.Int.REV_CODE_INDEX)
                self.__add_code = one_less_by_abs.__rev_code
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

    def print(self, fields):
        """Вывод всего комплекта в поля ввода-вывода"""
        fields.write(c.Int.DEC_NUM_INDEX, self.__dec_num)
        fields.write(c.Int.BIN_NUM_INDEX, self.__bin_num)
        fields.write(c.Int.STR_CODE_INDEX, self.__str_code)
        fields.write(c.Int.REV_CODE_INDEX, self.__rev_code)
        fields.write(c.Int.ADD_CODE_INDEX, self.__add_code)

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
