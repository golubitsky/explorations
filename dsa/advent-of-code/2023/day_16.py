from collections import namedtuple
from time import sleep
import os

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

HORIZONTAL_SPLITTER = "-"
VERTICAL_SPLITTER = "|"
EMPTY = "."

HEADING_BY_MIRROR = {
    "\\": {
        RIGHT: DOWN,
        DOWN: RIGHT,
        LEFT: UP,
        UP: LEFT,
    },
    "/": {
        RIGHT: UP,
        UP: RIGHT,
        DOWN: LEFT,
        LEFT: DOWN,
    },
}

VECTOR_BY_HEADING = {RIGHT: (0, 1), LEFT: (0, -1), UP: (-1, 0), DOWN: (1, 0)}

CHAR_BY_HEADING = {RIGHT: ">", LEFT: "<", DOWN: "v", UP: "^"}

Beam = namedtuple("Beam", "y x heading")


def parsed_as_matrix(data):
    return [list(row.strip()) for row in data]


def print_matrix(matrix, beams):
    os.system("clear")
    print("  0123456789")
    for y in range(len(matrix)):
        print(y, end=" ")

        for x in range(len(matrix[0])):

            value = matrix[y][x]

            if value == EMPTY:
                beams_present = [beam for beam in beams if beam.x == x and beam.y == y]
                n = len(beams_present)

                if n == 1:
                    value = CHAR_BY_HEADING[beams_present[0].heading]
                elif n >= 2:
                    value = n

            print(value, end="")
        print()


def possible_starting_beams(matrix):
    beams = []

    for x in range(len(matrix[0])):
        beams.append(Beam(y=0, x=x, heading=DOWN))
        beams.append(Beam(y=len(matrix) - 1, x=x, heading=UP))

    for y in range(len(matrix)):
        beams.append(Beam(y=y, x=0, heading=RIGHT))
        beams.append(Beam(y=y, x=len(matrix[0]) - 1, heading=LEFT))

    return beams


def solution(data):
    def is_at_wall(beam):
        y, x = beam.y, beam.x
        return y < 0 or y == len(matrix) or x < 0 or x == len(matrix[0])

    def with_new_pos(beam):
        y_v, x_v = VECTOR_BY_HEADING[beam.heading]
        return Beam(y=beam.y + y_v, x=beam.x + x_v, heading=beam.heading)

    def with_reflection(beam):
        item = matrix[beam.y][beam.x]
        is_at_mirror = item in HEADING_BY_MIRROR

        if not is_at_mirror:
            return beam

        return Beam(beam.y, beam.x, HEADING_BY_MIRROR[item][beam.heading])

    def with_split(beam):
        item = matrix[beam.y][beam.x]
        is_at_split = item in [HORIZONTAL_SPLITTER, VERTICAL_SPLITTER]

        if not is_at_split:
            return [beam]

        if item == HORIZONTAL_SPLITTER:
            if beam.heading in [UP, DOWN]:
                return [Beam(beam.y, beam.x, LEFT), Beam(beam.y, beam.x, RIGHT)]
            else:
                return [beam]  # ignore splitter
        if item == VERTICAL_SPLITTER:
            if beam.heading in [LEFT, RIGHT]:
                return [Beam(beam.y, beam.x, UP), Beam(beam.y, beam.x, DOWN)]
            else:
                return [beam]  # ignore splitter

        return [beam]

    def moved_beams(beams):
        new_beams = []

        for beam in beams:
            beam = with_reflection(beam)
            beam = with_new_pos(beam)
            if is_at_wall(beam):
                continue  # i.e., disappear

            energized_tiles.add((beam.y, beam.x))

            for beam in with_split(beam):
                if beam in beam_cache:
                    continue  # kill the beam!!

                beam_cache.add(beam)
                new_beams.append(beam)

        return new_beams

    matrix = parsed_as_matrix(data)
    max_energy = 0
    for starting_beam in possible_starting_beams(matrix):
        energized_tiles = set()
        beam_cache = set()

        beams = [starting_beam]
        energized_tiles.add((starting_beam.y, starting_beam.x))
        beam_cache.add(starting_beam)

        while beams:
            beams = moved_beams(beams)
            # sleep(2.2)
            # print_matrix(matrix, beams)
        if len(energized_tiles) > max_energy:
            max_energy = len(energized_tiles)
    print(max_energy)


if __name__ == "__main__":
    with open("day_16_input.txt", "r") as file:
        data = file.readlines()
    solution(data)
