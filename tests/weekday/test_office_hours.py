from unittest import TestCase
from game_system.weekday import office_hours
from unittest.mock import patch


class Test(TestCase):
    def setUp(self):
        self.character = {
            'IQ': 10, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 1, 'Y': 1, 'project': 0,
            'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
            'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
            'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
            'final': {'1510': None, '1537': None, '1113': None, '1712': None},
            'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0, 'work': 0, '1510': 0, '1537': 0,
                                  '1712': 0, '1113': 0},
            'location': 'home', 'vaccinated': False, 'skip_job': 0
        }

    @patch('game_system.weekday.roll_epiphany')
    @patch('random.randint')
    def test_office_hours_no_epiphany(self, mock_randint, mock_roll_epiphany):
        subject_code = '1510'
        mock_roll_epiphany.return_value = False
        mock_randint.side_effect = [15, 10]
        office_hours(self.character, subject_code)
        expected_exp_gain = 15 * self.character['IQ']
        expected_stress = 10

        self.assertEqual(self.character['exp'][subject_code], expected_exp_gain)
        self.assertEqual(self.character['stress'], expected_stress)

    @patch('game_system.weekday.roll_epiphany')
    @patch('random.randint')
    def test_office_hours_no_epiphany(self, mock_randint, mock_roll_epiphany):
        subject_code = '1510'
        mock_roll_epiphany.return_value = True
        mock_randint.return_value = 10
        office_hours(self.character, subject_code)
        expected_exp_gain = 100
        expected_stress = 10

        self.assertEqual(self.character['exp'][subject_code], expected_exp_gain)
        self.assertEqual(self.character['stress'], expected_stress)
