import itertools
import re


def part_one(data):
    directions, nodes_raw = data.split("\n\n")
    nodes_raw = nodes_raw.split("\n")
    edges = {}
    for node in nodes_raw:
        node, left, right = re.findall(r"\w+", node)
        edges[node] = {"L": left, "R": right}

    directions = itertools.cycle(directions)

    step_count = 0
    node = "AAA"
    while True:
        node = edges[node][next(directions)]
        step_count += 1
        if node == "ZZZ":
            break

    return step_count


def count_steps(source, target, edges, directions):
    directions = itertools.cycle(directions)

    step_count = 0
    node = source
    while True:
        node = edges[node][next(directions)]
        step_count += 1
        if step_count > 10000000:
            return "X"
        if node == target:
            break

    return step_count


def part_two(data):
    directions, nodes_raw = data.split("\n\n")
    nodes_raw = nodes_raw.split("\n")
    edges = {}
    nodes = []
    target_nodes = set()
    for node in nodes_raw:
        node, left, right = re.findall(r"\w+", node)
        edges[node] = {"L": left, "R": right}

        if node.endswith("A"):
            nodes.append(node)
        if node.endswith("Z"):
            target_nodes.add(node)

    step_count = 0
    count = 0
    print(nodes)
    print(target_nodes)
    print(count_steps("XVZ", "XVZ", edges, directions))
    # for node in nodes:
    #     results = []
    #     for target_node in target_nodes:
    #         steps = count_steps(node, target_node, edges, directions)
    #         results.append(steps)
    #     print(f'{node} {results}')
    exit()
    while True:
        direction = next(directions)
        nodes = [edges[node][direction] for node in nodes]
        step_count += 1
        if any(node in target_nodes for node in nodes):
            count += 1
            print([node for node in nodes])
            print([step_count for node in nodes])
            if count == 10:
                break
        if all(node in target_nodes for node in nodes):
            break

    return step_count


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as file:
        data = file.read()
    print(part_two(data))
# The code above is not cleaned up.
#
# There are only 6 starting nodes and 6 target nodes. It turns out that:
#   1. From one starting node there is a "relatively short path (< 100000 steps)"
#      to exactly one target node
#   2. Each of the target nodes is part of a cycle whose length (incidentally, I think)
#      equals the distance first traversed to first reach it from the starting node.
#
# Thus, to get the answer, manually get the lowest common multiple of the step counts below.
# AAA ['X', 'X', 'X', 'X', 13207, 'X']
# PRA ['X', 'X', 'X', 'X', 'X', 19951]
# PVA [14893, 'X', 'X', 'X', 'X', 'X']
# XLA ['X', 'X', 'X', 12083, 'X', 'X']
# PTA ['X', 'X', 20513, 'X', 'X', 'X']
# FBA ['X', 22199, 'X', 'X', 'X', 'X']
