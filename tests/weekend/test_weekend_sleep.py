from unittest import TestCase
from helper_functions.weekend import weekend_sleep
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', side_effect=[25])
    def test_sleep(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 25, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        expected = {'IQ': 1.0, 'EQ': 10, 'stress': 0, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        weekend_sleep(character)
        self.assertEqual(character, expected)

    @patch('random.randint', side_effect=[30])
    def test_sleep_again(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 40, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        expected = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        weekend_sleep(character)
        self.assertEqual(character, expected)