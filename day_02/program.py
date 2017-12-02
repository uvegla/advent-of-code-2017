def solve_part_1(lines):
    sum = 0
    for line in lines:
        nums = [int(x) for x in line.split('\t')]

        sum += max(nums) - min(nums)

    return sum


def solve_part_2(lines):
    sum = 0
    for line in lines:
        nums = [int(x) for x in line.split('\t')]

        divs = []
        for i in nums:
            for j in nums:
                if i % j == 0 or j % i == 0:
                    divs.append(max([i, j]) // min([i, j]))

        sum += max(divs)

    return sum


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readlines())
    print solve_part_2(open('input.txt').readlines())
