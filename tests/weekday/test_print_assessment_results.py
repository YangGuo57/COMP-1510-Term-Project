from unittest import TestCase
from helper_functions.weekday import print_assessment_results
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pass_quiz(self, mock_output):
        print_assessment_results(False, '1510', 'quiz')
        system_print = mock_output.getvalue()
        expected_print = ('Hurrah! You aced the COMP1510 quiz. All those tearful all-nighters were not for '
                          'naught!\n')
        self.assertEqual(system_print, expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fail_quiz(self, mock_output):
        print_assessment_results(True, '1510', 'quiz')
        system_print = mock_output.getvalue()
        expected_print = 'You completely bombed the COMP1510 quiz. Perhaps you should study harder.\n'
        self.assertEqual(system_print, expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fail_assignment(self, mock_output):
        print_assessment_results(True, '1510', 'assignment')
        system_print = mock_output.getvalue()
        expected_print = 'You completely bombed the COMP1510 assignment. Perhaps you should study harder.\n'
        self.assertEqual(system_print, expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pass_assignment(self, mock_output):
        print_assessment_results(False, '1510', 'assignment')
        system_print = mock_output.getvalue()
        expected_print = ('Hurrah! You aced the COMP1510 assignment. All those tearful all-nighters were not for '
                          'naught!\n')
        self.assertEqual(system_print, expected_print)
