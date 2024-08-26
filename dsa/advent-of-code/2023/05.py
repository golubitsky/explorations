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
    seeds = [int(seed) for seed in re.findall(r"\d+", seeds)]
    lowest_location = math.inf
    for seed in seeds:
        soil = read_with_default(seed_to_soil, seed)
        fertilizer = read_with_default(soil_to_fertilizer, soil)
        water = read_with_default(fertilizer_to_water, fertilizer)
        light = read_with_default(water_to_light, water)
        temperature = read_with_default(light_to_temperature, light)
        humidity = read_with_default(temperature_to_humidity, temperature)
        location = read_with_default(humidity_to_location, humidity)

        if location < lowest_location:
            lowest_location = location

    return lowest_location


if __name__ == "__main__":
    with open("05_input.txt", "r") as file:
        data = file.read()
    print(part_one(data))
