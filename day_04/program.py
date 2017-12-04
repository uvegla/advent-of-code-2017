def solve_part_1(passphrases):
    return sum([1 for x in passphrases if len(set(x)) == len(x)])


def solve_part_2(passphrases):
    return sum([1 for x in passphrases if len(set([''.join(sorted(y)) for y in x])) == len(x)])


if __name__ == '__main__':
    passphrases = [x.split(' ') for x in open('input.txt').read().splitlines()]
    print solve_part_1(passphrases)
    print solve_part_2(passphrases)
