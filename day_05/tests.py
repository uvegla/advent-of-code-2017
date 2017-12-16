from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day05TestCase(TestCase):
    def test_part_1(self):
        puzzle_input = [0, 3, 0, 1, -3]

        self.assertEqual(solve_part_1(puzzle_input), 5)

    def test_part_2(self):
        puzzle_input = [0, 3, 0, 1, -3]

        self.assertEqual(solve_part_2(puzzle_input), 10)
