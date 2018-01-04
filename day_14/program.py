from utils import knot_hash


def solve_part_1(seed):
    row_hashed = [knot_hash('{}-{}'.format(seed, row)) for row in range(128)]

    binaries = ['{0:04b}'.format(int(c, 16)) for c in [row_hash for row_hash in row_hashed]]

    return sum([binary.count('1') for binary in binaries])


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readline())
