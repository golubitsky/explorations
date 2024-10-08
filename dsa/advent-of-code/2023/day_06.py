import re
import math


def part_one(data):
    data = [[int(x) for x in re.findall(r"\d+", line)] for line in data]
    time, distance = data
    races = list(zip(time, distance))

    ways_to_win = []

    for time, best_distance in races:
        ways_to_win_this_race = 0
        for time_held_down in range(1, time + 1):
            time_remaining = time - time_held_down
            distance = time_held_down * time_remaining
            if distance > best_distance:
                ways_to_win_this_race += 1
        ways_to_win.append(ways_to_win_this_race)

    return math.prod(ways_to_win)


def part_two(data):
    data = [int("".join(re.findall(r"\d+", line))) for line in data]
    time, best_distance = data

    ways_to_win = 0

    for time_held_down in range(1, time + 1):
        time_remaining = time - time_held_down
        distance = time_held_down * time_remaining
        if distance > best_distance:
            ways_to_win += 1

    return ways_to_win


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as file:
        data = file.readlines()
    print(part_two(data))
