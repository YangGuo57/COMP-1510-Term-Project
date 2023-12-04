from unittest import TestCase
from helper_functions.weekday import go_home
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_go_home_print(self, mock_output):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        go_home(character)
        system_print = mock_output.getvalue()
        expected_print = 'You decide to call it a day and head home to get some rest.'
        self.assertTrue(expected_print in system_print)

    @patch('random.randint', side_effect=[10])
    def test_go_home_change_stat(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        go_home(character)
        expected = {'IQ': 1.0, 'EQ': 10, 'stress': 0, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(character, expected)
