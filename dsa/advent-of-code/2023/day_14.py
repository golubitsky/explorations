ROUND_ROCK = "O"
CUBE_ROCK = "#"
EMPTY = "."


def parsed_as_matrix(data):
    return [list(row.strip()) for row in data]


def tilt_north_until_stopped(matrix):
    def out_of_bounds(y):
        return y < 0

    def is_boundary(y, x):
        return matrix[y][x] in {ROUND_ROCK, CUBE_ROCK} or out_of_bounds(y)

    def rolled_position(y, x):
        while not is_boundary(y - 1, x):
            y -= 1
        return (y, x)

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] != ROUND_ROCK:
                continue

            y_rolled, x_rolled = rolled_position(y, x)
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
    tilt_north_until_stopped(matrix)
    print(total_load(matrix))


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


if __name__ == "__main__":
    with open("day_14_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
