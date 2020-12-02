from collections import Counter


def parse_inputs():
    with open("./day_2.txt", "r") as f:
        raw_lines = f.read()

    lines = []

    for raw_line in raw_lines.splitlines():
        raw_line = raw_line.replace(":", "")
        n, c, s = raw_line.split(" ")
        l, r = map(int, n.split("-"))
        lines.append(
            ((l, r), c, s)
        )

    return lines


def solution_1():
    return sum([
        l <= Counter(s)[c] <= r
        for (l, r), c, s in parse_inputs()
    ])


def solution_2():
    return sum([
        (s[l - 1] == c) ^ (s[r - 1] == c)
        for (l, r), c, s in parse_inputs()
    ])


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
