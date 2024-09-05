KEYPAD = ["XX1XX", "X234X", "56789", "XABCX", "XXDXX"]


def solution(data):
    instruction_sets = [list(line.strip()) for line in data]
    vector_by_heading = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    pos = (1, 1)

    def in_bounds(pos):
        y, x = pos
        return y < 5 and x < 5 and x >= 0 and y >= 0 and KEYPAD[y][x] != "X"

    result = []
    for instruction_set in instruction_sets:
        for instruction in instruction_set:
            dy, dx = vector_by_heading[instruction]
            new_pos = (pos[0] + dy, pos[1] + dx)
            if in_bounds(new_pos):
                pos = new_pos

        result.append(KEYPAD[pos[0]][pos[1]])
    print("".join(result))


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as file:
        data = file.readlines()
    solution(data)
