import os
import sys

VECTORS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def parsed(data):
    grid = [list(line.strip()) for line in data]

    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == "S":
                grid[y][x] = "."
                return grid, (y, x)


NEIGHBOR_CACHE = {}


def neighbors(pos, grid):
    if pos in NEIGHBOR_CACHE:
        return NEIGHBOR_CACHE[pos]

    def in_bounds(other_pos):
        y, x = other_pos
        return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])

    def is_empty(other_pos):
        y, x = other_pos
        return grid[y][x] == "."

    def new_pos(pos, vector):
        return (pos[0] + vector[0], pos[1] + vector[1])

    result = [
        new_pos(pos, v)
        for v in VECTORS
        if in_bounds(new_pos(pos, v)) and is_empty(new_pos(pos, v))
    ]
    NEIGHBOR_CACHE[pos] = result

    return result


def print_grid(grid, seen):
    os.system("clear")
    print("  0123456789")
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if (y, x) in seen:
                print("O", end="")
            else:
                print(item, end="")
        print()


def part_one(data):
    grid, pos = parsed(data)
    seen = set()
    seen.add(pos)
    step_count = 0
    positions = set()
    positions.add(pos)
    while step_count < int(sys.argv[1]):
        new_positions = set()
        for pos in positions:
            for neighbor in neighbors(pos, grid):
                new_positions.add(neighbor)

        positions = new_positions
        step_count += 1

    # print_grid(grid, positions)
    print(len(positions))


if __name__ == "__main__":
    with open("day_21_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
