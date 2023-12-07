from unittest import TestCase
from game_system.weekday import print_epiphany_office_hours
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_epiphany(self, mock_output):
        print_epiphany_office_hours('1510', True)
        system_print = mock_output.getvalue()
        expected_print = ('Your COMP1510 instructor graciously imparts their wisdom on you. You absorb all this wisdom '
                          'like a sponge.\n')
        self.assertEqual(system_print, expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_no_epiphany(self, mock_output):
        print_epiphany_office_hours('1510', False)
        system_print = mock_output.getvalue()
        expected_print = ('Your COMP1510 instructor graciously imparts their wisdom on you, but Alas, your brain '
                          'struggles to absorb all this wisdom.\n')
        self.assertEqual(system_print, expected_print)
