import re

conditionals = {
    '==': lambda x, y: x == y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '!=': lambda x, y: x != y
}

operations = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}


def solve_part_1_and_2(puzzle_input):
    instructions = [parse_instruction(line) for line in puzzle_input]

    registers, highest_ever = {}, 0
    for r, o, v, cr, co, cv in instructions:
        if check_condition(registers, cr, co, cv):
            execute(registers, o, r, v)

            highest_value = get_highest_value(registers)
            highest_ever = highest_value if highest_value > highest_ever else highest_ever

    return get_highest_value(registers), highest_ever


def parse_instruction(line):
    r, o, v, cr, co, cv = re.search(r'(\w+) (\w+) ([-0-9]+) if (\w+) ([!><=]+) ([-0-9]+)', line).groups()

    return r, o, int(v), cr, co, int(cv)


def check_condition(registers, cr, co, cv):
    return conditionals[co](get_or_initialize(registers, cr), cv)


def execute(registers, o, r, v):
    registers[r] = operations[o](get_or_initialize(registers, r), v)


def get_or_initialize(registers, register):
    if register not in registers:
        registers[register] = 0

    return registers[register]


def get_highest_value(registers):
    return registers[max(registers, key=registers.get)]


if __name__ == '__main__':
    lines = open('input.txt').readlines()
    print solve_part_1_and_2(lines)
