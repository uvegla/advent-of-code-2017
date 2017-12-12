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

    # def test_part_2_1(self):
    #     self.assertEqual(solve_part_2(1), 1)
    #
    # def test_part_2_2(self):
    #     self.assertEqual(solve_part_2(2), 1)
    #
    # def test_part_2_3(self):
    #     self.assertEqual(solve_part_2(3), 2)
    #
    # def test_part_2_4(self):
    #     self.assertEqual(solve_part_2(4), 4)
    #
    # def test_part_2_5(self):
    #     self.assertEqual(solve_part_2(5), 15)
    #
    # def test_part_2_10(self):
    #     self.assertEqual(solve_part_2(10), 26)
    #
    # def test_part_2_16(self):
    #     self.assertEqual(solve_part_2(16), 142)
