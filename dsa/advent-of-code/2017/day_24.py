import re


def parsed(data):
    return [tuple(int(x) for x in re.findall(r"\d+", line)) for line in data]


def starting_components(components):
    # sorted because we have to start with a zero
    return [tuple(sorted(c)) for c in components if 0 in c]


def rest_without(target, components):
    c = components.copy()

    try:
        index = c.index(target)
    except ValueError:
        index = c.index(tuple(reversed(target)))

    c.pop(index)

    return c


def fits(component, path):
    return path[-1][-1] == component[0]


def reversed_comps(components):
    # don't reverse components with identical ports
    return [tuple(reversed(c)) for c in components if c[0] != c[1]]


def solution(data):
    all_components = parsed(data)
    all_paths = []

    def find_paths(components, path):
        for component in components + reversed_comps(components):
            if not fits(component, path):
                continue
            find_paths(
                components=rest_without(component, components), path=[*path, component]
            )

        all_paths.append(path)

    def strongest(paths):
        return max(sum([sum(x) for x in p]) for p in paths)

    for start in starting_components(all_components):
        find_paths(components=rest_without(start, all_components), path=[start])

    # part 1
    print(strongest(all_paths))

    # part 2
    longest_length = max(len(x) for x in all_paths)
    longest_paths = [x for x in all_paths if len(x) == longest_length]
    print(strongest(longest_paths))


if __name__ == "__main__":
    with open("day_24_input.txt", "r") as file:
        data = file.readlines()
    solution(data)
