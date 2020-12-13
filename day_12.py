import re


def parse_inputs():
    with open("./day_12.txt", "r") as f:
        return [
            re.match(r"([NEWSLRF])(\d+)", line).groups()
            for line in f.read().splitlines()
        ]


def solution_1():
    # I'm lazy, probably could've done better
    x = 0
    y = 0
    d = "NESW"
    c = 1
    for i, n in parse_inputs():
        if i == "N":
            y += int(n)
        elif i == "S":
            y -= int(n)
        elif i == "E":
            x += int(n)
        elif i == "W":
            x -= int(n)
        elif i == "F":
            l = d[c]
            if l == "N":
                y += int(n)
            elif l == "S":
                y -= int(n)
            elif l == "E":
                x += int(n)
            elif l == "W":
                x -= int(n)
        elif i == "L":
            c = int((c - (int(n) / 360 * 4)) % 4)
        elif i == "R":
            c = int((c + (int(n) / 360 * 4)) % 4)

    return abs(x) + abs(y)


if __name__ == "__main__":
    print(solution_1())
