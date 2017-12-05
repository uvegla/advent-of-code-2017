from math import sqrt, ceil


def solve_part_1(puzzle_input):
    outward = outward_distance(puzzle_input)
    sideward = sideward_distance(puzzle_input, outward + 1)

    return outward + sideward


def outward_distance(puzzle_input):
    root_up = ceil(sqrt(puzzle_input))

    return root_up - 1 if root_up % 2 == 1 else root_up


def sideward_distance(puzzle_input, edge):
    return 0


def ping_pong_range(n, start=0, length=10 ** 5):
    r = range(n)
    ppr_list = (r + r[1:-1][::-1]) * length
    counter = start
    while True:
        yield ppr_list[counter]
        counter += 1


if __name__ == '__main__':
    solve_part_1(325489)
