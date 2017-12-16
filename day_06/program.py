def solve_part_1_and_2(puzzle_input):
    loops = 0
    states = {}

    while True:
        loops += 1

        max_value = max(puzzle_input)
        index = puzzle_input.index(max_value)

        puzzle_input[index] = 0
        for _ in range(max_value):
            index += 1
            puzzle_input[index % len(puzzle_input)] += 1

        state_hash = ','.join([str(y) for y in puzzle_input])
        if state_hash in states:
            return loops, loops - states[state_hash]

        states[state_hash] = loops


if __name__ == '__main__':
    blocks = [int(x) for x in open('input.txt').readline().split('\t')]
    print solve_part_1_and_2(blocks)
