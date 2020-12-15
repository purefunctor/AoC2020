from collections import deque


xs = "11,0,1,10,5,19"


def solution_1():
    numbers = deque(int(x) for x in reversed(xs.split(",")))
    spoken = {number: 1 for number in numbers}
    for _ in range(2020 - len(numbers)):
        if spoken.get(numbers[0], None) == 1:
            numbers.appendleft(0)
            spoken[0] += 1
        else:
            finder = (
                len(numbers) - index
                for index, number in enumerate(numbers)
                if number == numbers[0]
            )
            found = next(finder) - next(finder)
            numbers.appendleft(found)
            if found not in spoken:
                spoken[found] = 0
            spoken[found] += 1

    return numbers[0]


if __name__ == "__main__":
    print(solution_1())
