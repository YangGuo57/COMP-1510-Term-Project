from unittest import TestCase
from game_system.character import change_stat
from unittest.mock import patch


class Test(TestCase):
    def setUp(self):
        self.character = {
            'IQ': 100, 'EQ': 100, 'stress': 50, 'wealth': 1000, 'project': 0,
            'exp': {'1510': 10, '1537': 0, '1113': 0, '1712': 0},
            'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
            'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0,
                                  '1510': 0, '1537': 0, '1712': 0, '1113': 0},
            'location': 'home', 'vaccinated': False, 'skip_job': 0
        }

    @patch('game_system.character.describe_flat_stat_gain')
    def test_change_stat_increase_productive_stat(self, describe_flat_stat_gain):
        change_stat(self.character, 'IQ', 10)
        describe_flat_stat_gain(self.character, 'IQ', 10)
        self.assertEqual(self.character['IQ'], 110)

    @patch('game_system.character.describe_flat_stat_gain')
    def test_change_stat_reduce_productive_stat_to_zero(self, describe_flat_stat_gain):
        change_stat(self.character, 'IQ', -150)
        describe_flat_stat_gain(self.character, 'IQ', -150)
        self.assertEqual(self.character['IQ'], 0)

    @patch('game_system.character.describe_exp_gain')
    @patch('game_system.character.evaluate_exp')
    def test_change_stat_increase_exp_stat(self, evaluate_exp, describe_exp_gain):
        subject = '1510'
        amount = 50
        evaluate_exp(self.character, subject)
        describe_exp_gain(self.character, subject, amount)
        change_stat(self.character, subject, amount)
        self.assertEqual(self.character['exp']['1510'], 60)

    @patch('game_system.character.describe_exp_gain')
    @patch('game_system.character.evaluate_exp')
    def test_change_stat_decrease_exp_stat(self, evaluate_exp, describe_exp_gain):
        subject = '1510'
        amount = -10
        evaluate_exp(self.character, subject)
        describe_exp_gain(self.character, subject, amount)
        change_stat(self.character, subject, amount)
        self.assertEqual(self.character['exp']['1510'], 0)

    @patch('game_system.character.describe_stress_change')
    def test_change_stat_increase_stress_stat(self, describe_stress_change):
        attribute = 'stress'
        amount = 10
        describe_stress_change(self.character, amount)
        change_stat(self.character, attribute, amount)
        self.assertEqual(self.character['stress'], 60)

    @patch('game_system.character.describe_stress_change')
    def test_change_stat_reduce_stress_stat(self, describe_stress_change):
        attribute = 'stress'
        amount = -20
        describe_stress_change(self.character, amount)
        change_stat(self.character, attribute, amount)
        self.assertEqual(self.character['stress'], 30)

    @patch('game_system.character.describe_wealth_change')
    def test_change_stat_increase_wealth_stat(self, describe_wealth_change):
        attribute = 'wealth'
        amount = 500
        describe_wealth_change(self.character, amount)
        change_stat(self.character, attribute, amount)
        self.assertEqual(self.character['wealth'], 1500)

    @patch('game_system.character.describe_wealth_change')
    def test_change_stat_decrease_wealth_stat(self, describe_wealth_change):
        attribute = 'wealth'
        amount = -500
        describe_wealth_change(self.character, amount)
        change_stat(self.character, attribute, amount)
        self.assertEqual(self.character['wealth'], 500)
