from unittest import TestCase
from unittest.mock import patch
from game_system.weekend import evaluate_firing_from_job


class Test(TestCase):

    @patch('game_system.character.change_stat')
    @patch('game_system.weekend.binary_user_choice', return_value='2')
    def test_evaluate_firing_from_job_skipping_three_times(self, mock_user_choice, mock_change_stat):
        character = {'skip_job': 3, 'job': True, 'EQ': 50}
        evaluate_firing_from_job(character)
        self.assertFalse(character['job'])
        mock_change_stat.assert_called_with(character, 'EQ', -15)
        mock_user_choice.assert_not_called()

    @patch('game_system.character.change_stat')
    @patch('game_system.weekend.binary_user_choice', return_value='2')
    def test_evaluate_firing_from_job_quit_after_two_skips(self, mock_user_choice, mock_change_stat):
        character = {'skip_job': 2, 'job': True, 'EQ': 50}
        evaluate_firing_from_job(character)
        self.assertFalse(character['job'])
        mock_change_stat.assert_not_called()
        mock_user_choice.assert_called_once()

    @patch('game_system.weekend.binary_user_choice', return_value='1')
    def test_evaluate_firing_from_job_not_quit_after_two_skips(self, mock_user_choice):
        character = {'skip_job': 2, 'job': True, 'EQ': 50}
        evaluate_firing_from_job(character)
        self.assertTrue(character['job'])
        mock_user_choice.assert_called_once()
