from itertools import repeat


def parse_inputs():
    with open("./day_8.txt", "r") as f:
        return f.read().splitlines()


def solution_1(instructions):
    program_pointer = 0
    accumulator = 0

    visited = set()

    while True:
        if program_pointer in visited:
            return (False, accumulator)
        if program_pointer == len(instructions):
            return (True, accumulator)
        name, value = instructions[program_pointer].split()
        if name == "acc":
            accumulator += int(value)
            delta = 1
        elif name == "jmp":
            delta = int(value)
        else:
            delta = 1

        visited.add(program_pointer)
        program_pointer += delta


def solution_2():
    instructions = parse_inputs()

    program_pointer = 0
    accumulator = 0

    visited = set()
    tracker = []

    while True:
        if program_pointer in visited:
            break
        name, value = instructions[program_pointer].split()
        if name == "acc":
            accumulator += int(value)
            delta = 1
        elif name == "jmp":
            tracker.append((program_pointer, f"nop {value}"))
            delta = int(value)
        else:
            tracker.append((program_pointer, f"jmp {value}"))
            delta = 1
        visited.add(program_pointer)
        program_pointer += delta

    for idx, new in tracker:
        _instructions = instructions.copy()
        _instructions[idx] = new
        halted, value = solution_1(_instructions)
        if halted:
            return value


if __name__ == "__main__":
    print(solution_1(parse_inputs())[1])
    print(solution_2())
