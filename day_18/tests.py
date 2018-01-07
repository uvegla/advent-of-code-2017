from unittest import TestCase

from program import solve_part_1


class Day18TestCase(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1([
            'set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2'
        ]), 4)
