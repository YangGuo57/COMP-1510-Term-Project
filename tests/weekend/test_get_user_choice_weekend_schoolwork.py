from unittest import TestCase
from game_system.weekend import get_user_choice_weekend_schoolwork
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_valid_input(self, _):
        expected = '1510'
        system = get_user_choice_weekend_schoolwork()
        self.assertEqual(expected, system)

    @patch('builtins.input', side_effect=['@', '2'])
    def test_invalid_then_valid_input(self, _):
        expected = '1537'
        system = get_user_choice_weekend_schoolwork()
        self.assertEqual(expected, system)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['A', '1'])
    def test_print_invalid_then_valid_input(self, _, mock_output):
        get_user_choice_weekend_schoolwork()
        system_print = mock_output.getvalue()
        expected = 'That is not a valid entry.\n'
        self.assertEqual(system_print, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['A', ' ', '1'])
    def test_print_invalid_invalid_then_valid_input(self, _, mock_output):
        get_user_choice_weekend_schoolwork()
        system_print = mock_output.getvalue()
        expected = 'That is not a valid entry.\nThat is not a valid entry.\n'
        self.assertEqual(system_print, expected)
