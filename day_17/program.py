from collections import deque


def solve_part_1(steps):
    circular_buffer = deque()

    for i in xrange(2018):
        circular_buffer.rotate(steps)
        circular_buffer.appendleft(i)

    return circular_buffer[-1]


if __name__ == '__main__':
    print solve_part_1(366)
