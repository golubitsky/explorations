import re


def is_valid(line, part):
    words = re.findall(r"\w+", line)
    if part == 2:
        words = ["".join(sorted(word)) for word in words]
    return len(words) == len(set(words))


def solution(data, part):
    return sum(is_valid(line, part) for line in data)


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as file:
        data = file.readlines()
    print(solution(data, part=1))
    print(solution(data, part=2))
