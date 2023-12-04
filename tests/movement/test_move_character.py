from unittest import TestCase
from helper_functions.movement import move_character


class Test(TestCase):

    def test_move_character_north(self):
        player = {'X': 2, 'Y': 2}
        map_game = {'rows': 3,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', }
        move_character(player, 'North', map_game)
        self.assertEqual(player['X'], 1)
        self.assertEqual(player['Y'], 2)

    def test_move_character_east(self):
        player = {'X': 1, 'Y': 1}
        map_game = {'rows': 3,
                    'columns': 4,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ', (0, 3): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ', (1, 3): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', (2, 3): ' '}
        move_character(player, 'East', map_game)
        self.assertEqual(player['X'], 1)
        self.assertEqual(player['Y'], 2)

    def test_move_character_south_(self):
        player = {'X': 1, 'Y': 1}
        map_game = {'rows': 4,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ',
                    (3, 0): ' ', (3, 1): ' ', (3, 2): ' ', }
        move_character(player, 'South', map_game)
        self.assertEqual(player['X'], 2)
        self.assertEqual(player['Y'], 1)

    def test_move_character_west(self):
        player = {'X': 1, 'Y': 2}
        map_game = {'rows': 3,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', }
        move_character(player, 'West', map_game)
        self.assertEqual(player['X'], 1)
        self.assertEqual(player['Y'], 1)

    def test_move_character_hit_north_wall(self):
        player = {'X': 1, 'Y': 1}
        map_game = {'rows': 3,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', }
        move_character(player, 'North', map_game)
        self.assertEqual(player['X'], 1)
        self.assertEqual(player['Y'], 1)

    def test_move_character_hit_south_wall(self):
        player = {'X': 2, 'Y': 1}
        map_game = {'rows': 3,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', }
        move_character(player, 'South', map_game)
        self.assertEqual(player['X'], 2)
        self.assertEqual(player['Y'], 1)

    def test_move_character_hit_west_wall(self):
        player = {'X': 1, 'Y': 1}
        map_game = {'rows': 3,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', }
        move_character(player, 'West', map_game)
        self.assertEqual(player['X'], 1)
        self.assertEqual(player['Y'], 1)

    def test_move_character_hit_east_wall(self):
        player = {'X': 1, 'Y': 1}
        map_game = {'rows': 3,
                    'columns': 3,
                    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
                    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
                    (2, 0): ' ', (2, 1): ' ', (2, 2): ' ', }
        move_character(player, 'East', map_game)
        self.assertEqual(player['X'], 1)
        self.assertEqual(player['Y'], 1)
