def solve_part_1(instructions):
    registers = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}

    return ProcessorPartOne(registers).execute(instructions)


class Processor(object):
    def __init__(self, registers):
        self.registers = registers

    def calculate_jump(self, instruction):
        _, register, value = instruction.split()

        return int(value) if self.registers[register] > 0 else 1

    def execute_set(self, instruction):
        _, register, value = instruction.split()

        self.registers[register] = self.get_value(value)

    def execute_add(self, instruction):
        _, register, value = instruction.split()

        self.registers[register] += self.get_value(value)

    def execute_mul(self, instruction):
        _, register, value = instruction.split()

        self.registers[register] *= self.get_value(value)

    def execute_mod(self, instruction):
        _, register, value = instruction.split()

        self.registers[register] %= self.get_value(value)

    def get_value(self, value):
        try:
            value = int(value)
        except ValueError:
            value = self.registers[value]

        return value


class ProcessorPartOne(Processor):
    def __init__(self, registers):
        super(ProcessorPartOne, self).__init__(registers)

    def execute(self, instructions):
        instruction_pointer = 0

        last_sound_played = None

        while True:
            instruction = instructions[instruction_pointer]

            if instruction.startswith('jgz'):
                instruction_pointer += self.calculate_jump(instruction)
                continue

            if instruction.startswith('snd'):
                last_sound_played = self.registers[instruction.split()[1]]
            elif instruction.startswith('set'):
                self.execute_set(instruction)
            elif instruction.startswith('add'):
                self.execute_add(instruction)
            elif instruction.startswith('mul'):
                self.execute_mul(instruction)
            elif instruction.startswith('mod'):
                self.execute_mod(instruction)
            else:
                if self.should_terminate(instruction):
                    break

            instruction_pointer += 1

        return last_sound_played

    def should_terminate(self, instruction):
        _, register = instruction.split()

        return self.registers[register] > 0


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readlines())
