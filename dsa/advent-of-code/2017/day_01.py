def parsed(data):
    return [int(x) for x in data]


def solution(data, offset):
    digits = parsed(data)
    i = 0
    total = 0
    while i < len(digits):
        digit = digits[i]
        other_digit = digits[(i + offset) % len(digits)]

        if digit == other_digit:
            total += digit
        i += 1

    print(total)


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as file:
        data = file.read()
    solution(data, offset=1)
    solution(data, offset=len(data.strip()) // 2)
