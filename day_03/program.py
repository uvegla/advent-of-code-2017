def solve_part_1(puzzle_input):
    if puzzle_input == 1:
        return 0

    outward = outward_distance(puzzle_input)
    sideward = sideward_distance(puzzle_input, outward)

    return outward + sideward


def outward_distance(puzzle_input):
    for i in range(1, 10000, 2):
        if i ** 2 >= puzzle_input:
            return i // 2


def sideward_distance(puzzle_input, edge):
    circle = 2 * edge + 1
    start = (circle - 2) + puzzle_input - (circle - 2) ** 2 - 1

    return ping_pong_range(circle - 2, start=start).next()


def ping_pong_range(n, start=0, length=10 ** 5):
    r = range(int(n))
    ppr_list = (r + r[1:-1][::-1]) * length
    counter = int(start)
    while True:
        yield ppr_list[counter]
        counter += 1


if __name__ == '__main__':
    # print solve_part_1(1)
    # print solve_part_1(12)
    # print solve_part_1(23)
    print solve_part_1(1024)
