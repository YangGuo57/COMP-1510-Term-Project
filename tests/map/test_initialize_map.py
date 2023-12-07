from unittest import TestCase
from unittest.mock import patch
from game_system.map import initialize_map


class Test(TestCase):
    @patch('game_system.map.coordinates')
    @patch('game_system.map.make_board')
    @patch('game_system.map.add_element_to_map')
    def test_initialize_map(self, mock_add_element_to_map, mock_make_board, mock_coordinates):
        mock_rows, mock_columns = 5, 5
        mock_location_key = 'test_key'
        mock_coordinates.return_value = {'test_key': {(0, 0): 'home'}}
        mock_make_board.return_value = {(0, 0): 'home'}
        mock_add_element_to_map.return_value = {(0, 0): '✦'}
        result = initialize_map(mock_rows, mock_columns, mock_location_key)
        self.assertEqual(result['rows'], mock_rows)
        self.assertEqual(result['columns'], mock_columns)
        self.assertIn('board', result)
        mock_coordinates.assert_called_once()
        mock_make_board.assert_called_once_with(mock_rows, mock_columns, mock_coordinates.return_value,
                                                mock_location_key)
        mock_add_element_to_map.assert_called_once_with(mock_make_board.return_value)
