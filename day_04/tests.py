from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day04TestCase(TestCase):
    def test_part_1(self):
        passphrases = [
            'aa bb cc dd ee'.split(' '),
            'aa bb cc dd aa'.split(' '),
            'aa bb cc dd aaa'.split(' ')
        ]

        self.assertEqual(solve_part_1(passphrases), 2)

    def test_part_2(self):
        passphrases = [
            'abcde fghij'.split(' '),
            'abcde xyz ecdab'.split(' '),
            'a ab abc abd abf abj'.split(' '),
            'iiii oiii ooii oooi oooo'.split(' '),
            'oiii ioii iioi iiio'.split(' ')
        ]

        self.assertEqual(solve_part_2(passphrases), 3)
