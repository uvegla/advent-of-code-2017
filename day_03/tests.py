from unittest import TestCase

from program import solve_part_1


class Day03TestCase(TestCase):
    def test_part_1_1(self):
        self.assertEqual(solve_part_1(1), 0)

    def test_part_1_12(self):
        self.assertEqual(solve_part_1(12), 3)

    def test_part_1_23(self):
        self.assertEqual(solve_part_1(23), 2)

    def test_part_1_1024(self):
        self.assertEqual(solve_part_1(1024), 31)
