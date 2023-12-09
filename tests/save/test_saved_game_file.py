from unittest import TestCase
import pathlib


class Test(TestCase):
    def test_file_exists(self):
        dir_path = pathlib.Path(__file__).parent.resolve()
        path = dir_path / '../../saved_game.json'
        self.assertTrue(path.is_file())
