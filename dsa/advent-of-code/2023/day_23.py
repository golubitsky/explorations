import string
from itertools import cycle
from collections import defaultdict

VECTORS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
VECTOR_BY_CHAR = {
    ">": VECTORS[0],
    "^": VECTORS[1],
    "<": VECTORS[2],
    "v": VECTORS[3],
}


def parsed(data):
    grid = [list(line.strip()) for line in data]

    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == "S":
                grid[y][x] = "."
                return grid, (y, x)

    return grid


def print_grid(grid):
    y_c = cycle(string.digits)
    x_c = cycle(string.digits)
    y_label = "  " + "".join([next(y_c) for _ in range(len(grid))])
    print(y_label)
    for y, row in enumerate(grid):
        print(next(x_c), end=" ")
        for x, item in enumerate(row):
            print(item, end="")
        print()


def start_pos(grid):
    y = 0
    for x in range(len(grid[y])):
        if grid[y][x] == ".":
            return (y, x)


def end_pos(grid):
    y = len(grid) - 1
    for x in range(len(grid[y])):
        if grid[y][x] == ".":
            return (y, x)


CACHE = {}


def neighbors(pos, grid, part):
    if pos in CACHE:
        return CACHE[pos]

    def is_in_bounds(y2, x2):
        return y2 < len(grid) and y2 >= 0 and x2 < len(grid[0]) and x2 >= 0

    def is_path(y2, x2):
        return grid[y2][x2] != "#"

    y, x = pos

    result = []

    if part == 1:
        if grid[y][x] in VECTOR_BY_CHAR:
            dy, dx = VECTOR_BY_CHAR[grid[y][x]]
            y2, x2 = y + dy, x + dx
            if is_in_bounds(y2, x2) and is_path(y2, x2):
                return [(y2, x2)]
            print("logic error")
            exit()

    for dy, dx in VECTORS:
        y2, x2 = y + dy, x + dx
        if is_in_bounds(y2, x2) and is_path(y2, x2):
            result.append((y2, x2))

    CACHE[pos] = result
    return result


def precompute_optimized_graph(grid, part):
    graph = defaultdict(list)  # pos => [(pos, distance)]

    def find_junctions():
        junctions = set()
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if grid[y][x] == "#":
                    continue
                pos = (y, x)
                if len(neighbors(pos, grid, part)) > 2:
                    junctions.add(pos)
        return junctions

    def find_next_junction_or_end(pos, path, step_count=1):
        if pos == junction:
            return

        path.add(pos)

        if pos in junctions or pos == end_pos(grid):
            return (pos, step_count)

        n = [x for x in neighbors(pos, grid, part) if x not in path]

        if len(n) == 0:
            return
        if len(n) != 1:
            print("unexpected condition")
            exit()
        return find_next_junction_or_end(n[0], path, step_count + 1)

    junctions = find_junctions()

    # compute distances between all junctions, including end pos
    for junction in junctions:
        for neighbor in neighbors(junction, grid, part):
            next_junction = find_next_junction_or_end(neighbor, {junction})
            if next_junction is not None:
                graph[junction].append(next_junction)

    start = start_pos(grid)
    next_junction = find_next_junction_or_end(neighbors(start, grid, part)[0], {start})
    graph[start].append(next_junction)

    return graph


def find_all_path_lengths(start_pos, end_pos, grid, part):
    all_path_lengths = []

    def search(pos, path):
        if pos == end_pos:
            all_path_lengths.append(len(path))
            return

        for adj_pos in neighbors(pos, grid, part):
            if adj_pos not in path:
                new_path = path.copy()
                new_path.add(adj_pos)
                search(adj_pos, new_path)

    search(start_pos, path={start_pos})

    return all_path_lengths


def find_all_path_lengths_optimized(start_pos, end_pos, graph):
    all_path_lengths = []

    def search(pos, path, distance=0):
        if pos == end_pos:
            all_path_lengths.append(distance)
            return

        for adj_pos, d in graph[pos]:
            if adj_pos not in path:
                new_path = path.copy()
                new_path.add(adj_pos)
                search(adj_pos, new_path, distance + d)

    search(start_pos, path={start_pos})

    return all_path_lengths


def solution(data, part):
    grid = parsed(data)
    graph = precompute_optimized_graph(grid, part)

    all_path_lengths = find_all_path_lengths_optimized(
        start_pos(grid), end_pos(grid), graph
    )
    print(max(all_path_lengths))


if __name__ == "__main__":
    with open("day_23_input.txt", "r") as file:
        data = file.readlines()
    solution(data, part=2)
