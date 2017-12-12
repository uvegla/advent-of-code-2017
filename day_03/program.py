def solve_part_1(puzzle_input):
    outward = outward_distance(puzzle_input)
    sideward = sideward_distance(puzzle_input, outward)

    return outward + sideward


def outward_distance(puzzle_input):
    for i in range(1, 10000, 2):
        if i ** 2 >= puzzle_input:
            return i // 2


def sideward_distance(puzzle_input, outward):
    prev_square = 2 * (outward - 1) + 1
    start = outward + puzzle_input - prev_square ** 2

    return ping_pong_range(outward + 1, start=start).next()


def ping_pong_range(n, start=0, length=10 ** 5):
    r = range(int(n))
    ppr_list = (r + r[1:-1][::-1]) * length
    counter = int(start)
    while True:
        yield ppr_list[counter]
        counter += 1


def solve_part_2(puzzle_input):
    current = (0, 0)
    grid = {(0, 0): 1}

    outward = 0
    while True:
        outward += 1
        current = right(current)

        for direction in [up, left, down, right]:
            direction_modifier = -1 if direction == up else 0
            for step in range(0, 2 * outward + direction_modifier):
                grid[current] = calculate_field(grid, current)

                if grid[current] > puzzle_input:
                    print grid[current]
                    exit(0)

                current = direction(current)


def calculate_field(grid, current):
    return sum([grid.get(neighbour, 0) for neighbour in get_neighbours(current)])


def get_neighbours(current):
    x, y = current
    neighbours = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
                neighbours.add((x + dx, y + dy))

    return neighbours.difference(set(current))


def up(current):
    return current[0], current[1] + 1


def left(current):
    return current[0] - 1, current[1]


def down(current):
    return current[0], current[1] - 1


def right(current):
    return current[0] + 1, current[1]


if __name__ == '__main__':
    print solve_part_1(325489)
    print solve_part_2(325489)
