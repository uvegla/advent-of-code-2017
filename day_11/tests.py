from unittest import TestCase

from program import solve_part_1_and_2


class Day11TestCase(TestCase):
    def test_solve_part_1_example_1(self):
        self.assertEqual(solve_part_1_and_2(['ne', 'ne', 'ne'])[0], 3)

    def test_solve_part_1_example_2(self):
        self.assertEqual(solve_part_1_and_2(['ne', 'ne', 'sw', 'sw'])[0], 0)

    def test_solve_part_1_example_3(self):
        self.assertEqual(solve_part_1_and_2(['ne', 'ne', 's', 's'])[0], 2)

    def test_solve_part_1_example_4(self):
        self.assertEqual(solve_part_1_and_2(['se', 'sw', 'se', 'sw', 'sw'])[0], 3)
