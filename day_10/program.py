from utils import knot_hash
from utils.knot_hash import single_round


def solve_part_1(sparse_hash, lengths):
    sparse_hash, _, _ = single_round(sparse_hash, lengths)

    return sparse_hash[0] * sparse_hash[1]


def solve_part_2(puzzle_input):
    return knot_hash(puzzle_input)


if __name__ == '__main__':
    line = open('input.txt').readline()
    lengths = [int(x) for x in line.split(',')]

    print solve_part_1(range(256), lengths)
    print solve_part_2(line)
