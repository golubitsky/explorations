import math
import re


def read_with_default(d, key):
    # Any source numbers that aren't mapped correspond to the same destination number.
    # So, seed number 10 corresponds to soil number 10.
    for map_range in d:
        if map_range["min_in_range"] <= key and map_range["max_in_range"] >= key:
            return key + map_range["offset"]

    return key


def parsed_map(map):
    result = []
    for line in map.split("\n")[1:]:
        destination, source, len_range = [int(value) for value in line.split()]
        result.append(
            {
                "offset": destination - source,
                "min_in_range": source,
                "max_in_range": source + len_range,
            }
        )
    return result


def seeds_part_one(seeds):
    return [int(seed) for seed in re.findall(r"\d+", seeds)]


def part_one(data):
    seeds, *maps = data.split("\n\n")
    (
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ) = [parsed_map(map) for map in maps]
    seeds = seeds_part_one(seeds)
    lowest = math.inf
    for seed in seeds:
        soil = read_with_default(seed_to_soil, seed)
        fertilizer = read_with_default(soil_to_fertilizer, soil)
        water = read_with_default(fertilizer_to_water, fertilizer)
        light = read_with_default(water_to_light, water)
        temperature = read_with_default(light_to_temperature, light)
        humidity = read_with_default(temperature_to_humidity, temperature)
        location = read_with_default(humidity_to_location, humidity)

        if location < lowest:
            lowest = location

    return lowest


def seeds_part_two(seeds):
    result = []
    seeds = re.findall(r"\d+", seeds)
    for i in range(0, len(seeds), 2):
        seed, seed_range = [int(x) for x in seeds[i : i + 2]]
        result.append(
            {
                "min_in_range": seed,
                "max_in_range": seed + seed_range - 1,
            }
        )
    return result


def part_two(data):
    seeds, *maps = data.split("\n\n")
    (
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ) = [parsed_map(map) for map in maps]
    seeds = seeds_part_two(seeds)

    def location(seed, lowest):
        soil = read_with_default(seed_to_soil, seed)
        fertilizer = read_with_default(soil_to_fertilizer, soil)
        water = read_with_default(fertilizer_to_water, fertilizer)
        light = read_with_default(water_to_light, water)
        temperature = read_with_default(light_to_temperature, light)
        humidity = read_with_default(temperature_to_humidity, temperature)
        location = read_with_default(humidity_to_location, humidity)

        if location < lowest["l"]:
            lowest["l"] = location
        return [location, lowest]

    lowest = {"l": math.inf}

    def is_monotonically_increasing(low, high, lowest):
        input_offset = low - high
        low_result, lowest = location(high, lowest)
        (
            high_result,
            lowest,
        ) = location(low, lowest)
        output_offset = high_result - low_result

        return input_offset == output_offset

    def non_monotonically_increasing_ranges(low, high, lowest, ranges):
        if high <= low + 1:
            return

        if is_monotonically_increasing(low, high, lowest):
            return

        mid = (low + high) // 2

        non_monotonically_increasing_ranges(low, mid, lowest, ranges)
        non_monotonically_increasing_ranges(mid, high, lowest, ranges)

        # Ensure no inner ranges exist within the current range
        if not any(start <= high and end >= low for start, end in ranges):
            ranges.append((low, high))

    ranges = []
    for seed_range in reversed(seeds):
        low, high = seed_range["min_in_range"], seed_range["max_in_range"]
        non_monotonically_increasing_ranges(low, high, lowest, ranges)
        for low, high in ranges:
            i = low
            while i <= high:
                location(i, lowest)
                i += 1
    return lowest["l"]


if __name__ == "__main__":
    with open("05_input.txt", "r") as file:
        data = file.read()
    print(part_two(data))
    # TODO: 50716417 too high
