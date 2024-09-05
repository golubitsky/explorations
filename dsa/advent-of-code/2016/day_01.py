import re

HEADING_BY_CURRENT_HEADING = {
    "R": {
        "R": "D",
        "L": "U",
    },
    "L": {
        "R": "U",
        "L": "D",
    },
    "U": {
        "R": "R",
        "L": "L",
    },
    "D": {
        "R": "L",
        "L": "R",
    },
}


def part_one(data):
    directions = re.findall(r"\w+", data)
    vector_by_heading = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    y, x = 0, 0
    current_heading = "U"

    for direction in directions:
        heading, steps = direction[0], re.search(r'\d+', direction)
        steps = int(steps[0])

        current_heading = HEADING_BY_CURRENT_HEADING[current_heading][heading]
        dy, dx = vector_by_heading[current_heading]
        y += dy * steps
        x += dx * steps

    print(abs(y) + abs(x))


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as file:
        data = file.read()
    part_one(data)
