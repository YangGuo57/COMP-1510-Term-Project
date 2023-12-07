from unittest import TestCase
from unittest.mock import patch
import io
from game_system.character import describe_flat_stat_gain


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_flat_stat_gain_EQ_increase(self, mock_stdout):
        character = {'EQ': 2}
        describe_flat_stat_gain(character, 'EQ', 1)
        self.assertIn('You feel more confident talking to humans now.', mock_stdout.getvalue())
        self.assertIn('Your EQ increases by 1.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_flat_stat_gain_EQ_decrease(self, mock_stdout):
        character = {'EQ': 2}
        describe_flat_stat_gain(character, 'EQ', -1)
        self.assertIn('Clearly you are not very good at handling human interactions', mock_stdout.getvalue())
        self.assertIn('Your EQ decreases by 1.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_flat_stat_gain_IQ_decrease(self, mock_stdout):
        character = {'IQ': 0}
        describe_flat_stat_gain(character, 'IQ', 1)
        self.assertIn('You\'ve never felt this intelligent before in your entire life.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_flat_stat_gain_project_increase(self, mock_stdout):
        character = {'project': 0}
        describe_flat_stat_gain(character, 'project', 1)
        self.assertIn('You start grinding your personal project.', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_flat_stat_gain_project_no_change(self, mock_stdout):
        character = {'EQ': 2}
        describe_flat_stat_gain(character, 'EQ', 0)
        self.assertIn('Clearly you are not very good at handling human interactions', mock_stdout.getvalue())
        self.assertIn('Your EQ decreases by 0.', mock_stdout.getvalue())
