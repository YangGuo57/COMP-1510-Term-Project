import io
from unittest import TestCase
from unittest.mock import patch
from game_system.character import print_stats


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_stats(self, mock_stdout):
        character = {
            'IQ': 5, 'EQ': 6, 'stress': 2, 'wealth': 10000, 'project': 50,
            'exp': {'1712': 3, '1510': 5},
            'lvl': {'1510': 2, '1537': 4},
            'job': False
        }
        expected_output = (
            "Your current attributes:\n"
            "    IQ: 5\n"
            "    EQ: 6\n"
            "    stress: 2\n"
            "    wealth: 10000\n"
            "    experience in each course:\n"
            "        COMP1712: 3\n"
            "        COMP1510: 5\n"
            "    level in each course:\n"
            "        COMP1510: 2\n"
            "        COMP1537: 4\n"
            "    personal project progress: 50\n\n"
        )
        print_stats(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
