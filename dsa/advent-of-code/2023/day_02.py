import math
import re

PEBBLES_IN_BAG = {"red": 12, "green": 13, "blue": 14}


def parsed(line):
    def first_number(string):
        return re.search(r"\d+", string).group(0)

    def game_index(line):
        return first_number(line)

    def gem_count(set):
        return first_number(set)

    def color(gems):
        for color in PEBBLES_IN_BAG:
            if color in gems:
                return color

    def sets(line):
        results = []

        _, counts = line.split(":")

        for set in counts.split(";"):
            for gems in set.split(","):
                # For both parts it doesn't matter that all results are
                # independent of "rounds".
                results.append(
                    {
                        "color": color(gems),
                        "count": int(gem_count(gems)),
                        "game_index": int(game_index(line)),
                    }
                )

        return results

    return sets(line)


def part_one(lines):
    def is_round_possible(game):
        return PEBBLES_IN_BAG[game["color"]] >= game["count"]

    possible_games = []

    for line in lines:
        game = parsed(line)
        if all([is_round_possible(round) for round in (game)]):
            possible_games.append(game[0]["game_index"])

    return sum(possible_games)


def part_two(lines):
    powers = []

    for line in lines:
        game = parsed(line)

        needed = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for round in game:
            if round["count"] > needed[round["color"]]:
                needed[round["color"]] = round["count"]

        powers.append(math.prod(needed.values()))

    return sum(powers)


if __name__ == "__main__":
    data = open("day_02_input.txt")
    print(part_one(data))
    data = open("day_02_input.txt")
    print(part_two(data))
