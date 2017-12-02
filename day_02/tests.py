from unittest import TestCase

from program import solve_part_1, solve_part_2


class Day02TestCase(TestCase):
    def test_solve_part_1(self):
        puzzle_input = [
            '5\t1\t9\t5',
            '7\t5\t3',
            '2\t4\t6\t8'
        ]

        self.assertEqual(solve_part_1(puzzle_input), 18)

    def test_solve_part_2(self):
        puzzle_input = [
            '5\t9\t2\t8',
            '9\t4\t7\t3',
            '3\t8\t6\t5'
        ]

        self.assertEqual(solve_part_2(puzzle_input), 9)
