from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day13TestCase(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1({0: 3, 1: 2, 4: 4, 6: 4}), 24)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2({0: 3, 1: 2, 4: 4, 6: 4}), 10)
