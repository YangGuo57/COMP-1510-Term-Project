from unittest import TestCase
from helper_functions.exam import calculate_average


class Test(TestCase):

    def test_calculate_average_A(self):
        character = {
            'midterm': {'1510': 'A', '1537': 'A', '1113': 'A', '1712': 'D'},
            'final': {'1510': 'A', '1537': 'A', '1113': 'A', '1712': 'D'}
        }
        result = calculate_average(character)
        self.assertEqual(result, 'A')

    def test_calculate_average_B(self):
        character = {
            'midterm': {'1510': 'A', '1537': 'B', '1113': 'C', '1712': 'D'},
            'final': {'1510': 'A', '1537': 'B', '1113': 'C', '1712': 'D'}
        }
        result = calculate_average(character)
        self.assertEqual(result, 'B')

    def test_calculate_average_C(self):
        character = {
            'midterm': {'1510': 'B', '1537': 'B', '1113': 'C', '1712': 'D'},
            'final': {'1510': 'A', '1537': 'C', '1113': 'C', '1712': 'D'}
        }
        result = calculate_average(character)
        self.assertEqual(result, 'C')

    def test_calculate_average_invalid_grade(self):
        character = {
            'midterm': {'1510': 'D', '1537': 'E', '1113': 'F', '1712': 'G'},
            'final': {'1510': 'D', '1537': 'E', '1113': 'F', '1712': 'G'}
        }
        result = calculate_average(character)
        self.assertIsNone(result)
