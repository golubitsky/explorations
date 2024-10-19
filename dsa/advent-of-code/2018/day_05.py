import string
import math


def operation(data):
    indexes = []
    for i, char in enumerate(data[:-1]):
        next_char = data[i + 1]
        if abs(ord(char) - ord(next_char)) == 32:
            # avoid counting cCc twice
            if not indexes or i != indexes[-1] + 1:
                indexes.append(i)

    for i in reversed(indexes):
        # remove element at index and at the next index
        data.pop(i)
        data.pop(i)

    return data


def part_one(data):
    while True:
        length_before = len(data)
        data = operation(data)
        if len(data) == length_before:
            break
    return len(data)


def part_two(data):
    min_length = math.inf
    for letter in string.ascii_lowercase:
        transformed = [x for x in data if x not in [letter, letter.upper()]]
        l = part_one(transformed)
        if l < min_length:
            min_length = l
    print(min_length)


if __name__ == "__main__":
    with open("day_05_input.txt", "r") as file:
        data = list(file.read().strip())
    print(part_one(data))
    part_two(data)
