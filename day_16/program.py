import itertools


def solve_part_1(programs, commands):
    for command in commands:
        programs = COMMANDS[command[:1]](programs, command[1:])

    return programs


def spin(programs, size):
    s = int(size)

    return programs[-s:] + programs[:-s]


def exchange(programs, arguments):
    left, right = map(int, arguments.split('/'))

    return swap(programs, left, right)


def partner(programs, arguments):
    left, right = map(programs.index, arguments.split('/'))

    return swap(programs, left, right)


def swap(programs, left, right):
    plist = list(programs)

    plist[left], plist[right] = plist[right], plist[left]

    return ''.join(plist)


COMMANDS = {
    's': spin,
    'x': exchange,
    'p': partner
}


def solve_part_2_using_cache(programs, commands):
    solved_permutations = {}

    for _ in range(10 ** 9):
        if programs in solved_permutations:
            programs = solved_permutations[programs]
        else:
            solved_permutations[programs] = solve_part_1(programs, commands)

    return programs


def solve_part_2_using_cycle_length(programs, commands):
    length, cache = cycle_length(programs, commands)

    return cache[10 ** 9 % length - 1]


def cycle_length(programs, commands):
    solved_permutations = {}
    start_state = programs

    for counter in itertools.count():
        solution = solve_part_1(programs, commands)

        solved_permutations[counter] = solution

        if start_state == solution:
            return counter + 1, solved_permutations

        programs = solution


if __name__ == '__main__':
    programs = 'abcdefghijklmnop'
    commands = open('input.txt').readline().split(',')

    print solve_part_1(programs, commands)
    # print solve_part_2_using_cache(programs, commands)
    # print cycle_length(programs, commands)
    print solve_part_2_using_cycle_length(programs, commands)
