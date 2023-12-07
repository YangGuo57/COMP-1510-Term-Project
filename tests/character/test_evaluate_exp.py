from unittest import TestCase
from game_system.character import evaluate_exp


class Test(TestCase):
    def test_evaluate_exp_1510_level_up(self):
        player = {'exp': {'1510': 200}, 'lvl': {'1510': 1}}
        course = '1510'
        evaluate_exp(player, course)
        self.assertEqual(player['lvl']['1510'], 2)

    def test_evaluate_exp_1537_level_up(self):
        player = {'exp': {'1537': 200}, 'lvl': {'1537': 1}}
        course = '1537'
        evaluate_exp(player, course)
        self.assertEqual(player['lvl']['1537'], 2)

    def test_evaluate_exp_1712_level_up(self):
        player = {'exp': {'1712': 200}, 'lvl': {'1712': 1}}
        course = '1712'
        evaluate_exp(player, course)
        self.assertEqual(player['lvl']['1712'], 2)

    def test_evaluate_exp_1113_level_up(self):
        player = {'exp': {'1113': 200}, 'lvl': {'1113': 1}}
        course = '1113'
        evaluate_exp(player, course)
        self.assertEqual(player['lvl']['1113'], 2)

    def test_evaluate_exp_single_subject_no_level_up(self):
        player = {'exp': {'1510': 50}, 'lvl': {'1510': 1}}
        course = '1510'
        evaluate_exp(player, course)
        self.assertEqual(player['lvl']['1510'], 1)

    def test_evaluate_exp_multiple_subjects_level_up(self):
        player = {'exp': {'1510': 200, '1537': 300, '1113': 250, '1712': 345},
                  'lvl': {'1510': 1, '1537': 2, '1113': 1, '1712': 1}}
        evaluate_exp(player, 'all')
        self.assertEqual(player['lvl']['1510'], 2)
        self.assertEqual(player['lvl']['1537'], 3)
        self.assertEqual(player['lvl']['1113'], 2)
        self.assertEqual(player['lvl']['1712'], 2)
