from collections import Counter


def part_one(data):
    count_twos = 0
    count_threes = 0
    for line in data:
        if any(x == 2 for x in Counter(line).values()):
            count_twos += 1
        if any(x == 3 for x in Counter(line).values()):
            count_threes += 1

    print(count_twos * count_threes)


def are_matching(a, b):
    i = 0
    count = 0
    letters = []

    while i < len(a):
        if a[i] == b[i]:
            letters.append(a[i])
        else:
            count += 1
            if count > 1:
                return False
        i += 1

    return "".join(letters)


def part_two(data):
    data = sorted(data)
    i = 0
    while i < len(data) - 1:
        m = are_matching(data[i].strip(), data[i + 1].strip())
        if m:
            return m
        i += 1


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    print(part_two(data))
