import sys
import string
from itertools import cycle

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

    path = set()
    path.add(start_pos)
    search(start_pos, path)

    return all_path_lengths


def solution(data, part):
    grid = parsed(data)

    all_path_lengths = find_all_path_lengths(start_pos(grid), end_pos(grid), grid, part)

    start_node_count = 1
    print(sorted(all_path_lengths)[-1] - start_node_count)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    with open("day_23_input.txt", "r") as file:
        data = file.readlines()
    solution(data, part=1)
