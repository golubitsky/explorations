import re
from collections import defaultdict


def parsed(line):
    match = re.search(r"Step (\w) must be finished before step (\w) can begin.", line)

    return match.groups()


def part_one(data):
    pairs = [parsed(line) for line in data]
    dependencies = defaultdict(list)
    letters = set()
    for dependency, target in pairs:
        dependencies[target].append(dependency)
        letters.add(dependency)
        letters.add(target)
    letters = sorted(letters)

    result = []
    target_length = len(letters)
    while len(result) != target_length:
        for letter in letters:
            if dependencies[letter] == []:
                result.append(letter)
                letters.remove(letter)
                for target in dependencies:
                    try:
                        dependencies[target].remove(letter)
                    except ValueError:  # not in list
                        pass
                break

    return "".join(result)


if __name__ == "__main__":
    with open("day_07_input.txt", "r") as file:
        data = file.readlines()
    print(part_one(data))
