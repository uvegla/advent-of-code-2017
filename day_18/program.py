def solve_part_1(instructions):
    instruction_pointer = 0
    registers = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}

    last_sound_played = None

    while True:
        instruction = instructions[instruction_pointer]

        if instruction.startswith('jgz'):
            instruction_pointer += calculate_jump(registers, instruction)
            continue

        if instruction.startswith('snd'):
            last_sound_played = registers[instruction.split()[1]]
        elif instruction.startswith('set'):
            execute_set(registers, instruction)
        elif instruction.startswith('add'):
            execute_add(registers, instruction)
        elif instruction.startswith('mul'):
            execute_mul(registers, instruction)
        elif instruction.startswith('mod'):
            execute_mod(registers, instruction)
        else:
            if should_terminate(registers, instruction):
                break

        instruction_pointer += 1

    return last_sound_played


def calculate_jump(registers, instruction):
    _, register, value = instruction.split()

    return int(value) if registers[register] > 0 else 1


def should_terminate(registers, instruction):
    _, register = instruction.split()

    return registers[register] > 0


def execute_set(registers, instruction):
    _, register, value = instruction.split()

    registers[register] = get_value(registers, value)


def execute_add(registers, instruction):
    _, register, value = instruction.split()

    registers[register] += get_value(registers, value)


def execute_mul(registers, instruction):
    _, register, value = instruction.split()

    registers[register] *= get_value(registers, value)


def execute_mod(registers, instruction):
    _, register, value = instruction.split()

    registers[register] %= get_value(registers, value)


def get_value(registers, value):
    try:
        value = int(value)
    except ValueError:
        value = registers[value]

    return value


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readlines())
