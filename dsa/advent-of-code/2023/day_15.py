def hash(word):
    value = 0
    for char in word:
        if char in {"\n"}:
            continue

        value += ord(char)
        value *= 17
        value %= 256
    return value


def part_one(data):
    data = data.split(",")
    return sum([hash(word) for word in data])


if __name__ == "__main__":
    with open("day_15_input.txt", "r") as file:
        data = file.read()
    print(part_one(data))
