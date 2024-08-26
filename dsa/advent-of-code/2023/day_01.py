DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def first_digit(string):
    i = 0
    while i < len(string):
        if string[i].isdigit():
            return string[i]
        i += 1


def last_digit(string):
    i = len(string) - 1
    while i >= 0:
        if string[i].isdigit():
            return string[i]
        i -= 1


def part_one(lines):
    return sum([int(first_digit(line) + last_digit(line)) for line in lines])


def digits(line):
    result = []
    for index in range(len(line)):
        for word in DIGITS:
            start = index
            end = index + len(word)
            if line[start:end] == word:
                result.append(DIGITS[word])
        if line[index].isdigit():
            result.append(line[index])
    return result


def part_two(lines):
    line_numbers = []

    for line in lines:
        result = digits(line)
        line_numbers.append(int(result[0] + result[-1]))

    return sum(line_numbers)


if __name__ == "__main__":
    data = open("day_01_input.txt")
    print(part_two(data))
