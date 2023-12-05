from unittest import TestCase
from unittest.mock import patch
from helper_functions.weekend import describe_weekend_home_action


class Test(TestCase):
    @patch('builtins.print')
    def test_describe_weekend_home_action_productive_action(self, mock_print):
        describe_weekend_home_action('1')
        mock_print.assert_called_once_with('You decide to be productive (or try to be productive).')

    @patch('builtins.print')
    def test_describe_weekend_home_action_sleep_action(self, mock_print):
        describe_weekend_home_action('2')
        mock_print.assert_called_once_with('You pass out in your bed. Good night and sweet dreams.')
