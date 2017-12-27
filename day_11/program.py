from functools import reduce

DIRECTIONS = {
    'n': (-1, 1),
    'ne': (0, 1),
    'se': (1, 0),
    's': (1, -1),
    'sw': (0, -1),
    'nw': (-1, 0)
}


def solve_part_1(puzzle_input):
    position = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), [DIRECTIONS[x] for x in puzzle_input])

    return max(abs(position[0]), abs(position[1]))


if __name__ == '__main__':
    line = open('input.txt').readline().split(',')
    print solve_part_1(line)
