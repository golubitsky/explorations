import re


def parsed(data):
    return [int(re.match(r"-?\d+", line)[0]) for line in data]


def solution(data, part):
    jumps = parsed(data)
    pos = 0
    count = 0
    while pos < len(data) and pos >= 0:
        n = jumps[pos]
        if part == 1:
            jumps[pos] += 1
        elif part == 2:
            if n >= 3:
                jumps[pos] -= 1
            else:
                jumps[pos] += 1
        pos = pos + n
        count += 1
    print(count)


if __name__ == "__main__":
    with open("day_05_input.txt", "r") as file:
        data = file.readlines()
    solution(data, part=1)
    solution(data, part=2)
