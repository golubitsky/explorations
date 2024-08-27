import re


def solution(data, part=1):
    extrapolated_values = []
    for line in data:
        sequences = [[int(x) for x in re.findall(r"-?\d+", line)]]
        while not all([x == 0 for x in sequences[-1]]):
            cur_seq = sequences[-1]
            next_sequence = []
            for i in range(len(cur_seq) - 1):
                next_sequence.append(cur_seq[i + 1] - cur_seq[i])
            sequences.append(next_sequence)

        print(sequences)
        if part == 1:
            i = len(sequences) - 2
            while i >= 0:
                cur = sequences[i][-1]
                prev = sequences[i + 1][-1]
                sequences[i].append(cur + prev)
                i -= 1
            extrapolated_values.append(sequences[0][-1])
        elif part == 2:
            i = len(sequences) - 2
            while i >= 0:
                cur = sequences[i][0]
                prev = sequences[i + 1][0]
                sequences[i].insert(0, cur - prev)

                i -= 1
            extrapolated_values.append(sequences[0][0])
        print(sequences)

    return sum(extrapolated_values)


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as file:
        data = file.readlines()
    # print(solution(data, part=1))
    print(solution(data, part=2))
