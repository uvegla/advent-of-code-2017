from unittest import TestCase

from program import solve_part_1


class Day12TestCase(TestCase):
    def test_solve_part_1(self):
        lines = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]

        self.assertEqual(solve_part_1(lines), 6)
