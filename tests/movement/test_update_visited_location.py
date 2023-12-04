from unittest import TestCase
from unittest.mock import patch
from helper_functions.movement import update_visited_location


class Test(TestCase):

    @patch('helper_functions.map.coordinates')
    def test_update_visited_location_at_school(self, mock_coordinates):
        mock_coordinates.return_value = {'door': {'main': {'school': (1, 1)}}}
        player = {'X': 1, 'Y': 1, 'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0}}
        update_visited_location(player)
        expected = {'home': 1, 'school': 2, 'hospital': 0, 'park': 0}
        actual = player['visited_locations']
        self.assertEqual(actual, expected)

    @patch('helper_functions.map.coordinates')
    def test_update_visited_location_at_home(self, mock_coordinates):
        mock_coordinates.return_value = {'door': {'main': {'home': (0, 0)}}}
        player = {'X': 0, 'Y': 0, 'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0}}
        update_visited_location(player)
        expected = {'home': 2, 'school': 1, 'hospital': 0, 'park': 0}
        self.assertEqual(player['visited_locations'], expected)

    @patch('helper_functions.map.coordinates')
    def test_update_visited_location_multiple_calls(self, mock_coordinates):
        mock_coordinates.return_value = {'door': {'main': {'school': (1, 1)}}}
        player = {'X': 1, 'Y': 1, 'visited_locations': {'home': 1, 'school': 1}}
        update_visited_location(player)
        update_visited_location(player)
        expected = {'home': 1, 'school': 3}
        self.assertEqual(player['visited_locations'], expected)

    @patch('helper_functions.map.coordinates')
    def test_update_visited_location_no_visited(self, mock_coordinates):
        mock_coordinates.return_value = {'door': {'main': {'school': (2, 2), 'home': (3, 3)}}}
        player = {'X': 1, 'Y': 1, 'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0}}
        update_visited_location(player)
        expected = {'home': 1, 'school': 1, 'hospital': 0, 'park': 0}
        actual = player['visited_locations']
        self.assertEqual(actual, expected)
