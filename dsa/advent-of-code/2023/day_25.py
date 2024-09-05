from collections import defaultdict
import itertools
import re
import sys


def add_edge(graph, n1, n2):
    graph[n1].add(n2)
    graph[n2].add(n1)


def remove_edge(graph, n1, n2):
    graph[n1].remove(n2)
    graph[n2].remove(n1)


def parsed_graph(data):
    graph = defaultdict(set)

    for line in data:
        node, other_nodes = line.split(":")
        other_nodes = re.findall(r"\w+", other_nodes)
        for other_node in other_nodes:
            add_edge(graph, node, other_node)

    return graph


def count_connected_components(graph):
    all_seen = []

    def dfs(node, seen):
        for neighbor in graph[node]:
            if neighbor in seen:
                continue

            seen.add(neighbor)
            dfs(neighbor, seen)

        return seen

    for node in graph:
        if any([node in seen for seen in all_seen]):
            continue

        seen = dfs(node, {node})
        all_seen.append(seen)

    return all_seen


def all_edge_combinations(graph):
    combos = set()

    for node in graph:
        for other_node in graph:
            if node == other_node:
                continue
            if other_node not in graph[node]:
                continue

            combo = tuple(sorted([node, other_node]))
            if combo not in combos:
                combos.add(combo)

    return combos


def part_one(data):
    graph = parsed_graph(data)

    print(len(all_edge_combinations(graph)))
    combos_of_three_edges = itertools.combinations(all_edge_combinations(graph), 3)

    print('hi')
    print(len(list(combos_of_three_edges)))
    print('hi')
    for combo in combos_of_three_edges:
        for n1, n2 in combo:
            remove_edge(graph, n1, n2)

        components = count_connected_components(graph)

        if len(components) == 2:
            print(len(components[0]) * len(components[1]))
            break

        for n1, n2 in combo:
            add_edge(graph, n1, n2)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    with open("day_25_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
