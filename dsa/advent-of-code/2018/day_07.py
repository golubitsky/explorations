import re
import string
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


def cost(letter):
    return string.ascii_uppercase.index(letter) + 1


def new_worker():
    return {"time": 0, "letter": None}


def part_two(queue):
    queue = list(queue)
    workers = []
    for _ in range(2):
        workers.append(new_worker())

    while len(queue) > 0:
        letter = queue.pop(0)
        # TODO: still need dependencies here,
        # in case multiple letters are available simultaneously
    print(string.ascii_uppercase.index("Z") + 1)
    print(queue)


if __name__ == "__main__":
    with open("day_07_sample.txt", "r") as file:
        data = file.readlines()
    result = part_one(data)
    part_two(result)
