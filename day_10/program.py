def solve_part_1(r, puzzle_input):
    current, skip = 0, 0

    for length in puzzle_input:
        (s1_s, s1_e), (s2_s, s2_e) = get_sections(r, current, length)

        reverse = (r[s1_s:s1_e] + r[s2_s:s2_e])[::-1]

        r[s1_s:s1_e] = reverse[:s1_e-s1_s]
        r[s2_s:s2_e] = reverse[s1_e-s1_s:]

        current = (current + length + skip) % len(r)
        skip += 1

    return r[0] * r[1]


def get_sections(r, current, length):
    if current + length < len(r):
        return (current, current + length), (0, 0)
    else:
        return (current, len(r)), (0,  current + length - len(r))


if __name__ == '__main__':
    lengths = [int(x) for x in open('input.txt').readline().split(',')]
    print solve_part_1(range(256), lengths)
