from unittest import TestCase
from unittest.mock import patch
from game_system.weekend import generate_job_posting


class Test(TestCase):
    @patch('game_system.weekend.binary_user_choice', return_value='1')
    def test_generate_job_posting_character_applies_for_job(self, mock_choice):
        character = {'job': False}
        result = generate_job_posting(character)
        self.assertTrue(result)
        self.assertTrue(character['job'])
        self.assertTrue(mock_choice.called)

    @patch('game_system.weekend.binary_user_choice', return_value='2')
    def test_generate_job_posting_character_does_not_apply_for_job(self, mock_choice):
        character = {'job': False}
        result = generate_job_posting(character)
        self.assertFalse(result)
        self.assertFalse(character['job'])
        self.assertTrue(mock_choice.called)
