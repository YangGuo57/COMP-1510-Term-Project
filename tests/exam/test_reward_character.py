from unittest import TestCase
from game_system.exam import reward_character


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
        self.subject = '1510'

    def test_reward_character_increases_exp(self):
        initial_exp = self.character['exp'][self.subject]
        reward_character(self.character, self.subject)
        self.assertGreater(self.character['exp'][self.subject], initial_exp)

    def test_reward_character_decreases_stress(self):
        initial_stress = self.character['stress']
        reward_character(self.character, self.subject)
        self.assertLess(self.character['stress'], initial_stress)
