from unittest import TestCase
from unittest.mock import patch
from game_system.movement import get_user_choice


class Test(TestCase):
    @patch('builtins.input')
    def test_get_user_choice_direction_north(self, mock_input):
        mock_input.side_effect = ['w']
        character = {'location': 'home'}
        self.assertEqual(get_user_choice(character), 'North')

    @patch('builtins.input')
    def test_get_user_choice_direction_south(self, mock_input):
        mock_input.side_effect = ['s']
        character = {'location': 'home'}
        self.assertEqual(get_user_choice(character), 'South')

    @patch('builtins.input')
    def test_get_user_choice_direction_west(self, mock_input):
        mock_input.side_effect = ['a']
        character = {'location': 'home'}
        self.assertEqual(get_user_choice(character), 'West')

    @patch('builtins.input')
    def test_get_user_choice_direction_east(self, mock_input):
        mock_input.side_effect = ['d']
        character = {'location': 'home'}
        self.assertEqual(get_user_choice(character), 'East')

    @patch('builtins.input')
    def test_get_user_choice_school_command_back(self, mock_input):
        mock_input.side_effect = ['back']
        character = {'location': 'school'}
        self.assertEqual(get_user_choice(character), 'back')

    @patch('builtins.input')
    def test_get_user_choice_school_command_stats(self, mock_input):
        mock_input.side_effect = ['stats']
        character = {'location': 'school'}
        self.assertEqual(get_user_choice(character), 'stats')

    @patch('builtins.input')
    def test_get_user_choice_invalid_then_valid_input(self, mock_input):
        mock_input.side_effect = ['invalid', 'd']
        character = {'location': 'home'}
        self.assertEqual(get_user_choice(character), 'East')
