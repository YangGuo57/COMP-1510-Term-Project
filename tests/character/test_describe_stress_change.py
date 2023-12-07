from unittest import TestCase
from unittest.mock import patch
from game_system.character import describe_stress_change
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_change_increase(self, mock_stdout):
        character = {"stress": 1}
        describe_stress_change(character, 1)
        self.assertIn('The stress of life and schoolwork is getting to you', mock_stdout.getvalue())
        self.assertIn('Your stress increases by 1', mock_stdout.getvalue())
        self.assertIn('Your stress level is now 1.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_change_decrease(self, mock_stdout):
        character = {"stress": 0}
        describe_stress_change(character, -1)
        self.assertIn('You feel rejuvenated as if a great load has been taken off your shoulders.',
                      mock_stdout.getvalue())
        self.assertIn('Your stress decreases by 1', mock_stdout.getvalue())
        self.assertIn('Your stress level is now 0.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_change_no_change(self, mock_stdout):
        character = {"stress": 1}
        describe_stress_change(character, 0)
        self.assertIn('You feel rejuvenated as if a great load has been taken off your shoulders.',
                      mock_stdout.getvalue())
        self.assertIn('Your stress decreases by 0', mock_stdout.getvalue())
        self.assertIn('Your stress level is now 1.', mock_stdout.getvalue())
