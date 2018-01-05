from unittest import TestCase

from program import solve_part_1, solve_part_2


class Dat14TestCase(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1('flqrgnkx'), 8108)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2('flqrgnkx'), 1242)
