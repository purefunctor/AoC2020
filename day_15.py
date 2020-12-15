from collections import defaultdict, deque


xs = [int(x) for x in "11,0,1,10,5,19".split(",")]


def solution(xs, lim):
    latest = xs[-1]
    spoken = defaultdict(deque, {x: deque([turn]) for turn, x in enumerate(xs, start=1)})
    for turn in range(len(xs) + 1, lim + 1):
        if len(spoken[latest]) == 1:
            latest = 0
            spoken[0].append(turn)
        else:
            first = spoken[latest].pop()
            second = spoken[latest].pop()
            spoken[latest].append(first)
            latest = first - second
            spoken[latest].append(turn)
    return latest


def solution_1():
    return solution(xs, 2020)


def solution_2():
    return solution(xs, 30000000)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
