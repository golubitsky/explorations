import re
from itertools import cycle


def parsed(data):
    c = cycle("ABCDE")
    result = []
    for line in data:
        pos, velocity = [
            [int(value) for value in re.findall(r"-?\d+", item)]
            for item in line.split("@")
        ]
        result.append((pos, velocity))
    return result


def find_intersection(a, b):
    x1, y1, mx1, my1, x2, y2, mx2, my2 = (
        a[0][0],
        a[0][1],
        a[1][0],
        a[1][1],
        b[0][0],
        b[0][1],
        b[1][0],
        b[1][1],
    )
    # Calculate the determinant
    determinant = mx1 * my2 - my1 * mx2

    # If determinant is 0, the lines are parallel and do not intersect
    if determinant == 0:
        return None

    # Solve for t1 and t2 using Cramer's Rule
    t1_numerator = (x2 - x1) * my2 - (y2 - y1) * mx2
    t1 = t1_numerator / determinant

    t2_numerator = (x2 - x1) * my1 - (y2 - y1) * mx1
    t2 = t2_numerator / determinant

    # Calculate the intersection point using t1 (or t2)
    intersection_x = x1 + mx1 * t1
    intersection_y = y1 + my1 * t1

    precision = 3
    return round(intersection_x, precision), round(intersection_y, precision)


def part_one(data):
    hail_stones = parsed(data)

    min_value = 200000000000000
    max_value = 400000000000000

    combos = []
    for index, stone in enumerate(hail_stones):
        for other_stone in hail_stones[index + 1 :]:
            combos.append((stone, other_stone))

    count = 0

    def in_test_region(value):
        return value <= max_value and value >= min_value

    def dim_is_in_future(pos, interection, v):
        if v < 0:
            return pos > interection
        elif v > 0:
            return pos < interection
        elif v == 0:
            return pos == interection

    def is_in_future(intersection, particle):
        pos, velocity = particle
        pos, velocity = pos[:2], velocity[:2]
        for p, i, v in zip(pos, intersection, velocity):
            if not dim_is_in_future(p, i, v):
                return False
        return True

    for a, b in combos:
        intersection = find_intersection(a, b)
        if intersection is None:
            continue
        if not is_in_future(intersection, a):
            continue
        if not is_in_future(intersection, b):
            continue
        if all(in_test_region(dim) for dim in intersection):
            count += 1
    print(count)


if __name__ == "__main__":
    with open("day_24_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
