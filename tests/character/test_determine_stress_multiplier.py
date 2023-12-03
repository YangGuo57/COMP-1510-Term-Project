from unittest import TestCase
from helper_functions.character import determine_stress_multiplier


class Test(TestCase):
    def test_determine_stress_multiplier_high(self):
        character = {'stress': 101}
        multiplier = determine_stress_multiplier(character)
        self.assertEqual(multiplier, 0)

    def test_determine_stress_multiplier_upper_mid(self):
        character = {'stress': 86}
        multiplier = determine_stress_multiplier(character)
        self.assertEqual(multiplier, 0.4)

    def test_determine_stress_multiplier_lower_mid(self):
        character = {'stress': 71}
        multiplier = determine_stress_multiplier(character)
        self.assertEqual(multiplier, 0.7)

    def test_determine_stress_multiplier_exact_boundary(self):
        character = {'stress': 70}
        multiplier = determine_stress_multiplier(character)
        self.assertEqual(multiplier, 1)

    def test_determine_stress_multiplier_low(self):
        character = {'stress': 69}
        multiplier = determine_stress_multiplier(character)
        self.assertEqual(multiplier, 1)
