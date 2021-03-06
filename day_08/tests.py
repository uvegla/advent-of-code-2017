from unittest import TestCase

from program import solve_part_1_and_2


class Day08TestCase(TestCase):
    def test_solve_part_1_and_2(self):
        lines = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]

        self.assertEqual(solve_part_1_and_2(lines), (1, 10))
