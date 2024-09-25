from collections import defaultdict


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def value(str, registers):
    return int(str) if is_int(str) else registers[str]


def set_instr(x, y, registers):
    registers[x] = value(y, registers)


def decrease(x, y, registers):
    registers[x] -= value(y, registers)


def multiply(x, y, registers):
    registers[x] *= value(y, registers)


def part_one(data):
    functions = {"set": set_instr, "sub": decrease, "mul": multiply}
    registers = defaultdict(int)
    index = 0

    count = 0

    while index >= 0 and index < len(data):
        instruction, x, y = data[index].split()

        if instruction == "mul":
            count += 1

        if instruction == "jnz":
            if value(x, registers) != 0:
                index += value(y, registers)
            else:
                index += 1
        else:
            functions[instruction](x, y, registers)
            index += 1

    print(count)

if __name__ == "__main__":
    with open("day_23_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
