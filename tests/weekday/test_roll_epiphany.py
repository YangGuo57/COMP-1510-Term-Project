from unittest import TestCase
from helper_functions.weekday import roll_epiphany
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', side_effect=[0])
    def test_epiphany(self, _):
        self.assertTrue(roll_epiphany())

    @patch('random.randint', side_effect=[1])
    def test_no_epiphany_1(self, _):
        self.assertFalse(roll_epiphany())

    @patch('random.randint', side_effect=[2])
    def test_no_epiphany_2(self, _):
        self.assertFalse(roll_epiphany())

    @patch('random.randint', side_effect=[3])
    def test_no_epiphany_3(self, _):
        self.assertFalse(roll_epiphany())

    @patch('random.randint', side_effect=[4])
    def test_no_epiphany_4(self, _):
        self.assertFalse(roll_epiphany())
