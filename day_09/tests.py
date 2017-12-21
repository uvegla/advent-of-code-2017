from unittest import TestCase

from program import solve_part_1_and_2


class Day09TestCase(TestCase):
    def test_solve_part_1_example_1(self):
        self.assertEqual(solve_part_1_and_2('{}')[0], 1)

    def test_solve_part_1_example_2(self):
        self.assertEqual(solve_part_1_and_2('{{{}}}')[0], 6)

    def test_solve_part_1_example_3(self):
        self.assertEqual(solve_part_1_and_2('{{},{}}')[0], 5)

    def test_solve_part_1_example_4(self):
        self.assertEqual(solve_part_1_and_2('{{{},{},{{}}}}')[0], 16)

    def test_solve_part_1_example_5(self):
        self.assertEqual(solve_part_1_and_2('{<a>,<a>,<a>,<a>}')[0], 1)

    def test_solve_part_1_example_6(self):
        self.assertEqual(solve_part_1_and_2('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0], 9)

    def test_solve_part_1_example_7(self):
        self.assertEqual(solve_part_1_and_2('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0], 9)

    def test_solve_part_1_example_8(self):
        self.assertEqual(solve_part_1_and_2('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0], 3)

    def test_solve_part_2_example_1(self):
        self.assertEqual(solve_part_1_and_2('<>')[1], 0)

    def test_solve_part_2_example_2(self):
        self.assertEqual(solve_part_1_and_2('<random characters>')[1], 17)

    def test_solve_part_2_example_3(self):
        self.assertEqual(solve_part_1_and_2('<<<<>')[1], 3)

    def test_solve_part_2_example_4(self):
        self.assertEqual(solve_part_1_and_2('<{!>}>')[1], 2)

    def test_solve_part_2_example_5(self):
        self.assertEqual(solve_part_1_and_2('<!!>')[1], 0)

    def test_solve_part_2_example_6(self):
        self.assertEqual(solve_part_1_and_2('<!!!>>')[1], 0)

    def test_solve_part_2_example_7(self):
        self.assertEqual(solve_part_1_and_2('<{o"i!a,<{i<a>')[1], 10)
