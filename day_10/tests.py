from unittest import TestCase

from program import solve_part_1, get_sections


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
