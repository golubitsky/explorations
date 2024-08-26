import re


def part_one(data):
    total_count = 0
    for line in data:
        winning_nums, my_nums = line.split(":")[-1].split("|")
        winning_nums = set(re.findall(r"\d+", winning_nums))
        my_nums = re.findall(r"\d+", my_nums)
        count_my_wins = sum([1 for num in my_nums if num in winning_nums])
        if count_my_wins > 0:
            total_count += 2 ** (count_my_wins - 1)
    return total_count


def part_two(data):
    pass


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as file:
        data = file.readlines()
    print(part_two(data))
