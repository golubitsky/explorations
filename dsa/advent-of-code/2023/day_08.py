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


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as file:
        data = file.read()
    print(part_one(data))
