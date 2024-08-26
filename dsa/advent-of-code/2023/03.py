import re


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
    for line_index, line in enumerate(lines):
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

    return {"numbers": numbers, "symbol_indexes": symbols}


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


if __name__ == "__main__":
    data = open("03_input.txt")
    print(part_one(parsed(data)))
