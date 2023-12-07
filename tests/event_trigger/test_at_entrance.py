from unittest import TestCase
from unittest.mock import patch
from game_system.event_trigger import at_entrance


class Test(TestCase):

    def setUp(self):
        self.mock_map_data = {
            "door": {
                "main": {"home": (2, 3),
                         "school": (3, 9),
                         "hospital": (6, 12),
                         "park": (2, 15),
                         "work": (7, 4)},
                "school": {
                    "1510": (2, 6),
                    "1537": (10, 6),
                    "1712": (7, 6),
                    "1113": (4, 6),
                }
            }
        }

    @patch('game_system.map.coordinates')
    def test_character_not_at_entrance(self, mock_coordinates):
        mock_coordinates.return_value = self.mock_map_data
        character = {'location': 'outside', 'X': 1, 'Y': 2}
        self.assertIsNone(at_entrance(character))

    @patch('game_system.map.coordinates')
    def test_character_at_school_entrance_1537(self, mock_coordinates):
        mock_coordinates.return_value = self.mock_map_data
        character = {'location': 'school', 'X': 10, 'Y': 6}
        self.assertEqual(at_entrance(character), '1537')

    @patch('game_system.map.coordinates')
    def test_character_not_matching_any_entrance(self, mock_coordinates):
        mock_coordinates.return_value = self.mock_map_data
        character = {'location': 'outside', 'X': 8, 'Y': 8}
        self.assertIsNone(at_entrance(character))

    @patch('game_system.map.coordinates')
    def test_character_missing_coordinates(self, mock_coordinates):
        mock_coordinates.return_value = self.mock_map_data
        character = {'location': 'outside'}
        with self.assertRaises(KeyError):
            at_entrance(character)
