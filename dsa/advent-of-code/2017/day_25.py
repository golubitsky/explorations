import re
from collections import defaultdict


def parsed(data):
    meta, *rest = data.split("\n\n")

    states = {}
    for state in rest:
        cur_state = re.search(r"In state (\w+)", state)[1]
        current_values = re.findall(r"value is (\d+)", state)
        write_values = re.findall(r"value (\d+)", state)
        moves = re.findall(r"to the (\w+)", state)
        next_states = re.findall(r"with state (\w+)", state)

        states[cur_state] = {}

        for i in range(2):
            states[cur_state][current_values[i]] = {
                "write": write_values[i],
                "move": -1 if moves[i] == "left" else 1,
                "next_state": next_states[i],
            }

    return {
        "starting_state": re.search(r"state (\w+)", meta)[1],
        "steps": int(re.search(r"(\d+) steps", meta)[1]),
        "states": states,
    }


def part_one(data):
    x = parsed(data)

    tape = defaultdict(lambda: "0")
    state = x["starting_state"]
    pos = 0

    for _ in range(x["steps"]):
        cur = x["states"][state][tape[pos]]
        tape[pos] = cur["write"]
        pos += cur["move"]
        state = cur["next_state"]

    print(list(tape.values()).count("1"))


if __name__ == "__main__":
    with open("day_25_input.txt", "r") as file:
        data = file.read()
    part_one(data)
