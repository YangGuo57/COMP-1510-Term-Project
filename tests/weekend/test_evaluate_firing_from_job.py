import unittest
from unittest.mock import patch
from helper_functions.weekend import evaluate_firing_from_job


class TestEvaluateFiringFromJob(unittest.TestCase):

    @patch('helper_functions.character.change_stat')
    @patch('helper_functions.weekend.binary_user_choice', return_value='2')
    def test_evaluate_firing_from_job_skipping_three_times(self, mock_user_choice, mock_change_stat):
        character = {'skip_job': 3, 'job': True, 'EQ': 50}
        evaluate_firing_from_job(character)
        self.assertFalse(character['job'])
        mock_change_stat.assert_called_with(character, 'EQ', -15)

    @patch('helper_functions.character.change_stat')
    @patch('helper_functions.weekend.binary_user_choice', return_value='2')
    def test_evaluate_firing_from_job_quit_after_two_skips(self, mock_user_choice, mock_change_stat):
        character = {'skip_job': 2, 'job': True, 'EQ': 50}
        evaluate_firing_from_job(character)
        self.assertFalse(character['job'])
        mock_change_stat.assert_not_called()

    @patch('helper_functions.weekend.binary_user_choice', return_value='1')
    def test_evaluate_firing_from_job_not_quit_after_two_skips(self, mock_user_choice):
        character = {'skip_job': 2, 'job': True, 'EQ': 50}
        evaluate_firing_from_job(character)
        self.assertTrue(character['job'])
