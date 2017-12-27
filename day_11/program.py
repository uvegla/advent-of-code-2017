DIRECTIONS = {
    'n': (-1, 1),
    'ne': (0, 1),
    'se': (1, 0),
    's': (1, -1),
    'sw': (0, -1),
    'nw': (-1, 0)
}


def solve_part_1_and_2(puzzle_input):
    max_distance, position = 0, (0, 0)

    for direction in puzzle_input:
        position = step(position, DIRECTIONS[direction])
        max_distance = max(max_distance, distance(position))

    return distance(position), max_distance


def step(x, y):
    return x[0] + y[0], x[1] + y[1]


def distance(position):
    return max(abs(position[0]), abs(position[1]))


if __name__ == '__main__':
    line = open('input.txt').readline().split(',')

    print solve_part_1_and_2(line)
