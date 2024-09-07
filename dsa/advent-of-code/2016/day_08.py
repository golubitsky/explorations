import re

SIZE_X = 50
SIZE_Y = 6


def parsed_instruction(line):
    if line.startswith("rect"):
        x, y = re.findall(r"\d+", line)
        return {"type": "rect", "x": int(x), "y": int(y)}
    else:
        index, amount = re.findall(r"\d+", line)

        return {
            "type": "rotate",
            "direction": re.search(r"column|row", line)[0],
            "index": int(index),
            "amount": int(amount),
        }


def rect(instruction, grid):
    for y in range(instruction["y"]):
        for x in range(instruction["x"]):
            grid[y][x] = "#"


def rotate(instruction, grid):
    if instruction["direction"] == "column":
        column = [None] * SIZE_Y
        x = instruction["index"]
        for y in range(SIZE_Y):
            column[(y + instruction["amount"]) % SIZE_Y] = grid[y][x]

        for y, value in enumerate(column):
            grid[y][x] = value
    else:
        row = [None] * SIZE_X
        y = instruction["index"]
        for x in range(SIZE_X):
            row[(x + instruction["amount"]) % SIZE_X] = grid[y][x]

        for x, value in enumerate(row):
            grid[y][x] = value


def init_grid():
    grid = []

    for _ in range(SIZE_Y):
        grid.append([None] * SIZE_X)

    return grid


def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                char = "#"
            else:
                char = " "
            print(char, end="")
        print()


def part_one(data):
    grid = init_grid()

    for line in data:
        instruction = parsed_instruction(line)

        if instruction["type"] == "rect":
            rect(instruction, grid)
        elif instruction["type"] == "rotate":
            rotate(instruction, grid)
    print_grid(grid)
    count = 0
    for row in grid:
        for value in row:
            if value == "#":
                count += 1
    print(count)


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
