from unittest import TestCase
from unittest.mock import patch
from helper_functions.event_trigger import confirm_entry


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_confirm_entry_enter_location(self, mock_input):
        location = 'school'
        result = confirm_entry(location)
        self.assertEqual(result, '1')
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['2'])
    def test_confirm_entry_not_enter_location(self, mock_input):
        location = 'school'
        result = confirm_entry(location)
        self.assertEqual(result, '2')
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_confirm_entry_invalid_then_valid_input(self, mock_input):
        location = 'school'
        result = confirm_entry(location)
        self.assertEqual(result, '1')
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['0', '-1', 'abc', '2'])
    def test_confirm_entry_invalid_multiple_retries_then_valid_input(self, mock_input):
        location = 'school'
        result = confirm_entry(location)
        self.assertEqual(result, '2')
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['1'])
    def test_confirm_entry_location_not_found(self, mock_input):
        location = 'gym'
        result = confirm_entry(location)
        self.assertIsNone(result)
        self.assertFalse(mock_input.called)
