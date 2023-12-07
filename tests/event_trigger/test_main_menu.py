from unittest import TestCase
from game_system.event_trigger import main_menu
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_main_menu_valid_input(self, mock_input):
        self.assertEqual(main_menu(), '1')
        self.assertEqual(main_menu(), '2')
        self.assertEqual(main_menu(), '3')
        self.assertEqual(main_menu(), '4')
