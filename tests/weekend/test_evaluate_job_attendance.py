from unittest import TestCase
from unittest.mock import patch
from helper_functions.weekend import evaluate_job_attendance


class Test(TestCase):

    def setUp(self):
        self.character = {'job': True, 'skip_job': 0}

    @patch('helper_functions.weekend.evaluate_firing_from_job')
    def test_evaluate_job_attendance_skip_work(self, mock_evaluate_firing):

        evaluate_job_attendance(self.character, False)
        self.assertEqual(self.character['skip_job'], 1)
        mock_evaluate_firing.assert_called_once()

    @patch('helper_functions.weekend.evaluate_firing_from_job')
    def test_evaluate_job_attendance_not_skip_work(self, mock_evaluate_firing):
        evaluate_job_attendance(self.character, True)
        self.assertEqual(self.character['skip_job'], 0)
        mock_evaluate_firing.assert_not_called()

    @patch('helper_functions.weekend.evaluate_firing_from_job')
    def test_evaluate_job_attendance_no_job(self, mock_evaluate_firing):
        self.character['job'] = False
        evaluate_job_attendance(self.character, True)
        self.assertEqual(self.character['skip_job'], 0)
        mock_evaluate_firing.assert_not_called()
