from unittest import TestCase
from unittest.mock import patch
from helper_functions.weekend import execute_weekend_home_action


class Test(TestCase):

    def setUp(self):
        self.character = {"location": "", "stress": 50, "IQ": 100, "project": 0}

    @patch('helper_functions.weekend.binary_user_choice', return_value='1')
    @patch('helper_functions.weekend.get_user_choice_weekend_schoolwork', return_value='project')
    @patch('helper_functions.weekend.weekend_schoolwork')
    def test_execute_weekend_home_action_schoolwork_choice(self, mock_schoolwork, mock_get_choice,
                                                           mock_binary_choice):
        execute_weekend_home_action(self.character)
        mock_schoolwork.assert_called_with(self.character, 'project')
        self.assertEqual(self.character["location"], "home")
        mock_get_choice.assert_called_once()
        mock_binary_choice.assert_called_once()

    @patch('helper_functions.weekend.binary_user_choice', return_value='2')
    @patch('helper_functions.weekend.weekend_sleep')
    def test_execute_weekend_home_action_sleep_choice(self, mock_sleep, mock_binary_choice):
        execute_weekend_home_action(self.character)
        mock_sleep.assert_called_with(self.character)
        self.assertEqual(self.character["location"], "home")
        mock_binary_choice.assert_called_once()
