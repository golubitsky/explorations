VECTOR_BY_DIRECTION = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def parsed(data):
    y_len = len(data)
    x_len = len(data[1].strip())
    start_pos = (y_len // 2, x_len // 2)

    infected = set()

    for y in range(y_len):
        for x in range(x_len):
            if data[y][x] == "#":
                infected.add((y, x))

    return start_pos, infected


def part_one(data):
    def new_direction(pos, direction, infected):
        if pos in infected:
            return {"up": "right", "down": "left", "left": "up", "right": "down"}[
                direction
            ]
        else:
            return {"up": "left", "down": "right", "left": "down", "right": "up"}[
                direction
            ]

    def new_pos(pos, direction):
        dy, dx = VECTOR_BY_DIRECTION[direction]

        return (pos[0] + dy, pos[1] + dx)

    def simulate_one_burst(pos, direction, infected):
        caused_infection = False

        direction = new_direction(pos, direction, infected)

        if pos in infected:
            infected.remove(pos)
        else:
            infected.add(pos)
            caused_infection = True

        return new_pos(pos, direction), direction, caused_infection

    pos, infected = parsed(data)
    direction = "up"

    infection_bursts = 0

    for _ in range(10000):
        pos, direction, caused_infection = simulate_one_burst(pos, direction, infected)

        if caused_infection:
            infection_bursts += 1

    print(infection_bursts)


if __name__ == "__main__":
    with open("day_22_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
