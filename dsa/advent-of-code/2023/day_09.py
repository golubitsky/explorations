import re


def part_one(data):
    extrapolated_values = []
    for line in data:
        sequences = [[int(x) for x in re.findall(r"-?\d+", line)]]
        while not all([x == 0 for x in sequences[-1]]):
            cur_seq = sequences[-1]
            next_sequence = []
            for i in range(len(cur_seq) - 1):
                next_sequence.append(cur_seq[i + 1] - cur_seq[i])
            sequences.append(next_sequence)

        i = len(sequences) - 2
        while i >= 0:
            cur = sequences[i][-1]
            prev = sequences[i + 1][-1]
            sequences[i].append(cur + prev)
            i -= 1
        extrapolated_values.append(sequences[0][-1])

    return sum(extrapolated_values)


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as file:
        data = file.readlines()
    print(part_one(data))
