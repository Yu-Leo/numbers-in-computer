import unittest

from calculations.numbers_kits import IntKit


class TestIntKit(unittest.TestCase):
    """
    Test int mode
    """

    def setUp(self):
        self.kit_1 = IntKit(5)
        self.kit_1.by_dec_num(4)

        self.kit_2 = IntKit(0)
        self.kit_2.by_dec_num(8)

        self.kit_3 = IntKit(-5)
        self.kit_3.by_dec_num(8)

    def test_init(self):
        """
        Test initialization of kits
        """
        self.assertEqual(self.kit_1["dec_num"], 5)
        self.assertEqual(self.kit_2["dec_num"], 0)
        self.assertEqual(self.kit_3["dec_num"], -5)

    def test_from_dec_to_bin(self):
        """
        Test conversion from decimal system to binary
        """
        self.assertEqual(self.kit_1["bin_num"], "101")
        self.assertEqual(self.kit_2["bin_num"], "0")
        self.assertEqual(self.kit_3["bin_num"], "-")

    def test_from_dec_to_str_code(self):
        """
        Test conversion from decimal system to the straight code representation
        """
        self.assertEqual(self.kit_1["str_code"], "0101")
        self.assertEqual(self.kit_2["str_code"], "00000000")
        self.assertEqual(self.kit_3["str_code"], "10000101")

    def test_from_dec_to_rev_code(self):
        """
        Test conversion from decimal system to the reversed code representation
        """
        self.assertEqual(self.kit_1["rev_code"], "0101")
        self.assertEqual(self.kit_2["rev_code"], "00000000")
        self.assertEqual(self.kit_3["rev_code"], "11111010")

    def test_from_dec_to_add_code(self):
        """
        Test conversion from decimal system to the additional code representation
        """
        self.assertEqual(self.kit_1["add_code"], "0101")
        self.assertEqual(self.kit_2["add_code"], "00000000")
        self.assertEqual(self.kit_3["add_code"], "11111011")
