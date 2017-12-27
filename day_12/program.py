import re


def solve_part_1(puzzle_input):
    programs = parse(puzzle_input)

    reachable_programs = set(programs['0'])
    while True:
        item_count = len(reachable_programs)

        for reachable_program in reachable_programs:
            reachable_programs = reachable_programs.union(programs[reachable_program])

        if len(reachable_programs) == item_count:
            break

    return len(reachable_programs)


def parse(puzzle_input):
    programs = {}

    for line in puzzle_input:
        program, direct_pipes = re.search(r'(\w+) <-> ([0-9, ]+)', line).groups()
        programs[program] = set(direct_pipes.split(', '))

    return programs


if __name__ == '__main__':
    lines = open('input.txt').readlines()
    print solve_part_1(lines)
