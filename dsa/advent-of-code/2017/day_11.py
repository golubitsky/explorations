from collections import Counter


def part_one(data):
    a = Counter(data.strip().split(","))
    a["ne"] -= 1326
    a["sw"] -= 1326
    a["n"] -= 1057
    a["s"] -= 1057
    a["nw"] -= 1297
    a["se"] -= 1297
    print(a)

    # remainder: {'n': 422, 'ne': 342, 'nw': 99,
    #   422 (north)
    # + 99  (north "components" of both ne and nw)
    # + 243 (342 - 99 of each of the ne/nw "cancel out")
    # = 764
    # That's the least code I've ever written to solve one of these.
    # Although I can't solve part two like this.


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as file:
        data = file.read()
    part_one(data)
