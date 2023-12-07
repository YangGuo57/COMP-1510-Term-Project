from unittest import TestCase
from game_system.character import set_character_location


class Test(TestCase):
    def test_set_character_location_empty_string(self):
        character = {'location': 'home'}
        set_character_location(character, '')
        self.assertEqual(character['location'], '')

    def test_set_character_location_successfully(self):
        character = {'location': 'home'}
        set_character_location(character, 'hospital')
        self.assertEqual(character['location'], 'hospital')
