from unittest import TestCase
from unittest.mock import patch
from helper_functions.exam import take_coop_interview


class Test(TestCase):

    @patch('helper_functions.character.ask_questionnaire')
    def test_take_coop_interview_medium_eq_project_good_answers_pass(self, mock_questionnaire):
        mock_questionnaire.return_value = [1, 1, 1, 1]
        character = {'EQ': 5, 'project': 200}
        result = take_coop_interview(character)
        self.assertTrue(result)

    @patch('helper_functions.character.ask_questionnaire')
    def test_take_coop_interview_high_eq_low_project_bad_answers_fail(self, mock_questionnaire):
        mock_questionnaire.return_value = [0, 0, 0, 0]
        character = {'EQ': 10, 'project': 10}
        result = take_coop_interview(character)
        self.assertFalse(result)

    @patch('helper_functions.character.ask_questionnaire')
    def test_take_coop_interview_low_eq_high_project_good_answers_pass(self, mock_questionnaire):
        mock_questionnaire.return_value = [1, 1, 1, 1]
        character = {'EQ': 1, 'project': 200}
        result = take_coop_interview(character)
        self.assertTrue(result)

    @patch('helper_functions.character.ask_questionnaire')
    def test_take_coop_interview_zero_eq_project_fail(self, mock_questionnaire):
        mock_questionnaire.return_value = [1, 1, 1, 1]
        character = {'EQ': 0, 'project': 0}
        result = take_coop_interview(character)
        self.assertFalse(result)

    @patch('helper_functions.character.ask_questionnaire')
    def test_take_coop_interview_max_eq_project_pass(self, mock_questionnaire):
        mock_questionnaire.return_value = [0, 0, 0, 0]
        character = {'EQ': 10, 'project': 200}
        result = take_coop_interview(character)
        self.assertTrue(result)
