from utils import knot_hash

from itertools import product


def solve_part_1(seed):
    return sum([binary.count('1') for binary in to_binaries(seed)])


def to_binaries(seed):
    hashed_rows = [knot_hash('{}-{}'.format(seed, row)) for row in range(128)]

    binaries = []
    for hashed_row in hashed_rows:
        binaries.append(''.join(['{0:04b}'.format(int(c, 16)) for c in hashed_row]))

    return binaries


def solve_part_2(seed):
    binaries, regions, visited = to_binaries(seed), set(), set()

    for (i, j) in product(range(128), range(128)):
        region = get_region(binaries, visited, i, j)

        if region:
            visited.union(set(region))
            regions.add(hash_region(region))

    return len(regions)


def get_region(binaries, visited, i, j):
    if i in range(128) and j in range(128) and (i, j) not in visited and binaries[i][j] == '1':
        visited.add((i, j))
        return [(i, j)] \
               + get_region(binaries, visited, i + 1, j) \
               + get_region(binaries, visited, i - 1, j) \
               + get_region(binaries, visited, i, j + 1) \
               + get_region(binaries, visited, i, j - 1)
    else:
        return []


def hash_region(region):
    return '-'.join([str(x) for x in sorted(region)])


if __name__ == '__main__':
    seed = open('input.txt').readline()

    print solve_part_1(seed)
    print solve_part_2(seed)
