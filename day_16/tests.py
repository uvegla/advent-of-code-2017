from unittest import TestCase

from program import solve_part_1


class Day16TestCase(TestCase):
    def test_solve_part_1(self):
        programs = 'abcde'
        commands = [
            's1',
            'x3/4',
            'pe/b'
        ]
        self.assertEqual(solve_part_1(programs, commands), 'baedc')
