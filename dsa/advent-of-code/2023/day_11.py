EMPTY_SPACE = "."
GALAXY = "#"


def parsed_as_matrix(data):
    return [list(row.strip()) for row in data]


def transposed(matrix):
    return [list(row) for row in zip(*matrix)]


def contains_only_empty_space(row):
    return set(row) == {EMPTY_SPACE}


def with_expanded_rows(universe):
    expanded_rows = []

    for row in universe:
        expanded_rows.append(row)

        if contains_only_empty_space(row):
            expanded_rows.append(row)

    return expanded_rows


def print_universe(universe):
    for row in universe:
        print("".join(row))


def with_expanded_columns(universe):
    universe = transposed(universe)
    universe = with_expanded_rows(universe)
    return transposed(universe)


def galaxy_coordinates(universe):
    coordinates = []
    for y, row in enumerate(universe):
        for x, contents in enumerate(row):
            if contents == GALAXY:
                coordinates.append({"x": x, "y": y})

    return coordinates


def length_of_shortest_path(galaxy, other_galaxy):
    return sum(
        [
            max(galaxy[dimension], other_galaxy[dimension])
            - min(galaxy[dimension], other_galaxy[dimension])
            for dimension in ["x", "y"]
        ]
    )


def pairs_of_galaxies(galaxies):
    pairs = []

    for galaxy_index in range(len(galaxies) - 1):
        other_galaxy_index = galaxy_index + 1
        while other_galaxy_index < len(galaxies):
            pairs.append((galaxies[galaxy_index], galaxies[other_galaxy_index]))
            other_galaxy_index += 1

    return pairs


def lengths_of_shortest_path_between_every_pair_of_galaxies(galaxies):
    return [
        length_of_shortest_path(galaxy, other_galaxy)
        for galaxy, other_galaxy in pairs_of_galaxies(galaxies)
    ]


def part_one(data):
    universe = parsed_as_matrix(data)

    universe = with_expanded_rows(universe)
    universe = with_expanded_columns(universe)

    galaxies = galaxy_coordinates(universe)

    return sum(lengths_of_shortest_path_between_every_pair_of_galaxies(galaxies))


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as file:
        data = file.readlines()
    print(part_one(data))
