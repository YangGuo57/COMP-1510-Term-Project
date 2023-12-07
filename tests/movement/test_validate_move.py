from unittest import TestCase
from game_system.movement import validate_move


class Test(TestCase):
    def setUp(self):
        self.game_board = {(0, 0): ' ', (0, 1): ' ', (1, 0): ' ', (1, 1): ' '}

    def test_validate_move_north_valid(self):
        player = {'X': 1, 'Y': 0}
        direction = 'North'
        self.assertTrue(validate_move(self.game_board, player, direction))

    def test_validate_move_north_invalid(self):
        player = {'X': 0, 'Y': 0}
        direction = 'North'
        self.assertFalse(validate_move(self.game_board, player, direction))

    def test_validate_move_south_valid(self):
        player = {'X': 0, 'Y': 0}
        direction = 'South'
        self.assertTrue(validate_move(self.game_board, player, direction))

    def test_validate_move_south_invalid(self):
        player = {'X': 1, 'Y': 1}
        direction = 'South'
        self.assertFalse(validate_move(self.game_board, player, direction))

    def test_validate_move_east_valid(self):
        player = {'X': 0, 'Y': 0}
        direction = 'East'
        self.assertTrue(validate_move(self.game_board, player, direction))

    def test_validate_move_east_invalid(self):
        player = {'X': 1, 'Y': 1}
        direction = 'East'
        self.assertFalse(validate_move(self.game_board, player, direction))

    def test_validate_move_west_valid(self):
        player = {'X': 1, 'Y': 1}
        direction = 'West'
        self.assertTrue(validate_move(self.game_board, player, direction))

    def test_validate_move_west_invalid(self):
        player = {'X': 0, 'Y': 0}
        direction = 'West'
        self.assertFalse(validate_move(self.game_board, player, direction))
