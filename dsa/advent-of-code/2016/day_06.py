from collections import Counter


def transposed(matrix):
    return [list(row) for row in zip(*matrix)]


def part_one(data):
    letter = 0
    count = 1
    result = []
    for line in transposed([list(line.strip()) for line in data]):
        m = Counter(line).most_common(2)
        if m[0][count] > m[1][count]:
            result.append(max(m[0][letter]))
        elif m[0][count] < m[1][count]:
            result.append(max(m[1][letter]))
    print("".join(result))


def part_two(data):
    letter = 0
    count = 1
    result = []
    for line in transposed([list(line.strip()) for line in data]):
        m = Counter(line).most_common()[-2:]
        if m[0][count] > m[1][count]:
            result.append(max(m[1][letter]))
        elif m[0][count] < m[1][count]:
            result.append(max(m[0][letter]))
    print("".join(result))


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    part_two(data)
