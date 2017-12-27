from unittest import TestCase

from program import solve_part_1


class Day11TestCase(TestCase):
    def test_solve_part_1_example_1(self):
        self.assertEqual(solve_part_1(['ne', 'ne', 'ne']), 3)

    def test_solve_part_1_example_2(self):
        self.assertEqual(solve_part_1(['ne', 'ne', 'sw', 'sw']), 0)

    def test_solve_part_1_example_3(self):
        self.assertEqual(solve_part_1(['ne', 'ne', 's', 's']), 2)

    def test_solve_part_1_example_4(self):
        self.assertEqual(solve_part_1(['se', 'sw', 'se', 'sw', 'sw']), 3)
