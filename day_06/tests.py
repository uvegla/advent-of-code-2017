from unittest import TestCase

from program import solve_part_1_and_2


class Day06TestCase(TestCase):
    def test_part_1(self):
        puzzle_input = [0, 2, 7, 0]

        loops, resurface = solve_part_1_and_2(puzzle_input)

        self.assertEqual(loops, 5)
        self.assertEqual(resurface, 4)
