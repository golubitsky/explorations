EMPTY_SPACE = "."
GALAXY = "#"


def parsed_as_matrix(data):
    return [list(row.strip()) for row in data]


def transposed(matrix):
    return [list(row) for row in zip(*matrix)]


def contains_only_empty_space(row):
    return set(row) == {EMPTY_SPACE}


def galaxy_coordinates(universe):
    coordinates = []
    for y, row in enumerate(universe):
        for x, contents in enumerate(row):
            if contents == GALAXY:
                coordinates.append({"x": x, "y": y})

    return coordinates


def length_of_shortest_path(
    galaxy, other_galaxy, empty_row_indexes, empty_col_indexes, expansion_multiplier
):
    empty_indexes = {"x": empty_col_indexes, "y": empty_row_indexes}
    extra_distance_for_expansion_multiplier = (
        expansion_multiplier - 1
    )  # account for the row being expanded

    def index_between_galaxies(index, dimension):
        return index < max(galaxy[dimension], other_galaxy[dimension]) and index > min(
            galaxy[dimension], other_galaxy[dimension]
        )

    def dimension_distance_for_expansion(d):
        return sum(
            [
                extra_distance_for_expansion_multiplier
                for index in empty_indexes[d]
                if index_between_galaxies(index, d)
            ]
        )

    def dimension_distance(d):
        return (
            max(galaxy[d], other_galaxy[d])
            - min(galaxy[d], other_galaxy[d])
            + dimension_distance_for_expansion(d)
        )

    return sum([dimension_distance(dimension) for dimension in ["x", "y"]])


def pairs_of_galaxies(galaxies):
    pairs = []

    for galaxy_index in range(len(galaxies) - 1):
        other_galaxy_index = galaxy_index + 1
        while other_galaxy_index < len(galaxies):
            pairs.append((galaxies[galaxy_index], galaxies[other_galaxy_index]))
            other_galaxy_index += 1

    return pairs


def lengths_of_shortest_path_between_every_pair_of_galaxies(
    galaxies, empty_row_indexes, empty_column_indexes, expansion_multiplier
):
    return [
        length_of_shortest_path(
            galaxy,
            other_galaxy,
            empty_row_indexes,
            empty_column_indexes,
            expansion_multiplier,
        )
        for galaxy, other_galaxy in pairs_of_galaxies(galaxies)
    ]


def empty_row_indexes(universe):
    return [
        index for index, row in enumerate(universe) if contains_only_empty_space(row)
    ]


def empty_column_indexes(universe):
    return empty_row_indexes(transposed(universe))


def solution(data, expansion_multiplier):
    universe = parsed_as_matrix(data)
    galaxies = galaxy_coordinates(universe)
    lengths = lengths_of_shortest_path_between_every_pair_of_galaxies(
        galaxies,
        empty_row_indexes(universe),
        empty_column_indexes(universe),
        expansion_multiplier,
    )

    return sum(lengths)


def print_universe(universe):
    for row in universe:
        print("".join(row))


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as file:
        data = file.readlines()
    print(solution(data, expansion_multiplier=2))
    print(solution(data, expansion_multiplier=1000000))
