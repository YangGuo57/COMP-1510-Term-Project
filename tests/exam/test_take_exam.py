from unittest import TestCase
from unittest.mock import patch
from game_system.exam import take_exam


class Test(TestCase):
    SUBJECTS = ['1510', '1537', '1113', '1712']

    def setUp(self):
        self.character = {
            'midterm': {subject: 'F' for subject in Test.SUBJECTS},
            'final': {subject: 'F' for subject in Test.SUBJECTS}
        }

    @patch('builtins.print')
    @patch('game_system.exam.evaluate_exam', return_value='A')
    @patch('game_system.exam.reward_character')
    @patch('game_system.exam.exam_status', return_value={'A': ['Great job!'], 'F': ['Failed']})
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_take_exam_pass_all(self, mock_choice, mock_exam_status, mock_reward_character, mock_evaluate_exam,
                                mock_print):
        result = take_exam(self.character, 'midterm')
        self.assertTrue(result)
        for subject in Test.SUBJECTS:
            self.assertEqual(self.character['midterm'][subject], 'A')

        mock_choice.assert_not_called()
        mock_exam_status.assert_called()
        mock_reward_character.assert_called()
        mock_evaluate_exam.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('game_system.exam.evaluate_exam', side_effect=['F'] + ['A'] * (len(SUBJECTS) - 1))
    @patch('game_system.exam.reward_character')
    @patch('game_system.exam.exam_status', return_value={'A': ['Great job!'], 'F': ['Failed']})
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_take_exam_fail_one_subject(self, mock_choice, mock_exam_status, mock_reward_character, mock_evaluate_exam,
                                        mock_print):
        result = take_exam(self.character, 'midterm')
        self.assertFalse(result)
        self.assertEqual(self.character['midterm'][Test.SUBJECTS[0]], 'F')

        mock_choice.assert_not_called()
        mock_exam_status.assert_called()
        mock_reward_character.assert_called()
        mock_evaluate_exam.assert_called()
        mock_print.assert_called()
