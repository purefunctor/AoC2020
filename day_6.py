from functools import reduce


def parse_inputs():
    with open("./day_6.txt", "r") as f:
        return [line.strip().split("\n") for line in f.read().split("\n\n")]


def solution_1():
    return sum(len(set("".join(group))) for group in parse_inputs())


def solution_2():
    return sum(len(list(reduce(lambda x, y: x & y, map(set, group)))) for group in parse_inputs())


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
