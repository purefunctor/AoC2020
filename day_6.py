def parse_inputs():
    with open("./day_6.txt", "r") as f:
        return [line.strip().split("\n") for line in f.read().split("\n\n")]


def solution_1():
    n = 0
    for group in parse_inputs():
        n += len(set("".join(group)))
    return n


if __name__ == "__main__":
    print(solution_1())
