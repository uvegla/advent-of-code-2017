from unittest import TestCase

from program import solve_part_1


class Day09TestCase(TestCase):
    def test_solve_part_1_example_1(self):
        self.assertEqual(solve_part_1('{}'), 1)

    def test_solve_part_1_example_2(self):
        self.assertEqual(solve_part_1('{{{}}}'), 6)

    def test_solve_part_1_example_3(self):
        self.assertEqual(solve_part_1('{{},{}}'), 5)

    def test_solve_part_1_example_4(self):
        self.assertEqual(solve_part_1('{{{},{},{{}}}}'), 16)

    def test_solve_part_1_example_5(self):
        self.assertEqual(solve_part_1('{<a>,<a>,<a>,<a>}'), 1)

    def test_solve_part_1_example_6(self):
        self.assertEqual(solve_part_1('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)

    def test_solve_part_1_example_7(self):
        self.assertEqual(solve_part_1('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)

    def test_solve_part_1_example_8(self):
        self.assertEqual(solve_part_1('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)
