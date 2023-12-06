from unittest import TestCase
from unittest.mock import patch
from helper_functions.weekend import flea_market


class Test(TestCase):
    def setUp(self):
        self.character = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 100, 'X': 1, 'Y': 1, 'project': 0,
                          'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                          'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                          'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                          'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                          'visited_locations': {'home': 1, 'school': 1, 'hospital': 0, 'park': 0, 'work': 0, "1510": 0,
                                                "1537": 0, "1712": 0, "1113": 0},
                          'location': 'home', 'vaccinated': False, 'skip_job': 0}

    @patch('builtins.print')
    def test_flea_market_not_enter(self, mock_print):
        with patch('builtins.input', return_value='2'):
            result = flea_market(self.character)
            self.assertFalse(result)
            mock_print.assert_called_with("You decide to keep walking.")

    @patch('builtins.print')
    @patch('random.randint', return_value=12)
    def test_flea_market_enter_with_sufficient_wealth(self, mock_randint, mock_print):
        with patch('builtins.input', return_value='1'):
            flea_market(self.character)

            self.assertEqual(self.character['wealth'], 40)
            self.assertEqual(self.character['IQ'], 0.5)
            mock_print.assert_called_with("Your IQ increases by 0.5. It is now 0.5.")
            mock_randint.assert_called_once()

    @patch('builtins.print')
    @patch('random.randint', return_value=12)
    def test_flea_market_enter_with_insufficient_wealth(self, mock_randint, mock_print):
        self.character['wealth'] = 50
        with patch('builtins.input', return_value='1'):
            flea_market(self.character)

            self.assertEqual(self.character['wealth'], 50)
            self.assertTrue(10 <= self.character['stress'] <= 15)
            mock_print.assert_called_with("Your stress level is now 12.")
            mock_randint.assert_called_once_with(10, 15)
