from unittest import TestCase
import pathlib


class Test(TestCase):
    def test_file_exists(self):
        path = pathlib.Path('../../saved_game.json')
        self.assertTrue(path.is_file())
