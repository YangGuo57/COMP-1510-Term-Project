from unittest import TestCase
from helper_functions.weekday import assessment_stat_change
from unittest.mock import patch


class Test(TestCase):

    @patch('random.randint', return_value=8)
    def test_fail_quiz(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                            '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        assessment_stat_change(character, True, '1510', 'quiz')
        expected_character = {'IQ': 1.0, 'EQ': 10, 'stress': 18, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                              'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                              'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                              'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                                    '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                              'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(character['stress'], expected_character['stress'])

    @patch('random.randint', side_effect=[4, 15])
    def test_pass_quiz(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        assessment_stat_change(character, False, '1510', 'quiz')
        expected_character = {'IQ': 1.0, 'EQ': 10, 'stress': 14, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                              'exp': {'1510': 15, '1537': 0, '1113': 0, '1712': 0},
                              'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                              'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                                    '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                              'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(character['stress'], expected_character['stress'])

    @patch('random.randint', side_effect=[4, 25])
    def test_pass_assignment(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        assessment_stat_change(character, False, '1537', 'assignment')
        expected_character = {'IQ': 1.0, 'EQ': 10, 'stress': 14, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                              'exp': {'1510': 0, '1537': 25, '1113': 0, '1712': 0},
                              'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                              'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                                    '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                              'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(character, expected_character)

    @patch('random.randint', return_value=8)
    def test_fail_assignment(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        assessment_stat_change(character, True, '1537', 'assignment')
        expected_character = {'IQ': 1.0, 'EQ': 10, 'stress': 18, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                              'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                              'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                              'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                              'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                                    '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                              'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(character['stress'], expected_character['stress'])
