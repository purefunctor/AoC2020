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


def solution_2():
    _, xs = parse_inputs()
    xs = [(i, x) for i, x in enumerate(xs) if x is not None]

    ys = [x for (_, x) in xs]
    zs = [-i % y for i, y in xs]

    earliest = 0
    delta = 1

    for y, z in zip(ys, zs):
        while earliest % y != z:
            earliest += delta
        delta *= y

    return earliest


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
