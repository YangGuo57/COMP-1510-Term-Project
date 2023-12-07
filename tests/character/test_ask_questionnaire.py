from unittest import TestCase
from unittest.mock import patch
from game_system.character import ask_questionnaire


class Test(TestCase):
    @patch('game_system.character.input', side_effect=['1', '2', '1', '2'])
    def test_ask_questionnaire_coop_setting(self, mock_input):
        setting = 'coop'
        expected_answers = [0, 1, 0, 1]
        actual_answers = ask_questionnaire(setting)
        self.assertEqual(actual_answers, expected_answers)
        self.assertEqual(mock_input.call_count, 4)

    @patch('game_system.character.input', side_effect=['2', '1', '2', '1'])
    def test_ask_questionnaire_new_setting(self, mock_input):
        setting = 'new'
        expected_answers = [1, 0, 1, 0]
        actual_answers = ask_questionnaire(setting)
        self.assertEqual(actual_answers, expected_answers)
        self.assertEqual(mock_input.call_count, 4)
