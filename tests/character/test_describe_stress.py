from unittest import TestCase
from unittest.mock import patch
import io
from game_system.character import describe_stress


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_extreme(self, mock_stdout):
        character = {'stress': 101}
        describe_stress(character)
        self.assertIn('ERROR 4044444444', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_high(self, mock_stdout):
        character = {'stress': 90}
        describe_stress(character)
        self.assertIn('You feel like you no longer have a FUnctionING BRAIn', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_moderate(self, mock_stdout):
        character = {'stress': 75}
        describe_stress(character)
        self.assertIn('your brain is no longer registering what you\'re reading', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_low(self, mock_stdout):
        character = {'stress': 70}
        describe_stress(character)
        self.assertEqual('', mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_stress_very_low(self, mock_stdout):
        character = {'stress': 60}
        describe_stress(character)
        self.assertEqual('', mock_stdout.getvalue().strip())
