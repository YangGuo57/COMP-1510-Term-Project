from unittest import TestCase
from game_system.character import create_character


class Test(TestCase):

    def test_create_character_empty_answers(self):
        answers = []
        expected_output = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 1, 'Y': 1, 'project': 0,
                           'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                           'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                           'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                           'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                           'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0, 'work': 0,
                                                 '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                           'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(create_character(answers), expected_output)

    def test_create_character_normal_input(self):
        answers = [0, 1, 0, 1]
        expected_output = {'IQ': 1.0, 'EQ': 10, 'stress': 0, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                           'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                           'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                           'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                           'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                           'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0, 'work': 0,
                                                 '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                           'location': 'home', 'vaccinated': False, 'skip_job': 0}
        self.assertEqual(create_character(answers), expected_output)
