from unittest import TestCase
from game_system.weekday import weekday_schoolwork
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', side_effect=[15, 15, 15, 15, 10])
    def test_weekday_schoolwork_one_IQ(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        expected = {'IQ': 1.0, 'EQ': 10, 'stress': 20, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 15, '1537': 15, '1113': 15, '1712': 15},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        weekday_schoolwork(character)
        self.assertEqual(character, expected)

    @patch('random.randint', side_effect=[15, 15, 15, 15, 10])
    def test_weekday_schoolwork_two_IQ(self, _):
        character = {'IQ': 2.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        expected = {'IQ': 2.0, 'EQ': 10, 'stress': 20, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 30, '1537': 30, '1113': 30, '1712': 30},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        weekday_schoolwork(character)
        self.assertEqual(character, expected)

