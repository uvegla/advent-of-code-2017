def solve_part_1(puzzle_input):
    score, state, depth, pointer = 0, 'READ', 0, 0

    while pointer < len(puzzle_input):
        char = puzzle_input[pointer]

        if char == '!':
            pointer += 2
            continue

        if state == 'READ':
            if char == '{':
                depth += 1
                score += depth
            if char == '}':
                depth -= 1
            if char == '<':
                state = 'DEVOUR'
        elif state == 'DEVOUR':
            if char == '>':
                state = 'READ'

        pointer += 1

    return score


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readline())
