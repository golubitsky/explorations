from collections import defaultdict


def parsed_instruction(line):
    a, b = line.split("if")
    a = a.split("inc")
    if len(a) == 2:
        instruction = "inc"
    else:
        a = a[0].split("dec")
        instruction = "dec"
    a = [x.strip() for x in a]
    a[1] = int(a[1])
    a[1] = a[1] if instruction == "inc" else a[1] * -1

    other_reg, comparator, required_amount = b.split()
    required_amount = int(required_amount)

    return {
        "register": a[0],
        "amount": a[1],
        "other_reg": other_reg,
        "comparator": comparator,
        "required_amount": required_amount,
    }


def eval_comparator(a, b, comparator):
    return eval(f"{a} {comparator} {b}")


def solution(data):
    instructions = [parsed_instruction(line.strip()) for line in data]

    registers = defaultdict(int)
    highest_max = 0

    for instruction in instructions:
        if eval_comparator(
            registers[instruction["other_reg"]],
            instruction["required_amount"],
            instruction["comparator"],
        ):
            registers[instruction["register"]] += instruction["amount"]
            if registers[instruction["register"]] > highest_max:
                highest_max = registers[instruction["register"]]

    print(highest_max)


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as file:
        data = file.readlines()
    solution(data)
