from unittest import TestCase
from unittest.mock import patch
from helper_functions.event_trigger import process_movement


class Test(TestCase):
    @patch('helper_functions.movement.validate_move')
    @patch('helper_functions.movement.move_character')
    @patch('helper_functions.movement.update_visited_location')
    def test_process_movement_valid_movement(self, mock_update_visited_location, mock_move_character,
                                             mock_validate_move):
        mock_validate_move.return_value = True
        character = {'location': 'home', 'X': 1, 'Y': 2}
        game_map = {(0, 0): 'home', (0, 1): ' ', (1, 0): ' ', (1, 1): 'park'}
        user_choice = 'north'
        result = process_movement(user_choice, game_map, character)
        self.assertTrue(result)
        mock_move_character.assert_called_once()
        mock_update_visited_location.assert_called_once()

    @patch('helper_functions.movement.validate_move')
    @patch('helper_functions.movement.move_character')
    @patch('helper_functions.movement.update_visited_location')
    def test_process_movement_invalid_movement(self, mock_update_visited_location, mock_move_character,
                                               mock_validate_move):
        mock_validate_move.return_value = False
        character = {'location': 'home', 'X': 1, 'Y': 2}
        game_map = {(0, 0): 'home', (0, 1): ' ', (1, 0): ' ', (1, 1): 'park'}
        user_choice = 'south'
        result = process_movement(user_choice, game_map, character)
        self.assertFalse(result)
        mock_move_character.assert_not_called()
        mock_update_visited_location.assert_not_called()

    @patch('helper_functions.movement.validate_move')
    @patch('helper_functions.movement.move_character')
    @patch('helper_functions.movement.update_visited_location')
    def test_process_movement_out_of_bounds(self, mock_update_visited_location, mock_move_character, mock_validate_move):
        mock_validate_move.return_value = False
        character = {'location': 'home', 'X': 0, 'Y': 0}
        game_map = {(0, 0): 'home'}
        user_choice = 'west'
        result = process_movement(user_choice, game_map, character)
        self.assertFalse(result)
        mock_move_character.assert_not_called()
        mock_update_visited_location.assert_not_called()

    @patch('helper_functions.movement.validate_move')
    @patch('helper_functions.movement.move_character')
    @patch('helper_functions.movement.update_visited_location')
    def test_process_movement_stay(self, mock_update_visited_location, mock_move_character, mock_validate_move):
        mock_validate_move.return_value = True
        character = {'location': 'home', 'X': 1, 'Y': 1}
        game_map = {(1, 1): 'home'}
        user_choice = 'stay'
        result = process_movement(user_choice, game_map, character)
        self.assertTrue(result)
        mock_move_character.assert_called_once_with(character, user_choice, game_map)
        mock_update_visited_location.assert_called_once()
