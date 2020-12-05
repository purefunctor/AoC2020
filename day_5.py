from collections import Counter
from itertools import tee
from operator import itemgetter
import re


def parse_inputs():
    with open("./day_5.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def has_pairs(xs):
    ys, zs = tee(xs)
    next(zs)
    for y, z in zip(ys, zs):
        if y == z:
            return True
    return False


def solution_1():
    return sum([
        sum(itemgetter(*"aeiou")(Counter(line))) >= 3
        and has_pairs(line) and not re.search("(ab|cd|pq|xy)", line)
        for line in parse_inputs()
    ])


if __name__ == "__main__":
    print(solution_1())
