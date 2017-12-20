import re

from anytree import Node, PreOrderIter


def solve_part_1(puzzle_input):
    return get_root(parse(puzzle_input)).name


def solve_part_2(puzzle_input):
    root = get_root(parse(puzzle_input))

    weights, unbalanced, balanced = find_point_of_unbalance(root)

    return unbalanced.weight - (weights[unbalanced] - weights[balanced])


def parse(puzzle_input):
    raw_nodes = [re.search(r'([a-z]*) \(([0-9]*)\)(?: -> )?([a-z, ]+)?.*', line).groups() for line in puzzle_input]

    nodes = {}
    for name, weight, _ in raw_nodes:
        nodes[name] = Node(name, weight=int(weight))

    for name, _, children in raw_nodes:
        if children:
            for child in children.split(', '):
                nodes[child].parent = nodes[name]

    return nodes


def get_root(nodes):
    return next(node for node in nodes.values() if node.is_root)


def find_point_of_unbalance(root, previous_layer=(None, None, None)):
    while True:
        weights, unbalanced, balanced = measure_layer(root)

        if weights[unbalanced] == weights[balanced]:
            return previous_layer
        else:
            return find_point_of_unbalance(unbalanced, (weights, unbalanced, balanced))


def measure_layer(root):
    weights = {child: sum([node.weight for node in PreOrderIter(child)]) for child in root.children}
    unbalanced, balanced = max(weights, key=weights.get), min(weights, key=weights.get)

    return weights, unbalanced, balanced


if __name__ == '__main__':
    lines = open('input.txt').readlines()
    print solve_part_1(lines)
    print solve_part_2(lines)
