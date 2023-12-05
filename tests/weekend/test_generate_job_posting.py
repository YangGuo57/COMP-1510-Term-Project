from unittest import TestCase
from unittest.mock import patch
from helper_functions.weekend import generate_job_posting


class Test(TestCase):
    @patch('helper_functions.weekend.binary_user_choice', return_value='1')
    def test_character_applies_for_job(self, mock_choice):
        character = {'job': False}
        result = generate_job_posting(character)
        self.assertTrue(result)
        self.assertTrue(character['job'])

    @patch('helper_functions.weekend.binary_user_choice', return_value='2')
    def test_character_does_not_apply_for_job(self, mock_choice):
        character = {'job': False}
        result = generate_job_posting(character)
        self.assertFalse(result)
        self.assertFalse(character['job'])
