import re


def has_abba(string):
    if len(string) < 4:
        return False

    i = 0
    while i < len(string) - 3:
        s = string[i : i + 4]
        if s[0] != s[1] and s[0] == s[3] and s[1] == s[2]:
            return True
        i += 1
    return False


def parsed(line):
    standard = []
    hypernet = []
    sequence = []

    i = 0
    while i < len(line):
        if line[i] == "[":
            standard.append("".join(sequence))
            sequence = []
        elif line[i] == "]":
            hypernet.append("".join(sequence))
            sequence = []
        else:
            sequence.append(line[i])

        i += 1
    if sequence:
        standard.append("".join(sequence))

    return {"standard": standard, "hypernet": hypernet}


def supports_tls(line):
    p = parsed(line)

    standard_abba = [has_abba(s) for s in p["standard"]]
    hypernet_abba = [has_abba(s) for s in p["hypernet"]]

    if any(standard_abba) and not any(hypernet_abba):
        return True

    return False


def part_one(data):
    print(sum([supports_tls(line) for line in data]))


if __name__ == "__main__":
    with open("day_07_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
