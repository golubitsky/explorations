ROUND_ROCK = "O"
CUBE_ROCK = "#"
EMPTY = "."

NORTH = "N"
WEST = "W"
SOUTH = "S"
EAST = "E"


def parsed_as_matrix(data):
    return [list(row.strip()) for row in data]


def tilt_until_rocks_stop(matrix, direction):
    def out_of_bounds(y, x):
        return y < 0 or x < 0 or y == len(matrix) or x == len(matrix[0])

    def is_boundary(y, x):
        return out_of_bounds(y, x) or matrix[y][x] in {ROUND_ROCK, CUBE_ROCK}

    def next_pos(y, x, direction):
        if direction == NORTH:
            return (y - 1, x)
        elif direction == WEST:
            return (y, x - 1)
        elif direction == SOUTH:
            return (y + 1, x)
        elif direction == EAST:
            return (y, x + 1)

    def rolled_position(y, x, direction):
        while True:
            pos = next_pos(y, x, direction)
            if is_boundary(*pos):
                break
            y, x = pos

        return (y, x)

    def roll_round_rock(y, x):
        if matrix[y][x] != ROUND_ROCK:
            return

        y_rolled, x_rolled = rolled_position(y, x, direction)
        matrix[y][x] = EMPTY
        matrix[y_rolled][x_rolled] = ROUND_ROCK

    if direction in [NORTH, WEST]:
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                roll_round_rock(y, x)
    else:
        for y in range(len(matrix) - 1, -1, -1):
            for x in range(len(matrix[0]) - 1, -1, -1):
                roll_round_rock(y, x)


def total_load(matrix):
    total = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] != ROUND_ROCK:
                continue

            total += len(matrix) - y

    return total


def part_one(data):
    matrix = parsed_as_matrix(data)
    tilt_until_rocks_stop(matrix, direction=NORTH)
    print(total_load(matrix))


def run_tile_cycle(matrix, directions):
    for direction in directions:
        tilt_until_rocks_stop(matrix, direction)


def part_two(data):
    matrix = parsed_as_matrix(data)
    directions = [NORTH, WEST, SOUTH, EAST]
    n_cycles = 10000

    for _ in range(n_cycles):
        run_tile_cycle(matrix, directions)
    print_matrix(matrix)
    print(total_load(matrix))


def print_matrix(matrix):
    print("----------")
    for row in matrix:
        print("".join(row))


if __name__ == "__main__":
    with open("day_14_sample.txt", "r") as file:
        data = file.readlines()
    part_two(data)
