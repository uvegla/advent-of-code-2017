import re


def solve_part_1(puzzle_input):
    return parse(puzzle_input)


def parse(puzzle_input):
    nodes = [re.search(r'([a-z]*) \(([0-9]*)\)(?: -> )?([a-z, ]+)?.*', line).groups() for line in puzzle_input]

    return nodes


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readlines())
