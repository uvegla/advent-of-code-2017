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


def solve_part_2(programs, commands):
    solved_permutations = {}

    for _ in range(10 ** 9):
        if programs in solved_permutations:
            programs = solved_permutations[programs]
        else:
            solved_permutations[programs] = solve_part_1(programs, commands)

    return programs


if __name__ == '__main__':
    print solve_part_1('abcdefghijklmnop', open('input.txt').readline().split(','))
    print solve_part_2('abcdefghijklmnop', open('input.txt').readline().split(','))
