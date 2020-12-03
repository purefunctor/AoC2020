from itertools import count


DELTA_X = 3
DELTA_Y = 1


def parse_inputs():
    with open("./day_3.txt", "r") as f:
        lines = f.readlines()

    max_y = len(lines)
    max_x = len(lines[0]) - 1

    return max_x, max_y, lines


def solution():
    max_x, max_y, lines = parse_inputs()

    coords = zip(
        (x % max_x for x in count(3, 3)),
        (range(1, max_y))
    )

    print(sum(lines[y][x] == "#" for x, y in coords))


if __name__ == "__main__":
    solution()
