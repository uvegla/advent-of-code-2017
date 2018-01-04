from unittest import TestCase

from utils.knot_hash import get_sections

from program import solve_part_1, solve_part_2


class Day10TestCase(TestCase):
    def test_get_sections_no_overflow(self):
        s_1, s_2 = get_sections(range(5), 0, 3)

        self.assertEqual(s_1, (0, 3))
        self.assertEqual(s_2, (0, 0))

    def test_get_sections_to_limit(self):
        s_1, s_2 = get_sections(range(5), 1, 4)

        self.assertEqual(s_1, (1, 5))
        self.assertEqual(s_2, (0, 0))

    def test_get_sections_with_overflow(self):
        s_1, s_2 = get_sections(range(5), 4, 3)

        self.assertEqual(s_1, (4, 5))
        self.assertEqual(s_2, (0, 2))

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(range(5), [3, 4, 1, 5]), 12)

    def test_solve_part_2_example_1(self):
        self.assertEqual(solve_part_2(''), 'a2582a3a0e66e6e86e3812dcb672a272')

    def test_solve_part_2_example_2(self):
        self.assertEqual(solve_part_2('AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')

    def test_solve_part_2_example_3(self):
        self.assertEqual(solve_part_2('1,2,3'), '3efbe78a8d82f29979031a4aa0b16a9d')

    def test_solve_part_2_example_4(self):
        self.assertEqual(solve_part_2('1,2,4'), '63960835bcdc130f0b66d7ff4f6a5a8e')
