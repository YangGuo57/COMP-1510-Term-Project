from unittest import TestCase
from unittest.mock import patch
from helper_functions.character import describe_wealth_change
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_wealth_change_increase(self, mock_stdout):
        character = {'wealth': 50}
        describe_wealth_change(character, 50)
        self.assertIn('Earning money puts a smile on your face', mock_stdout.getvalue())
        self.assertIn('Your wealth increases by 50', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_wealth_change_decrease(self, mock_stdout):
        character = {'wealth': 100}
        describe_wealth_change(character, -50)
        self.assertIn('You watch your savings deplete', mock_stdout.getvalue())
        self.assertIn('Your wealth decreases by 50', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_wealth_change_no_change(self, mock_stdout):
        character = {'wealth': 100}
        describe_wealth_change(character, 0)
        self.assertIn('Earning money puts a smile on your face', mock_stdout.getvalue())
        self.assertIn('Your wealth increases by 0', mock_stdout.getvalue())
