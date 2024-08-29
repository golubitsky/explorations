from collections import deque

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"


def next_pos(cur, direction):
    return {
        RIGHT: (cur[0], cur[1] + 1),
        LEFT: (cur[0], cur[1] - 1),
        UP: (cur[0] - 1, cur[1]),
        DOWN: (cur[0] + 1, cur[1]),
    }[direction]


def min_max(holes):
    max_y = max([y for y, x in holes])
    max_x = max([x for y, x in holes])
    min_y = min([y for y, x in holes])
    min_x = min([x for y, x in holes])

    return [min_y, max_y, min_x, max_x]


def count_empties_at_edge(holes):
    min_y, max_y, min_x, max_x = min_max(holes)
    seen_empties = set()
    found_neighbors = set()

    def in_bounds(pos):
        y, x = pos
        return y >= min_y and y <= max_y and x >= min_x and x <= max_x

    def empty_neighbors(pos):
        result = []

        for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            y, x = pos
            adj = (y + dy, x + dx)
            if adj not in holes and in_bounds(adj):
                result.append(adj)

        return result

    def find_adjacent_empties(pos):
        q = deque([pos])
        while q:
            pos = q.popleft()
            if pos not in seen_empties:
                seen_empties.add(pos)

            for neighbor in empty_neighbors(pos):
                if neighbor not in found_neighbors:
                    found_neighbors.add(neighbor)
                    q.append(neighbor)

    for x in range(min_x, max_x + 1):
        for pos in [(min_y, x), (max_y, x)]:
            if pos not in seen_empties and pos not in holes:
                find_adjacent_empties(pos)

    for y in range(min_y, max_y + 1):
        for pos in [(y, min_x), (y, max_x)]:
            if pos not in seen_empties and pos not in holes:
                find_adjacent_empties(pos)

    return len(seen_empties)


def area(holes):
    min_y, max_y, min_x, max_x = min_max(holes)
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

    return area - count_empties_at_edge(holes)


def print_lagoon(holes):
    min_y, max_y, min_x, max_x = min_max(holes)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) in holes:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part_two(data):
    pos = (0, 0)
    holes = set()
    for line in data:
        hex_code = line.strip().split(" ")[-1][2:-1]

        direction = [RIGHT, DOWN, LEFT, UP][int(hex_code[5])]
        count = int(hex_code[:5], 16)
        print(count)
        continue
        holes.add(pos)

        for _ in range(count):
            pos = next_pos(pos, direction)
            holes.add(pos)
    holes.add(pos)

    print(area(holes))
    # print_lagoon(holes)


def part_one(data):
    pos = (0, 0)
    holes = set()
    for line in data:
        direction, count, color = line.strip().split(" ")
        holes.add(pos)

        count = int(count)
        for _ in range(count):
            pos = next_pos(pos, direction)
            holes.add(pos)
    holes.add(pos)

    print(area(holes))
    # print_lagoon(holes)


if __name__ == "__main__":
    with open("day_18_sample.txt", "r") as file:
        data = file.readlines()
    part_two(data)
