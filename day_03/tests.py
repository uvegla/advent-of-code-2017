from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day03TestCase(TestCase):
    def test_part_1_1(self):
        self.assertEqual(solve_part_1(1), 0)

    def test_part_1_12(self):
        self.assertEqual(solve_part_1(12), 3)

    def test_part_1_23(self):
        self.assertEqual(solve_part_1(23), 2)

    def test_part_1_1024(self):
        self.assertEqual(solve_part_1(1024), 31)

    def test_part_2_1(self):
        self.assertEqual(solve_part_2(1), 2)

    def test_part_2_50(self):
        self.assertEqual(solve_part_2(50), 54)

    def test_part_2_140(self):
        self.assertEqual(solve_part_2(140), 142)

    def test_part_2_350(self):
        self.assertEqual(solve_part_2(350), 351)

    def test_part_2_800(self):
        self.assertEqual(solve_part_2(800), 806)
