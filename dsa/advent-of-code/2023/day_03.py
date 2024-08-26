import re
import math

def parsed(lines):
    def symbol_indexes(line):
        indexes = []

        for char_index, char in enumerate(line):
            if char in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}:
                continue
            indexes.append(char_index)

        return indexes

    symbols = set()
    numbers = []
    star_symbols = set()
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == '*':
                star_symbols.add((line_index, char_index))

        for char_index in symbol_indexes(line.strip()):
            symbols.add((line_index, char_index))

        for match in re.finditer(r"\d+", line):
            number_data = {
                "n": match.group(),
                "start": match.start(),
                "end": match.end() - 1,
                "line_index": line_index,
            }
            numbers.append(number_data)

    return {"numbers": numbers, "symbol_indexes": symbols, "star_symbols": star_symbols}


def part_one(parsed_data):
    def is_part_number(number):
        for line_index in range(number["line_index"] - 1, number["line_index"] + 2):
            for char_index in range(number["start"] - 1, number["end"] + 2):
                if (line_index, char_index) in parsed_data["symbol_indexes"]:
                    return True

        return False

    return sum(
        [
            int(number["n"])
            for number in parsed_data["numbers"]
            if is_part_number(number)
        ]
    )


def part_two(parsed_data):
    def is_gear(numbers_found):
        return len(numbers_found) == 2

    def number_key(n):
        return f"{n["line_index"]}{n["start"]}{n["end"]}-{n['n']}"

    numbers = {}
    for n in parsed_data["numbers"]:
        for char_index in range(n["start"], n["end"] + 1):
            position_key = (n['line_index'], char_index)
            numbers[position_key] = number_key(n)

    gear_ratios = []

    for line, char in parsed_data["star_symbols"]:
        numbers_found = set()

        adjacent_positions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for line_offset, char_offset in adjacent_positions:
            pos_to_check = (line + line_offset, char + char_offset)
            if pos_to_check in numbers:
                numbers_found.add(numbers[pos_to_check])

        if is_gear(numbers_found):
            gear_ratio = math.prod([int(n.split('-')[-1]) for n in numbers_found])
            gear_ratios.append(gear_ratio)

    return sum(gear_ratios)

if __name__ == "__main__":
    # data = open("03_input.txt")
    # print(part_one(parsed(data)))
    data = open("03_input.txt")
    print(part_two(parsed(data)))
