import re


def solve_part_1(puzzle_input):
    programs = parse(puzzle_input)

    return len(reachable_programs_for('0', programs))


def parse(puzzle_input):
    programs = {}

    for line in puzzle_input:
        program, direct_pipes = re.search(r'(\w+) <-> ([0-9, ]+)', line).groups()
        programs[program] = set(direct_pipes.split(', '))

    return programs


def reachable_programs_for(n, programs):
    reachable_programs = set(programs[n])
    while True:
        item_count = len(reachable_programs)

        for reachable_program in reachable_programs:
            reachable_programs = reachable_programs.union(programs[reachable_program])

        if len(reachable_programs) == item_count:
            break

    return reachable_programs


def solve_part_2(puzzle_input):
    groups = set()
    programs = parse(puzzle_input)

    for pid in range(len(puzzle_input)):
        groups.add(hash_set(reachable_programs_for(str(pid), programs)))

    return len(groups)


def hash_set(s):
    return ','.join(sorted(s))


if __name__ == '__main__':
    lines = open('input.txt').readlines()

    print solve_part_1(lines)
    print solve_part_2(lines)
