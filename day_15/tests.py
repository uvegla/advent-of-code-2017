from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day15TestCase(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(65, 8921), 588)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(65, 8921), 309)
