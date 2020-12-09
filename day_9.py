from collections import deque


def parse_inputs():
    with open("./day_9.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def solution_1():
    numbers = iter(parse_inputs())
    preamble = dict.fromkeys(next(numbers) for _ in range(25))

    for current in numbers:
        for previous in preamble:
            if abs(current - previous) in preamble:
                break
        else:
            return current
        preamble[current] = None
        preamble.pop(next(iter(preamble)))


def solution_2():
    queue = deque()
    total = 0

    invalid = solution_1()
    numbers = parse_inputs()

    for number in numbers:
        queue.append(number)
        total += number
        while total > invalid:
            total -= queue.popleft()
        if total == invalid:
            return min(queue) + max(queue)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
