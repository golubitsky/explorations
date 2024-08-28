import heapq

from collections import deque, namedtuple
import math

NodeKey = namedtuple("NodeKey", "y x direction n_steps_in_direction")


RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

DIRECTIONS = [RIGHT, LEFT, UP, DOWN]
REVERSE_DIRECTION = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
VECTOR_BY_DIRECTION = {RIGHT: (0, 1), LEFT: (0, -1), UP: (-1, 0), DOWN: (1, 0)}


def parsed_as_matrix(data):
    return [list(row.strip()) for row in data]


def run_graph_diagnostics(graph):
    count_partial_missing = 0
    count_full_missing = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            found = False
            for d in DIRECTIONS:
                for s in range(4):
                    node = NodeKey(y, x, d, s)
                    try:
                        graph[node]
                        found = True
                    except KeyError:
                        # print(node)
                        count_partial_missing += 1
            if not found:
                count_full_missing += 1
    print(f"partially missing {count_partial_missing}")
    print(f"completely missing {count_full_missing}")


def initialize_graph_with_bfs_of_matrix(matrix):
    def add_to_graph(node_key):
        graph[node_key] = {
            # TODO: potentially delete below
            # "y": node_key.y,
            # "x": node_key.x,
            # "direction": node_key.direction,
            # "distance": 0 if node_key in start_node_keys else math.inf,
            # TODO: potentially delete above
            "cost": (
                0 if node_key == end_node_key else int(matrix[node_key.y][node_key.x])
            ),
            "neighbors": [],
        }

    def in_bounds(y, x):
        return y >= 0 and y < len(matrix) and x >= 0 and x < len(matrix[0])

    def debug_print(*args):
        if node_key != (0, 4, UP, 1):
            return
        print(*args)

    def neighbor_keys(node_key):
        keys = []
        for direction in DIRECTIONS:
            if direction == REVERSE_DIRECTION[node_key.direction]:
                continue  # crucible can't reverse

            if direction == node_key.direction:
                n_steps_in_direction = node_key.n_steps_in_direction + 1
            else:
                n_steps_in_direction = 0
            if n_steps_in_direction > 2:
                continue  # crucible can't go more than 3 in the same direction

            y_v, x_v = VECTOR_BY_DIRECTION[direction]
            y = node_key.y + y_v
            x = node_key.x + x_v

            if in_bounds(y, x):
                keys.append(NodeKey(y, x, direction, n_steps_in_direction))
        return keys

    graph = {}
    visited = set()

    start_node_keys = [
        NodeKey(y=0, x=0, direction=RIGHT, n_steps_in_direction=0),
        NodeKey(y=0, x=0, direction=DOWN, n_steps_in_direction=0),
    ]

    # For ending node, create an "extra" ending node that can be reached
    # from all the flavors of the "real" ending node. Its cost will be zero
    # and shouldn't affect the final result.
    end_node_key = NodeKey(len(matrix), len(matrix[0]), "X", "X")

    for node_key in start_node_keys:
        visited.add(node_key)
        add_to_graph(node_key)

    add_to_graph(end_node_key)

    queue = deque(start_node_keys.copy())

    while queue:
        node_key = queue.popleft()
        cur_node = graph[node_key]

        for neighbor_key in neighbor_keys(node_key):
            cur_node["neighbors"].append(neighbor_key)

            if neighbor_key not in visited:
                add_to_graph(neighbor_key)
                visited.add(neighbor_key)

                # Create one common ending node with a cost of zero.
                if (
                    neighbor_key.y == len(matrix) - 1
                    and neighbor_key.x == len(matrix[0]) - 1
                ):
                    graph[neighbor_key]["neighbors"].append(end_node_key)

                queue.append(neighbor_key)

    return graph, start_node_keys, end_node_key


def dijkstra(graph, start_node_key):
    pq = [(0, start_node_key)]
    heapq.heapify(pq)

    shortest_paths = {start_node_key: 0}
    previous_node_keys = {start_node_key: None}

    def debug_print(*args):
        return
        if cur_key != (0, 4, UP, 1):
            return
        print(*args)

    while pq:
        cur_distance, cur_key = heapq.heappop(pq)
        debug_print(f"cur node: {(cur_key.y, cur_key.x)}")
        debug_print(f"  cur distance: {cur_distance}")
        cur_node = graph[cur_key]
        debug_print(f'  neighbors: {[(k.y, k.x) for k in cur_node["neighbors"]]}')

        if cur_distance > shortest_paths.get(cur_key, math.inf):
            continue

        for neighbor_key in cur_node["neighbors"]:
            distance = cur_distance + graph[neighbor_key]["cost"]
            debug_print(f"  distance to neighbor: {distance}")

            if distance < shortest_paths.get(neighbor_key, math.inf):
                debug_print("shorter")
                shortest_paths[neighbor_key] = distance
                previous_node_keys[neighbor_key] = cur_key
                heapq.heappush(pq, (distance, neighbor_key))

    return shortest_paths, previous_node_keys


def print_matrix(matrix, previous, end_node_key):
    path = set()
    node_key = previous[end_node_key]
    while node_key:
        path.add((node_key.y, node_key.x))
        if node_key.y == 4:
            print(node_key)
        node_key = previous[node_key]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (y, x) in path:
                char = "x"
            else:
                char = matrix[y][x]

            print(char, end="")
        print()


def part_one(data):
    matrix = parsed_as_matrix(data)
    graph, start_node_keys, end_node_key = initialize_graph_with_bfs_of_matrix(matrix)

    for key in start_node_keys:
        shortest_paths, previous_node_keys = dijkstra(graph, key)
        if end_node_key in shortest_paths:
            # print_matrix(matrix, previous_node_keys, end_node_key)
            print(shortest_paths[end_node_key])


if __name__ == "__main__":
    with open("day_17_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
