import re


def solve_part_1(puzzle_input):
    severity = 0

    for depth in range(max(puzzle_input.keys()) + 1):
        if depth in puzzle_input and collides(depth, puzzle_input[depth]):
            severity += depth * puzzle_input[depth]

    return severity


def collides(depth, rng):
    return depth % (2 * rng - 2) == 0


def parse(lines):
    return {int(depth): int(rng) for (depth, rng) in [re.search(r'(\d+): (\d+)', line).groups() for line in lines]}


if __name__ == '__main__':
    print solve_part_1(parse(open('input.txt').readlines()))
