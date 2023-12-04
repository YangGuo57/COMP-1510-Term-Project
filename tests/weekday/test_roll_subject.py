from unittest import TestCase
from helper_functions.weekday import roll_subject
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', side_effect=[0])
    def test_roll_0(self, _):
        system_output = roll_subject()
        expected_output = '1510'
        self.assertEqual(system_output, expected_output)

    @patch('random.randint', side_effect=[1])
    def test_roll_1(self, _):
        system_output = roll_subject()
        expected_output = '1537'
        self.assertEqual(system_output, expected_output)

    @patch('random.randint', side_effect=[2])
    def test_roll_2(self, _):
        system_output = roll_subject()
        expected_output = '1113'
        self.assertEqual(system_output, expected_output)

    @patch('random.randint', side_effect=[3])
    def test_roll_3(self, _):
        system_output = roll_subject()
        expected_output = '1712'
        self.assertEqual(system_output, expected_output)
