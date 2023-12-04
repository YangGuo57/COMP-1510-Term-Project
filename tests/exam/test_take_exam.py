from unittest import TestCase
from unittest.mock import patch
from helper_functions.exam import take_exam


class Test(TestCase):
    def setUp(self):
        self.character = {"midterm": {}, "final": {}}

    @patch('helper_functions.exam.exam_status', return_value={"A": ["Great job!"], "F": ["Oh no!"]})
    @patch('helper_functions.exam.evaluate_exam', return_value="A")
    @patch('helper_functions.exam.reward_character')
    def test_midterm_all_pass(self, mock_reward, mock_evaluate, mock_status):
        result = take_exam(self.character, "midterm")
        self.assertTrue(result)
        mock_evaluate.assert_called()
        mock_status.assert_called()
        mock_reward.assert_called()

    @patch('helper_functions.exam.exam_status', return_value={"A": ["Great job!"], "F": ["Oh no!"]})
    @patch('helper_functions.exam.evaluate_exam', side_effect=["F", "A", "A", "A"])
    @patch('helper_functions.exam.reward_character')
    def test_fail_midterm(self, mock_reward, mock_evaluate, mock_status):
        result = take_exam(self.character, "midterm")
        self.assertFalse(result)
        mock_evaluate.assert_called()
        mock_status.assert_called()
        mock_reward.assert_called()

    @patch('helper_functions.exam.exam_status', return_value={"A": ["Great job!"], "F": ["Oh no!"]})
    @patch('helper_functions.exam.evaluate_exam', return_value="F")
    @patch('helper_functions.exam.reward_character')
    def test_final_one_fail(self, mock_reward, mock_evaluate, mock_status):
        result = take_exam(self.character, "final")
        self.assertFalse(result)
        mock_evaluate.assert_called()
        mock_status.assert_called()
        mock_reward.assert_not_called()

    @patch('helper_functions.exam.exam_status', return_value={"A": ["Great job!"], "F": ["Oh no!"]})
    @patch('helper_functions.exam.evaluate_exam', return_value="A")
    @patch('helper_functions.exam.reward_character')
    def test_final_all_pass(self, mock_reward, mock_evaluate, mock_status):
        result = take_exam(self.character, "final")
        self.assertTrue(result)
        mock_evaluate.assert_called()
        mock_status.assert_called()
        mock_reward.assert_called()
