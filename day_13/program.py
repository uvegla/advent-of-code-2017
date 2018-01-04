import re
import itertools


def generic(puzzle_input, delay=0):
    apprehends = []

    for depth in range(max(puzzle_input.keys()) + 1):
        if depth in puzzle_input and collides(depth + delay, puzzle_input[depth]):
            apprehends.append((depth, puzzle_input[depth]))

    return apprehends


def collides(depth, rng):
    return depth % (2 * rng - 2) == 0


def parse(lines):
    return {int(depth): int(rng) for (depth, rng) in [re.search(r'(\d+): (\d+)', line).groups() for line in lines]}


def solve_part_1(puzzle_input):
    return sum([depth * rng for (depth, rng) in generic(puzzle_input)])


def solve_part_2(puzzle_input):
    for i in itertools.count():
        if len(generic(puzzle_input, i)) == 0:
            return i


if __name__ == '__main__':
    parsed_input = parse(open('input.txt').readlines())

    print solve_part_1(parsed_input)
    print solve_part_2(parsed_input)
