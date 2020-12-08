def parse_inputs():
    with open("./day_8.txt", "r") as f:
        return f.read().splitlines()


def solution_1():
    instructions = parse_inputs()

    program_pointer = 0
    accumulator = 0

    visited = set()

    while True:
        if program_pointer in visited:
            return accumulator
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


if __name__ == "__main__":
    print(solution_1())
