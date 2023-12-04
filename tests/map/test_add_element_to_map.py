from unittest import TestCase
from helper_functions.map import add_element_to_map


class Test(TestCase):

    def test_add_element_to_map_empty_map(self):
        board = {}
        expected = {}
        result = add_element_to_map(board)
        self.assertEqual(result, expected)

    def test_add_element_to_map_single_element_map(self):
        board = {(0, 0): 'home'}
        expected = {
            (0, 0): '✦', (-1, -1): '-', (-1, 0): '-', (-1, 1): '-',
            (0, -1): '|', (0, 1): '-', (1, -1): '-', (1, 0): '-', (1, 1): '-'
        }
        result = add_element_to_map(board)
        self.assertEqual(result, expected)

    def test_add_element_to_multiple_elements(self):
        board = {(0, 0): 'home', (2, 2): 'park'}
        expected = {
            (0, 0): '✦', (-1, -1): '-', (-1, 0): '-', (-1, 1): '-',
            (0, -1): '|', (0, 1): '-', (1, -1): '-', (1, 0): '-', (1, 1): '-',
            (2, 2): 'P', (1, 1): '-', (1, 2): '-', (1, 3): '-',
            (2, 1): '|', (2, 3): '-', (3, 1): '-', (3, 2): '-', (3, 3): '-'
        }
        result = add_element_to_map(board)
        self.assertEqual(result, expected)
