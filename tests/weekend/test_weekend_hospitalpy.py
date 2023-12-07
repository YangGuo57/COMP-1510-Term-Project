from unittest import TestCase
from unittest.mock import patch
from game_system.weekend import weekend_hospital


class Test(TestCase):
    def setUp(self):
        self.character = {'IQ': 0, 'vaccinated': False}

    @patch('builtins.print')
    @patch('game_system.weekend.binary_user_choice', return_value='1')
    def test_weekend_hospital_not_vaccinated(self, mock_user_choice, mock_print):
        def mock_change_stat(character, key, value):
            character[key] += value

        with patch('game_system.character.change_stat', new=mock_change_stat):
            weekend_hospital(self.character)
        self.assertEqual(self.character['IQ'], 1)
        self.assertTrue(self.character['vaccinated'])
        mock_user_choice.assert_called_once_with('hospital')
        mock_print.assert_called()

    @patch('builtins.print')
    def test_weekend_hospital_already_vaccinated(self, mock_print):
        self.character['vaccinated'] = True
        weekend_hospital(self.character)
        self.assertEqual(self.character['IQ'], 0)
        mock_print.assert_called()
