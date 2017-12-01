def generic(puzzle_input, f_next_index):
    circular = puzzle_input * 2

    return sum([int(circular[i]) for i in range(len(puzzle_input)) if circular[i] == circular[f_next_index(i)]])


def solve_part_1(puzzle_input):
    return generic(puzzle_input, lambda i: i + 1)


def solve_part_2(puzzle_input):
    return generic(puzzle_input, lambda i: i + len(puzzle_input) // 2)


if __name__ == '__main__':
    input_line = open('input.txt').readline()
    print solve_part_1(input_line)
    print solve_part_2(input_line)
