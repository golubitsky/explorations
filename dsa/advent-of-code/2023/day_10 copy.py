def north(row, col):
    return [row - 1, col]


def south(row, col):
    return [row + 1, col]


def east(row, col):
    return [row, col + 1]


def west(row, col):
    return [row, col - 1]


def in_bound(row, col, data):
    return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])


def parsed(data):
    # parse as chars
    data = [list(line.strip()) for line in data]

    # convert to nodes
    for row in range(len(data)):
        for col in range(len(data[0])):
            char = data[row][col]
            data[row][col] = {"char": char, "edges": [], "row": row, "col": col}

    # add edges
    fns_by_char = {
        "|": [north, south],
        "-": [east, west],
        "L": [north, east],
        "J": [west, north],
        "7": [west, south],
        "F": [east, south],
        ".": [],
        # Handle starting node separately, last.
    }
    chars = set(fns_by_char.keys())

    starting_node = None
    for row in range(len(data)):
        for col in range(len(data[0])):
            cur_node = data[row][col]
            if cur_node["char"] in chars:
                for fn in fns_by_char[cur_node["char"]]:
                    adj_row, adj_col = fn(row, col)

                    if in_bound(adj_row, adj_col, data):
                        cur_node["edges"].append((adj_row, adj_col))
                    # else:
                    #     print(f"out of range: skipping {fn.__name__} for {row}, {col}")
            elif cur_node['char'] == 'S':
                # Handle starting node separately, last.
                starting_node = data[row][col]
            else:
                print(f"unknown char {cur_node["char"]}")
                exit()

    # Add edges for S node
    r = starting_node['row']
    c = starting_node['col']
    for fn in [north, east, south, west]:
        row_adj, col_adj = fn(r, c)

        if in_bound(row_adj, col_adj, data):
            adjacent_node = data[row_adj][col_adj]
            if (r, c) in adjacent_node['edges']:
                starting_node['edges'].append((row_adj, col_adj))

    return (data, starting_node)


def pick_edge(node, previous_node):
    if node['char'] == 'S':
        # doesn't matter which way we go because starting node is
        # guaranteed to be part of circular pipe
        return node['edges'][0]
    else:
        for edge in node['edges']:
            if edge != (previous_node['row'], previous_node['col']):
                return edge


def part_one(data):
    data, starting_node = parsed(data)

    previous_node = None
    node = starting_node
    starting_node['in_loop'] = True # for part 2
    adj_row, adj_col = pick_edge(node, previous_node)
    node, previous_node = data[adj_row][adj_col], node
    steps_to_get_back_to_start = 1 # already took one step away from start
    
    while node != starting_node:
        node['in_loop'] = True # for part 2
        adj_row, adj_col = pick_edge(node, previous_node)
        node, previous_node = data[adj_row][adj_col], node
        steps_to_get_back_to_start += 1

    # print("loop steps:", steps_to_get_back_to_start)
    # print("to point furthest:", steps_to_get_back_to_start//2)
    return data

def print_grid_for_part_two(data):
    print('  01234567890')
    for row in range(len(data)):
        print(row, end=' ')

        for col in range(len(data[0])):
            cur = data[row][col]
            if 'in_loop' in cur:
                print('*', end='')
            else:
                print('.', end='')
        print()
    print()

def part_two(data):
    print_grid_for_part_two(data)

    # "L": [north, east],
    # "J": [west, north],
    # "7": [west, south],
    # "F": [east, south],
    starting_y = 0
    starting_x = 0
    count_inside = 0
    while starting_x < len(data[0]):
        inside = False
        y = starting_y
        x = starting_x
        while x < len(data[0]) and y < len(data):
            cur = data[y][x]
            if 'in_loop' in cur:
                if cur['char'] not in '7L':
                    inside = not inside
            else:
                if inside:
                    count_inside += 1
            x += 1
            y += 1
        starting_x += 1
    starting_y = 1
    starting_x = 0
    while starting_y < len(data):
        y = starting_y
        x = starting_x
        while x < len(data[0]) and y < len(data):
            cur = data[y][x]
            if 'in_loop' in cur:
                if cur['char'] not in '7L':
                    inside = not inside
            else:
                if inside:
                    count_inside += 1
            x += 1
            y += 1
        starting_y += 1

    print(count_inside)


if __name__ == "__main__":
    with open("day_10_sample_3.txt", "r") as file:
        data = file.readlines()
    data = part_one(data)
    part_two(data)
