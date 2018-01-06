from collections import deque


def generic(steps, length):
    circular_buffer = deque(maxlen=length)

    for i in xrange(length):
        circular_buffer.rotate(steps)
        circular_buffer.appendleft(i)

    return circular_buffer


def solve_part_1(steps):
    return generic(steps, 2018)[-1]


def solve_part_2(steps):
    circular_buffer = list(generic(steps, 5 * 10 ** 7 + 1))

    return circular_buffer[circular_buffer.index(0) - 1]


if __name__ == '__main__':
    print solve_part_1(366)
    print solve_part_2(366)
