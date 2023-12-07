from unittest import TestCase
from unittest.mock import patch
from game_system.weekend import weekend_job


class Test(TestCase):
    def setUp(self):
        self.character = {'wealth': 0, 'EQ': 0, 'stress': 0}

    @patch('builtins.print')
    @patch('random.randint')
    def test_weekend_job_with_job(self, mock_randint, mock_print):
        self.character['job'] = True
        mock_randint.side_effect = [2, 5]
        weekend_job(self.character)
        self.assertEqual(self.character['wealth'], 20)
        self.assertEqual(self.character['EQ'], 2)
        self.assertEqual(self.character['stress'], 5)
        mock_randint.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('random.randint', return_value=6)
    def test_weekend_job_without_job_but_had_one(self, mock_randint, mock_print):
        self.character['job'] = False
        weekend_job(self.character)
        self.assertEqual(self.character['stress'], 6)
        mock_randint.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('random.randint', return_value=7)
    def test_weekend_job_never_had_job(self, mock_randint, mock_print):
        if 'job' in self.character:
            del self.character['job']
        weekend_job(self.character)
        self.assertEqual(self.character['stress'], 7)
        mock_randint.assert_called()
        mock_print.assert_called()
