def solve_generic(puzzle_input, f_increment):
    steps, index = 0, 0
    try:
        while True:
            current = puzzle_input[index]

            next_index = index + current
            if next_index < 0:
                raise IndexError

            puzzle_input[index] += f_increment(current)
            index = next_index

            steps += 1
    except IndexError:
        return steps


def solve_part_1(puzzle_input):
    return solve_generic(puzzle_input, lambda current: 1)


def solve_part_2(puzzle_input):
    return solve_generic(puzzle_input, lambda current: 1 if current < 3 else -1)


if __name__ == '__main__':
    for solver in [solve_part_1, solve_part_2]:
        lines = [int(x) for x in open('input.txt').readlines()]
        print solver(lines)
