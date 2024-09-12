def part_one(data):
    count_open = 0
    score = 0
    garbage = False
    cancel_next_char = False
    for char in data:
        if cancel_next_char:
            cancel_next_char = False
            continue

        if char == "!":
            cancel_next_char = True
        elif char == "{" and not garbage:
            count_open += 1
        elif char == "}" and not garbage:
            score += count_open
            count_open -= 1
        elif char == "<":
            garbage = True
        elif char == ">":
            if not garbage:
                raise RuntimeError("error closing garbage")
            garbage = False
    print(score)


def part_two(data):
    garbage = False
    cancel_next_char = False
    score = 0

    for char in data:
        if cancel_next_char:
            cancel_next_char = False
            continue

        if char == "<" and not garbage:
            garbage = True
        elif char == ">":
            garbage = False
        elif char == "!":
            cancel_next_char = True
        elif garbage:
            score += 1

    print(score)


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as file:
        data = file.read()
    part_one(data)
    part_two(data)
