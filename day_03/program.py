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


if __name__ == '__main__':
    print solve_part_1(325489)
