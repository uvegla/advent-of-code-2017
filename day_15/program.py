def solve_part_1(init_a, init_b):
    generator_a = generator(init_a, 16807)
    generator_b = generator(init_b, 48271)

    return compare_n_times(generator_a, generator_b, 4 * 10 ** 7)


def generator(initial, factor):
    previous = initial
    while True:
        previous = (previous * factor) % 2147483647
        yield previous


def l16m(a, b):
    return '{0:b}'.format(a)[-16:] == '{0:b}'.format(b)[-16:]


def solve_part_2(init_a, init_b):
    generator_a = generator_with_criteria(generator(init_a, 16807), 4)
    generator_b = generator_with_criteria(generator(init_b, 48271), 8)

    return compare_n_times(generator_a, generator_b, 5 * 10 ** 6)


def generator_with_criteria(raw_generator, divisor):
    while True:
        value = next(raw_generator)

        if value % divisor == 0:
            yield value
        else:
            continue


def compare_n_times(generator_a, generator_b, times):
    return sum([1 if l16m(next(generator_a), next(generator_b)) else 0 for _ in range(times)])


if __name__ == '__main__':
    print solve_part_1(289, 629)
    print solve_part_2(289, 629)
