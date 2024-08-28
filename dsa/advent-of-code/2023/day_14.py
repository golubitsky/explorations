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
    def out_of_bounds(y):
        return y < 0 or x < 0 or y == len(matrix) or x == len(matrix[0])

    def is_boundary(y, x):
        return matrix[y][x] in {ROUND_ROCK, CUBE_ROCK} or out_of_bounds(y)

    def next_pos(y, x, direction):
        if direction == NORTH:
            return (y - 1, x)

    def rolled_position(y, x, direction):
        while True:
            pos = next_pos(y, x, direction)
            if is_boundary(*pos):
                break
            y, x = pos

        return (y, x)

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] != ROUND_ROCK:
                continue

            y_rolled, x_rolled = rolled_position(y, x, direction)
            matrix[y][x] = EMPTY
            matrix[y_rolled][x_rolled] = ROUND_ROCK


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


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


if __name__ == "__main__":
    with open("day_14_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
