def generic(lines, logic):
    return sum([logic([int(x) for x in line.split('\t')]) for line in lines])


def solve_part_1(lines):
    def max_min_difference(numbers):
        return max(numbers) - min(numbers)

    return generic(lines, max_min_difference)


def solve_part_2(lines):
    def evenly_divisible_values(numbers):
        divs = []
        for i in numbers:
            for j in numbers:
                if i % j == 0 or j % i == 0:
                    divs.append(max([i, j]) // min([i, j]))

        return max(divs)

    return generic(lines, evenly_divisible_values)


if __name__ == '__main__':
    puzzle_input = open('input.txt').readlines()
    print solve_part_1(puzzle_input)
    print solve_part_2(puzzle_input)
