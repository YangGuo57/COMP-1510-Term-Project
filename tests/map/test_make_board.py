from unittest import TestCase
from game_system.map import make_board


class Test(TestCase):
    def test_make_board_typical_case(self):
        result = make_board(2, 2, {'key': {(0, 0): 'home', (1, 1): 'park'}}, 'key')
        expected = {(0, 0): 'home', (0, 1): ' ', (1, 0): ' ', (1, 1): 'park'}
        self.assertEqual(result, expected)

    def test_make_board_single_cell_board(self):
        result = make_board(1, 1, {'key': {(0, 0): 'home'}}, 'key')
        expected = {(0, 0): 'home'}
        self.assertEqual(result, expected)

    def test_make_board_no_rows_or_columns(self):
        result = make_board(0, 0, {'key': {}}, 'key')
        expected = {}
        self.assertEqual(result, expected)

    def test_make_board_rows_zero(self):
        result = make_board(0, 2, {'key': {(0, 0): 'home'}}, 'key')
        expected = {}
        self.assertEqual(result, expected)

    def test_make_board_columns_zero(self):
        result = make_board(2, 0, {'key': {(0, 0): 'home'}}, 'key')
        expected = {}
        self.assertEqual(result, expected)

    def test_make_board_non_continuous_locations(self):
        result = make_board(3, 3, {'key': {(0, 0): 'home', (2, 2): 'park'}}, 'key')
        expected = {(0, 0): 'home', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): 'park'}
        self.assertEqual(result, expected)
