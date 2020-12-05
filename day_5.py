from collections import Counter
from functools import reduce
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


def solution_2():
    nice = 0
    for line in parse_inputs():
        pair, num = Counter(map("".join, zip(line, line[1:]))).most_common(1)[0]
        if num == 1:
            continue
        if len(line) - len(re.sub(pair, "", line)) != 4:
            continue
        if not any(x == y for x, y in zip(line, line[2:])):
            continue
        nice += 1
    return nice


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
