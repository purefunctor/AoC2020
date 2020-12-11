from functools import lru_cache


def parse_inputs():
    with open("./day_10.txt") as f:
        return [int(line) for line in f.readlines()]


def solution_1():
    joltages = set(parse_inputs())

    current = 0
    deltas = [0, 0, 1]  # Accounts for the device's joltage

    while joltages:
        for delta in range(1, 4):
            expected = current + delta
            if expected in joltages:
                joltages.remove(expected)
                deltas[expected - current - 1] += 1
                current = expected
                break

    return deltas[0] * deltas[2]


def solution_2():
    joltages = set(parse_inputs())
    joltages.add(0)
    joltages.add(max(joltages) + 3)

    joltages_subpaths = {
        joltage: [
            expected
            for expected in range(joltage + 1, joltage + 4)
            if expected in joltages
        ]
        for joltage in joltages
    }

    @lru_cache(maxsize=None)
    def check_branching(current):
        subpaths = joltages_subpaths[current]
        possible = len(subpaths)
        if possible == 0:
            return 0
        elif possible == 1:
            return check_branching(subpaths[0])
        else:
            paths = 0
            for subpath in subpaths:
                branches = check_branching(subpath)
                if branches == 0:
                    paths += 1
                else:
                    paths += branches
            return paths

    return check_branching(0)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
