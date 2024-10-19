from collections import defaultdict
import re


def parsed(data):
    guard_data = []
    current_guard = None
    for line in sorted(data):
        time_match = re.search(r"(\d+)-(\d+)-(\d+) (\d+):(\d+)", line)
        year = int(time_match[1])
        month = int(time_match[2])
        day = int(time_match[3])
        hour = int(time_match[4])
        minute = int(time_match[5])
        # print(year, month, day, hour, minute)

        state_match = re.search(r"Guard #(\d+) begins shift", line)
        if state_match:
            if current_guard is not None:
                guard_data.append(current_guard)

            current_guard = {"guard": int(state_match[1]), "transitions": []}
        else:
            state_match = re.search(r"falls asleep", line)
            if not state_match:
                state_match = re.search(r"wakes up", line)
            current_guard["transitions"].append((minute, state_match[0]))
    guard_data.append(current_guard)

    return guard_data


def solution(data):
    guard_data = parsed(data)
    sleep_times = defaultdict(int)
    sleep_minutes = {}
    for item in guard_data:
        if item["guard"] not in sleep_minutes:
            sleep_minutes[item["guard"]] = defaultdict(int)
        for minute, state in item["transitions"]:
            if state == "falls asleep":
                start = minute
            elif state == "wakes up":
                sleep_times[item["guard"]] += minute - start
                for m in range(start, minute):
                    sleep_minutes[item["guard"]][m] += 1
    # part 1
    id = max(sleep_times, key=sleep_times.get)
    m = max(sleep_minutes[id], key=sleep_minutes[id].get)
    print(id * m)

    # part 2
    max_sleep = 0
    max_sleep_minute = None
    max_sleep_guard = None
    for guard in sleep_minutes:
        if not sleep_minutes[guard]:
            continue
        m = max(sleep_minutes[guard], key=sleep_minutes[guard].get)
        if sleep_minutes[guard][m] > max_sleep:
            max_sleep_guard = guard
            max_sleep_minute = m
            max_sleep = sleep_minutes[guard][m]
    print(max_sleep_guard * max_sleep_minute)


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as file:
        data = file.readlines()
    solution(data)
