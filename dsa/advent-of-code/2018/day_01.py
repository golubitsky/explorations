import re


def part_one(data):
    total = 0
    for line in data:
        total += int(re.search(r"-?\d+", line)[0])
    print(total)


def part_two(data):
    values = set()
    total = 0
    values.add(0)

    while True:
        for line in data:
            total += int(re.search(r"-?\d+", line)[0])
            if total in values:
                return total
            values.add(total)


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    print(part_two(data))
