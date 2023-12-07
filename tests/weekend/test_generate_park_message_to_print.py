from unittest import TestCase
from game_system.weekend import generate_park_message_to_print


class Test(TestCase):
    def test_generate_park_message_to_print_fresh_air_message(self):
        self.assertEqual(generate_park_message_to_print(1),
                         'Taking a deep breath of the fresh air in Stanley Park helps ease your anxiety as '
                         'you walk.')
        self.assertEqual(generate_park_message_to_print(4),
                         'Taking a deep breath of the fresh air in Stanley Park helps ease your anxiety as '
                         'you walk.')

    def test_generate_park_message_to_print_stray_cat_message(self):
        expected_message = ('A stray cat approaches, meowing softly. You give it a gentle tummy rub, and it responds '
                            'with happy purring. Seeing this carefree, adorable little creature revel in the simple '
                            'joys of life inspires you to adopt a similar mentality.')
        self.assertEqual(generate_park_message_to_print(5), expected_message)
        self.assertEqual(generate_park_message_to_print(6), expected_message)

    def test_generate_park_message_to_print_flea_market_message(self):
        expected_message = {
            'default': 'It seems there is a weekend flea market going on today at Stanley Park. Should you '
                       'go check it out?\nEnter "1" to check out the flea market, "2" to continue walking.',
            'enter flea': 'You decide to explore the flea market.',
            'kool-aid': 'An eccentric old lady grabs you and pulls you to her stall, excitedly pitching her '
                        '"Mega Brain Power Elixir" to you. She claims it can turn even the dumbest person '
                        'into a genius. Despite your attempts to leave, she\'s persistent. Feeling cornered, '
                        'you give in and buy a ridiculously expensive bottle of the mysterious liquid. '
                        'You chug it down. Hmmmm... kinda tastes like Kool-Aid.',
            'no kool-aid': 'You see so many things you want to buy. You reach for your wallet, but Alas, '
                           'there\'s no money inside. The sight of your empty wallet makes you sad. With a '
                           'sigh, you turn around and leave the park.',
            'leave flea': 'You decide to keep walking.'}
        self.assertEqual(generate_park_message_to_print(7), expected_message)
        self.assertEqual(generate_park_message_to_print(8), expected_message)

    def test_generate_park_message_to_print_money_found_message(self):
        self.assertEqual(generate_park_message_to_print(9), 'How lucky! You find some money on the ground!')
        self.assertEqual(generate_park_message_to_print(10), 'How lucky! You find some money on the ground!')
