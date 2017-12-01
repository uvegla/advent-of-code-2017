from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day01TestCase(TestCase):
    def test_solve_part_1_1122(self):
        self.assertEqual(solve_part_1('1122'), 3)

    def test_solve_part_1_1111(self):
        self.assertEqual(solve_part_1('1111'), 4)

    def test_solve_part_1_1234(self):
        self.assertEqual(solve_part_1('1234'), 0)

    def test_solve_part_1_91212129(self):
        self.assertEqual(solve_part_1('91212129'), 9)

    def test_solve_part_2_1212(self):
        self.assertEqual(solve_part_2('1212'), 6)

    def test_solve_part_2_1221(self):
        self.assertEqual(solve_part_2('1221'), 0)

    def test_solve_part_2_123425(self):
        self.assertEqual(solve_part_2('123425'), 4)

    def test_solve_part_2_123123(self):
        self.assertEqual(solve_part_2('123123'), 12)

    def test_solve_part_2_12131415(self):
        self.assertEqual(solve_part_2('12131415'), 4)
