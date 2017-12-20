import re

from anytree import Node


def solve_part_1(puzzle_input):
    return next(node.name for node in parse(puzzle_input).values() if node.is_root)


def parse(puzzle_input):
    raw_nodes = [re.search(r'([a-z]*) \(([0-9]*)\)(?: -> )?([a-z, ]+)?.*', line).groups() for line in puzzle_input]

    nodes = {}
    for name, weight, _ in raw_nodes:
        nodes[name] = Node(name, weight=weight)

    for name, _, children in raw_nodes:
        if children:
            for child in children.split(', '):
                nodes[child].parent = nodes[name]

    return nodes


if __name__ == '__main__':
    print solve_part_1(open('input.txt').readlines())
