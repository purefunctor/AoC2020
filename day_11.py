from functools import lru_cache


def parse_inputs():
    with open("./day_11.txt", "r") as f:
        return f.read().splitlines()


@lru_cache(maxsize=None)
def get_adjacent(x, y):
    return [
        (xn, yn)
        for xn in range(x - 1, x + 2)
        for yn in range(y - 1, y + 2)
        if (x, y) != (xn, yn)
    ]


def board_mutate(mapping):
    _mapping = {}
    for (x, y), v in mapping.items():
        if v == "L":
            for xn, yn in get_adjacent(x, y):
                try:
                    if mapping[(xn, yn)] == "#":
                        _mapping[(x, y)] = "L"
                        break
                except KeyError:
                    pass
            else:
                _mapping[(x, y)] = "#"
        elif v == "#":
            n = 0
            for xn, yn in get_adjacent(x, y):
                try:
                    if mapping[(xn, yn)] == "#":
                        n += 1
                except KeyError:
                    pass
            if n >= 4:
                _mapping[(x, y)] = "L"
            else:
                _mapping[(x, y)] = "#"
        elif v == ".":
            _mapping[(x, y)] = v
    return _mapping


def solution_1():
    mapping_1 = {
        (x, y): v
        for x, ys in enumerate(parse_inputs())
        for y, v in enumerate(ys)
    }
    mapping_2 = board_mutate(mapping_1)

    while True:
        if mapping_1 == mapping_2:
            return sum(v == "#" for v in mapping_2.values())
        mapping_1, mapping_2 = mapping_2, board_mutate(mapping_2)


if __name__ == "__main__":
    print(solution_1())
