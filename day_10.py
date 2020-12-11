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


if __name__ == "__main__":
    print(solution_1())
