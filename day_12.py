import math
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


def rotate(x, y, d):
    r = math.radians(d)
    c, s = math.cos(r), math.sin(r)
    return (round(x * c - y * s), round(y * c + x * s))


def solution_2():
    # I'm lazy, probably could've done better
    sx, sy = 0, 0
    wx, wy = 10, 1
    waypoint_deltas = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0),
    }
    for i, n in parse_inputs():
        if i in "NEWS":
            xd, yd = waypoint_deltas[i]
            wx += xd * int(n)
            wy += yd * int(n)
        elif i == "F":
            sx += int(n) * wx
            sy += int(n) * wy
        elif i in "LR":
            n = int(n) if i == "L" else -int(n)
            wx, wy = rotate(wx, wy, n)
    return abs(sx) + abs(sy)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
