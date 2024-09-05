from collections import Counter
import math
import string


def is_real_room(letters, checksum):
    n = math.inf

    counts = Counter(letters)
    last_char = ""
    for char in checksum:
        if char not in counts:
            return False

        if counts[char] == n:
            if char > last_char:
                last_char = char
            else:
                return False
        elif counts[char] < n:
            n = counts[char]
            last_char = char
        elif counts[char] > n:
            return False

    return True


def parsed(line):
    letters, checksum = line.split("[")
    *letters, room_id = letters.split("-")
    letters = "".join(letters)
    room_id = int(room_id)
    checksum = checksum.split("]")[0]

    return letters, checksum, room_id


def part_one(data):
    real_rooms = []

    for line in data:
        letters, checksum, room_id = parsed(line)

        if is_real_room(letters, checksum):
            real_rooms.append(room_id)

    print(sum(real_rooms))


def cipher(letters, room_id):
    a = string.ascii_lowercase

    def char(x):
        return a[(a.index(x) + room_id) % len(a)]

    return "".join([char(x) for x in letters])


def part_two(data):
    for line in data:
        letters, checksum, room_id = parsed(line)
        words = cipher(letters, room_id)
        if "northpole" in words:
            print(room_id)


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    part_two(data)
