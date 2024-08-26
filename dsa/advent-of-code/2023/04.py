from collections import defaultdict
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
    counts = defaultdict(int)

    for card_index, line in enumerate(data):
        counts[card_index] += 1  # count the card itself
        winning_nums, my_nums = line.split(":")[-1].split("|")
        winning_nums = set(re.findall(r"\d+", winning_nums))
        my_nums = re.findall(r"\d+", my_nums)
        count_my_wins = sum([1 for num in my_nums if num in winning_nums])
        num_cards = counts[card_index]
        for win_index in range(card_index + 1, card_index + 1 + count_my_wins):
            counts[win_index] += num_cards

    return sum(counts.values())


if __name__ == "__main__":
    with open("04_input.txt", "r") as file:
        data = file.readlines()
    print(part_two(data))
