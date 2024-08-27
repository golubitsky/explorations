def north(row, col):
    return (row - 1, col)


def south(row, col):
    return (row + 1,col)


def east(row, col):
    return (row,col + 1)


def west(row, col):
    return (row,col - 1)

def in_bound(row, col, data):
    return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])

def part_one(data):
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
                    else:
                        print(f"out of range: skipping {fn.__name__} for {row}, {col}")
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
    print(starting_node)


if __name__ == "__main__":
    with open("day_10_sample.txt", "r") as file:
        data = file.readlines()
    print(part_one(data))
