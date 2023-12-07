from unittest import TestCase
from unittest.mock import patch
from game_system.weekend import weekend_park


class Test(TestCase):
    @patch('game_system.weekend.generate_job_posting')
    @patch('game_system.weekend.random_park_event')
    def test_weekend_park_character_without_job(self, mock_random_event, mock_job_posting):
        mock_job_posting.return_value = True
        character = {}
        result = weekend_park(character)
        mock_job_posting.assert_called_once()
        mock_random_event.assert_not_called()
        self.assertTrue(result)

    @patch('game_system.weekend.generate_job_posting')
    @patch('game_system.weekend.random_park_event')
    def test_weekend_park_character_with_job(self, mock_random_event, mock_job_posting):
        character = {'job': True}
        result = weekend_park(character)
        mock_job_posting.assert_not_called()
        mock_random_event.assert_called_once()
        self.assertFalse(result)
