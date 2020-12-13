from math import ceil
from operator import mul


def parse_inputs():
    with open("./day_13.txt", "r") as f:
        e, xs = f.read().splitlines()
        return int(e), [int(x) if x != "x" else None for x in xs.split(",")]


def solution_1():
    e, xs = parse_inputs()

    ys = [x for x in xs if x is not None]
    zs = [ceil(e / y) * y - e for y in ys]

    return mul(*min(zip(ys, zs), key=lambda yz: yz[1]))


if __name__ == "__main__":
    print(solution_1())
