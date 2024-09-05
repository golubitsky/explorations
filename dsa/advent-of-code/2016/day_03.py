import re


def transposed(matrix):
    return [list(row) for row in zip(*matrix)]


def parsed(line):
    return [int(x) for x in re.findall(r"\d+", line)]


def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True


def part_one(data):
    count = 0

    for line in data:
        if is_triangle(*parsed(line)):
            count += 1

    print(count)


def part_two(data):
    count = 0

    for row in transposed([parsed(line) for line in data]):
        for i in range(0, len(row), 3):
            if is_triangle(*row[i : i + 3]):
                count += 1

    print(count)


if __name__ == "__main__":
    with open("day_03_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    part_two(data)
