from unittest import TestCase
from unittest.mock import patch
from game_system.weekend import random_park_event


class Test(TestCase):
    def setUp(self):
        self.character = {'stress': 10, 'wealth': 0}

    @patch('builtins.print')
    @patch('random.randint', return_value=10)
    def test_random_event_wealth_gain(self, mock_randint, mock_print):
        with patch('time.sleep'):
            random_park_event(self.character)

            self.assertEqual(self.character['wealth'], 10)
            mock_randint.assert_called_once_with(1, 10)
            mock_print.assert_called()

    @patch('builtins.print')
    @patch('random.randint')
    def test_random_event_stress_loss(self, mock_randint, mock_print):
        mock_randint.side_effect = [6, -10]

        def mock_change_stat(character, key, value):
            character[key] = max(0, character[key] + value)

        with patch('time.sleep'), patch('game_system.character.change_stat', new=mock_change_stat):
            random_park_event(self.character)
            self.assertEqual(self.character['stress'], 0)
            mock_randint.assert_called()
            mock_print.assert_called()
