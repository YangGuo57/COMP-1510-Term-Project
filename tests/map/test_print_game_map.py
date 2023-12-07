from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from game_system.map import print_game_map


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_game_map(self, mock_stdout):
        game_map = {
            'rows': 3,
            'columns': 3,
            'board': {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                      (1, 0): ' ', (1, 1): 'H', (1, 2): ' ',
                      (2, 0): ' ', (2, 1): ' ', (2, 2): ' '}
        }
        character = {'X': 1, 'Y': 1}
        print_game_map(game_map, character)
        output = mock_stdout.getvalue()
        expected_output = "- - - \n| * | \n- - - \n"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_game_map_empty_map(self, mock_stdout):
        game_map = {'rows': 0, 'columns': 0, 'board': {}}
        character = {'X': 0, 'Y': 0}
        print_game_map(game_map, character)
        output = mock_stdout.getvalue()
        expected_output = ""
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_game_map_character_positions(self, mock_stdout):
        game_map = {
            'rows': 3,
            'columns': 3,
            'board': {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                      (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                      (2, 0): ' ', (2, 1): ' ', (2, 2): ' '}
        }
        character = {'X': 1, 'Y': 2}

        print_game_map(game_map, character)
        output = mock_stdout.getvalue()

        expected_output = "- - - \n|   * \n- - - \n"
        self.assertEqual(output, expected_output)
