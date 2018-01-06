from unittest import TestCase

from program import solve_part_1


class Day17TestCase(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(3), 638)
