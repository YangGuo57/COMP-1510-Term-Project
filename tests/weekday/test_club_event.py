from unittest import TestCase
from game_system.weekday import club_event
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_club_event_print(self, mock_output):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        club_event(character)
        system_print = mock_output.getvalue()
        expected_print = ('In the midst of overwhelming homework, the news of a socializing club event feels like a '
                          'welcomed blessing. Naturally, you decide to join, finding solace among your peers as you '
                          'all unwind and complain about your school life to each other. Laughter fills the air, '
                          'and as the evening unfolds, it\'s as if the weight of your stress has been lifted, '
                          'leaving you liberated and refreshed.')
        self.assertTrue(expected_print in system_print)

    @patch('random.randint', side_effect=[-10, 1])
    def test_club_event_character_stat_change_one(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 10, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        expected = {'IQ': 1.0, 'EQ': 11, 'stress': 0, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        club_event(character)
        self.assertEqual(character, expected)

    @patch('random.randint', side_effect=[-15, 3])
    def test_club_event_character_stat_change_two(self, _):
        character = {'IQ': 1.0, 'EQ': 10, 'stress': 15, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                           '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}
        expected = {'IQ': 1.0, 'EQ': 13, 'stress': 0, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0,
                    'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                    'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                    'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                          '1510': 0, '1537': 0, '1712': 0, '1113': 0},
                    'location': 'home', 'vaccinated': False, 'skip_job': 0}
        club_event(character)
        self.assertEqual(character, expected)
