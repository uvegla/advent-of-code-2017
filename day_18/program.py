from Queue import Queue, Empty


def solve_part_1(instructions):
    registers = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}

    return ProcessorPartOne(registers).execute(instructions)


def solve_part_2(instructions):
    p_0 = ProcessorPartTwo({'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}, instructions)
    p_1 = ProcessorPartTwo({'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 1}, instructions)

    p_0.make_aware_of(p_1)
    p_1.make_aware_of(p_0)

    while True:
        if p_0.waiting and p_1.waiting:
            return p_1.snd_counter
        else:
            p_0.step()
            p_1.step()


class Processor(object):
    def __init__(self, registers):
        self.registers = registers

    def calculate_jump(self, instruction):
        _, register, value = instruction.split()

        return int(self.get_value(value)) if self.get_value(register) > 0 else 1

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


class ProcessorPartTwo(Processor):
    def __init__(self, registers, instructions):
        super(ProcessorPartTwo, self).__init__(registers)

        self.instructions = instructions
        self.instruction_pointer = 0

        self.other = None
        self.message_queue = Queue()

        self.waiting = False

        self.snd_counter = 0

    def make_aware_of(self, other):
        self.other = other

    def step(self):
        instruction = self.instructions[self.instruction_pointer]

        if instruction.startswith('jgz'):
            self.instruction_pointer += self.calculate_jump(instruction)
            return

        if instruction.startswith('snd'):
            self.execute_snd(instruction)
        elif instruction.startswith('set'):
            self.execute_set(instruction)
        elif instruction.startswith('add'):
            self.execute_add(instruction)
        elif instruction.startswith('mul'):
            self.execute_mul(instruction)
        elif instruction.startswith('mod'):
            self.execute_mod(instruction)
        elif instruction.startswith('rcv'):
            self.waiting = self.execute_rcv(instruction)

        self.instruction_pointer += 1 if not self.waiting else 0

    def execute_snd(self, instruction):
        _, value = instruction.split()

        self.other.queue(int(self.get_value(value)))
        self.snd_counter += 1

    def queue(self, value):
        self.message_queue.put(value)

    def execute_rcv(self, instruction):
        _, register = instruction.split()

        try:
            self.registers[register] = self.message_queue.get_nowait()
        except Empty:
            return True

        return False


if __name__ == '__main__':
    instructions = open('input.txt').readlines()

    print solve_part_1(instructions)
    print solve_part_2(instructions)
