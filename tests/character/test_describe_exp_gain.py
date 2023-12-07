from unittest import TestCase
from unittest.mock import patch
import io
from game_system.character import describe_exp_gain


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_exp_gain_1510(self, mock_stdout):
        character = {'exp': {'1510': 10, '1537': 0, '1113': 0, '1712': 0}}
        describe_exp_gain(character, '1510', 10)
        self.assertIn('Through hardwork and perseverance', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1510 increased by 10.', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1510 is now 10.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_exp_gain_1537(self, mock_stdout):
        character = {'exp': {'1510': 10, '1537': 10, '1113': 0, '1712': 0}}
        describe_exp_gain(character, '1537', 10)
        self.assertIn('Through hardwork and perseverance', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1537 increased by 10.', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1537 is now 10.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_exp_gain_1113(self, mock_stdout):
        character = {'exp': {'1510': 10, '1537': 10, '1113': 10, '1712': 0}}
        describe_exp_gain(character, '1113', 10)
        self.assertIn('Through hardwork and perseverance', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1113 increased by 10.', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1113 is now 10.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_exp_gain_1712(self, mock_stdout):
        character = {'exp': {'1510': 10, '1537': 10, '1113': 10, '1712': 10}}
        describe_exp_gain(character, '1712', 10)
        self.assertIn('Through hardwork and perseverance', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1712 increased by 10.', mock_stdout.getvalue())
        self.assertIn('Your experience in COMP1712 is now 10.', mock_stdout.getvalue())
