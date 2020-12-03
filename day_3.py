from itertools import count


DELTA_X = 3
DELTA_Y = 1


def parse_inputs():
    with open("./day_3.txt", "r") as f:
        lines = list(map(str.strip, f.readlines()))

    max_y = len(lines)
    max_x = len(lines[0])

    return max_x, max_y, lines


def solution_1():
    max_x, max_y, lines = parse_inputs()

    coords = zip(
        (x % max_x for x in count(DELTA_X, DELTA_X)),
        (range(DELTA_Y, max_y, DELTA_Y))
    )

    return sum(lines[y][x] == "#" for x, y in coords)


def solution_2():
    max_x, max_y, lines = parse_inputs()

    def create_coords(dx, dy):
        return zip(
            (x % max_x for x in count(dx, dx)),
            (range(dy, max_y, dy)),
        )

    deltas = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    prod = 1
    for dx, dy in deltas:
        prod *= sum(lines[y][x] == "#" for x, y in create_coords(dx, dy))

    return prod


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
