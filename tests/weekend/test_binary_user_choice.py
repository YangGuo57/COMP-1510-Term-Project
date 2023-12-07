from unittest import TestCase
from game_system.weekend import binary_user_choice
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_confirm(self, _):
        result = '1'
        self.assertEqual(result, binary_user_choice('hospital'))

    @patch('builtins.input', side_effect=['2'])
    def test_refuse(self, _):
        result = '2'
        self.assertEqual(result, binary_user_choice('hospital'))

    @patch('builtins.input', side_effect=['s', '@', '1'])
    def test_invalid_invalid_confirm(self, _):
        result = '1'
        self.assertEqual(result, binary_user_choice('hospital'))

    @patch('builtins.input', side_effect=[' ', '!', '2'])
    def test_invalid_invalid_refuse(self, _):
        result = '2'
        self.assertEqual(result, binary_user_choice('hospital'))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_print_confirm_in_hospital_setting(self, _, mock_output):
        binary_user_choice('hospital')
        system_print = mock_output.getvalue()
        expected = ('"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the '
                    'way, the lineup for getting your vaccine is this way."\nShe grabs you by your arm and tries to '
                    'lead you deeper into the hospital.\nThe nurse jabs you with a needle. Ouch. Surely this won\'t '
                    'make you autistic right?\n')
        self.assertEqual(system_print, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['@', '1'])
    def test_one_invalid_input_hospital(self, _, mock_output):
        binary_user_choice('hospital')
        system_print = mock_output.getvalue()
        expected = ('"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the '
                    'way, the lineup for getting your vaccine is this way."\nShe grabs you by your arm and tries to '
                    'lead you deeper into the hospital.\n'
                    'That is not a valid command.\n'
                    '"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the '
                    'way, the lineup for getting your vaccine is this way."\nShe grabs you by your arm and tries to '
                    'lead you deeper into the hospital.\n'
                    'The nurse jabs you with a needle. Ouch. Surely this won\'t make you autistic right?\n')
        self.assertEqual(system_print, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['@', ' ', '1'])
    def test_two_invalid_input_hospital(self, _, mock_output):
        binary_user_choice('hospital')
        system_print = mock_output.getvalue()
        expected = ('"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the '
                    'way, the lineup for getting your vaccine is this way."\nShe grabs you by your arm and tries to '
                    'lead you deeper into the hospital.\n'
                    'That is not a valid command.\n'
                    '"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the '
                    'way, the lineup for getting your vaccine is this way."\nShe grabs you by your arm and tries to '
                    'lead you deeper into the hospital.\n'
                    'That is not a valid command.\n'
                    '"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the '
                    'way, the lineup for getting your vaccine is this way."\nShe grabs you by your arm and tries to '
                    'lead you deeper into the hospital.\n'
                    'The nurse jabs you with a needle. Ouch. Surely this won\'t make you autistic right?\n')
        self.assertEqual(system_print, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_print_confirm_in_home_setting(self, _, mock_output):
        binary_user_choice('home')
        system_print = mock_output.getvalue()
        expected = ('Your desk and your laptop patiently await your presence, ready for a productive session. Yet, '
                    'your bed is whispering your name like a neglected girlfriend. What do you do?\n')
        self.assertEqual(system_print, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['A', '1'])
    def test_print_invalid_then_confirm_in_home_setting(self, _, mock_output):
        binary_user_choice('home')
        system_print = mock_output.getvalue()
        expected = ('Your desk and your laptop patiently await your presence, ready for a productive session. Yet, '
                    'your bed is whispering your name like a neglected girlfriend. What do you do?\n'
                    'That is not a valid command.\n'
                    'Your desk and your laptop patiently await your presence, ready for a productive session. Yet, '
                    'your bed is whispering your name like a neglected girlfriend. What do you do?\n')
        self.assertEqual(system_print, expected)
