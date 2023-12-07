from unittest import TestCase
from unittest.mock import patch
from helper_functions.weekend import weekend_school


class Test(TestCase):
    def setUp(self):
        self.character = {'EQ': 0, 'stress': 12}

    @patch('builtins.print')
    @patch('random.randint')
    def test_weekend_school_with_party(self, mock_randint, mock_print):
        mock_randint.side_effect = [1, 12, 2]

        def mock_change_stat(character, key, value):
            character[key] = max(0, character[key] + value)

        with patch('helper_functions.character.change_stat', new=mock_change_stat):
            weekend_school(self.character)
        self.assertEqual(self.character['EQ'], 2)
        self.assertEqual(self.character['stress'], 0)
        mock_randint.assert_called()
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('random.randint')
    def test_weekend_school_with_hobo(self, mock_randint, mock_print):
        mock_randint.side_effect = [2, 13, 2]

        def mock_change_stat(character, key, value):
            character[key] += value

        with patch('helper_functions.character.change_stat', new=mock_change_stat):
            weekend_school(self.character)
        self.assertEqual(self.character['EQ'], 2)
        self.assertEqual(self.character['stress'], 25)
        mock_randint.assert_called()
        mock_print.assert_called()
