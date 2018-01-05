def solve_part_1(init_a, init_b):
    generator_a = generator(init_a, 16807)
    generator_b = generator(init_b, 48271)

    return sum([1 if l16m(next(generator_a), next(generator_b)) else 0 for _ in range(4 * 10 ** 7)])


def generator(initial, factor):
    previous = initial
    while True:
        previous = (previous * factor) % 2147483647
        yield previous


def l16m(a, b):
    return '{0:b}'.format(a)[-16:] == '{0:b}'.format(b)[-16:]


if __name__ == '__main__':
    print solve_part_1(289, 629)
