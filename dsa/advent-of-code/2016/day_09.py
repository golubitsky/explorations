import re

NORMAL = 0
PAREN_OPEN = 1
IMPLEMENTING_COMPRESSION = 2


def parse_paren(paren):
    n_chars, n_repeat = re.findall(r"\d+", "".join(paren))

    return {"n_chars": int(n_chars), "n_repeats": int(n_repeat)}


def part_one(data):
    decompressed = []
    paren = []
    state = NORMAL
    i = 0
    while i < len(data):
        char = data[i]
        if state == NORMAL:
            if char == "(":
                paren = []
                state = PAREN_OPEN
            else:
                decompressed.append(char)
            i += 1
        elif state == PAREN_OPEN:
            if char != ")":
                paren.append(char)
            elif char == ")":
                paren = parse_paren(paren)
                state = IMPLEMENTING_COMPRESSION
            i += 1
        elif state == IMPLEMENTING_COMPRESSION:
            s = data[i : i + paren["n_chars"]] * paren["n_repeats"]
            decompressed.append(s)
            state = NORMAL
            i += paren["n_chars"]

    return len("".join(decompressed))


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as file:
        data = file.read().strip()
    print(part_one(data))
