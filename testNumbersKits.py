import unittest

from numbersKits import IntKit, FloatKit


class TestIntKit(unittest.TestCase):
    """
    Test int mode
    """

    def setUp(self):
        self.kit = None

    def test_from_dec_1(self):
        """
        Test conversion from decimal system to the rest
        """
        self.kit = IntKit(5)
        self.kit.by_dec_num(4)
        self.assertEqual(self.kit["dec_num"], 5)
        self.assertEqual(self.kit["bin_num"], "101")
        self.assertEqual(self.kit["str_code"], "0101")
        self.assertEqual(self.kit["rev_code"], "0101")
        self.assertEqual(self.kit["add_code"], "0101")

    def test_from_dec_2(self):
        """
        Test conversion from decimal system to the rest
        """
        self.kit = IntKit(0)
        self.kit.by_dec_num(8)
        self.assertEqual(self.kit["dec_num"], 0)
        self.assertEqual(self.kit["bin_num"], "0")
        self.assertEqual(self.kit["str_code"], "00000000")
        self.assertEqual(self.kit["rev_code"], "00000000")
        self.assertEqual(self.kit["add_code"], "00000000")

    def test_from_dec_3(self):
        """
        Test conversion from decimal system to the rest
        """
        self.kit = IntKit(-5)
        self.kit.by_dec_num(8)
        self.assertEqual(self.kit["dec_num"], -5)
        self.assertEqual(self.kit["bin_num"], "-")
        self.assertEqual(self.kit["str_code"], "10000101")
        self.assertEqual(self.kit["rev_code"], "11111010")
        self.assertEqual(self.kit["add_code"], "11111011")
