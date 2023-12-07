from unittest import TestCase
from game_system.exam import evaluate_exam


class Test(TestCase):
    def test_evaluate_exam_midterm_fail(self):
        character = {'lvl': {'1510': 1}}
        result = evaluate_exam(character, '1510', 'midterm')
        self.assertEqual(result, 'F')

    def test_evaluate_exam_midterm_pass(self):
        character = {'lvl': {'1510': 2}}
        result = evaluate_exam(character, '1510', 'midterm')
        self.assertEqual(result, 'C')

    def test_final_fail(self):
        character = {'lvl': {'1510': 1}}
        result = evaluate_exam(character, '1510', 'final')
        self.assertEqual(result, 'F')

    def test_evaluate_exam_final_pass(self):
        character = {'lvl': {'1510': 4}}
        result = evaluate_exam(character, '1510', 'final')
        self.assertEqual(result, 'C')

    def test_evaluate_exam_multiple_subjects_pass(self):
        character = {'lvl': {'1510': 2, '1511': 3}}
        result = evaluate_exam(character, '1511', 'midterm')
        self.assertEqual(result, 'B')

    def test_evaluate_exam_multiple_subjects_fail(self):
        character = {'lvl': {'1510': 1, '1511': 1}}
        result = evaluate_exam(character, '1511', 'midterm')
        self.assertEqual(result, 'F')
