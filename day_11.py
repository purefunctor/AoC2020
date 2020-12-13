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


def make_beam_gun(size_x, size_y):
    @lru_cache(maxsize=None)
    def beam_gun(x, y):
        beams = []
        for (xd, yd) in get_adjacent(0, 0):
            beam_group = []
            multiplier = 1
            while True:
                xn = xd * multiplier + x
                yn = yd * multiplier + y
                if 0 > xn or xn >= size_x or 0 > yn or yn >= size_y:
                    break
                beam_group.append((xn, yn))
                multiplier += 1
            beams.append(beam_group)
        return beams
    return beam_gun


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


def board_mutate_with_beam_gun(mapping, beam_gun):
    _mapping = {}
    for (x, y), v in mapping.items():
        if v == "L":
            for beam_group in beam_gun(x, y):
                do = ""
                for xn, yn in beam_group:
                    seeing = mapping[(xn, yn)]
                    if seeing == ".":
                        continue
                    elif seeing == "L":
                        do = "continue"
                        break
                    else:
                        do = "break"
                        break
                if do == "continue":
                    continue
                elif do == "break":
                    _mapping[(x, y)] = "L"
                    break
            else:
                _mapping[(x, y)] = "#"
        elif v == "#":
            n = 0
            for beam_group in beam_gun(x, y):
                next_group = False
                for xn, yn in beam_group:
                    seeing = mapping[(xn, yn)]
                    if seeing == ".":
                        continue
                    elif seeing == "L":
                        next_group = True
                        break
                    else:
                        n += 1
                        break
                if next_group:
                    continue
            if n >= 5:
                _mapping[(x, y)] = "L"
            else:
                _mapping[(x, y)] = "#"
        elif v == ".":
            _mapping[(x, y)] = v
    return _mapping


def solution_2():
    xs = parse_inputs()
    mapping_1 = {
        (x, y): v
        for x, ys in enumerate(xs)
        for y, v in enumerate(ys)
    }
    beam_gun = make_beam_gun(len(xs), len(xs[0]))
    mapping_2 = board_mutate_with_beam_gun(mapping_1, beam_gun)

    while True:
        if mapping_1 == mapping_2:
            return sum(v == "#" for v in mapping_2.values())
        mapping_1, mapping_2 = mapping_2, board_mutate_with_beam_gun(mapping_2, beam_gun)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
