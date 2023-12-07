from unittest import TestCase
from unittest.mock import patch
from game_system.movement import fast_travel


class Test(TestCase):
    def setUp(self):
        self.character = {
            'X': 0,
            'Y': 0,
            'visited_locations': {'home': True, 'school': False}
        }
        self.locations = {
            'door': {
                'main': {'home': (2, 4), 'school': (4, 5)}
            }
        }

    @patch('builtins.input', side_effect=['home'])
    @patch('builtins.print')
    def test_fast_travel_to_visited(self, mock_print, mock_input):
        fast_travel(self.character)
        self.assertEqual(self.character['X'], 2)
        self.assertEqual(self.character['Y'], 3)
        mock_print.assert_called_with("You've fast traveled to home!")

    @patch('builtins.input', side_effect=['school'])
    @patch('builtins.print')
    def test_fast_travel_to_not_visited(self, mock_print, mock_input):
        fast_travel(self.character)
        self.assertNotEqual(self.character['X'], 4)
        self.assertNotEqual(self.character['Y'], 5)
        mock_print.assert_called_with(
            "You're new to Vancouver, you don't know where school is! "
            "You must have visited school at least once before fast traveling there.")
