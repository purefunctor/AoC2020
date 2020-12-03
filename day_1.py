def parse_inputs():
    with open("./day_1.txt", "r") as f:
        return set(map(int, f.readlines()))


def solution_1(expenses):
    for expense in expenses:
        delta = 2020 - expense
        if delta in expenses:
            return expense * delta


def solution_2(expenses):
    for expense in expenses:
        for expense_two in expenses:
            delta = 2020 - expense - expense_two
            if delta in expenses:
                return expense * delta * expense_two


if __name__ == "__main__":
    print(solution_1(parse_inputs()))
    print(solution_2(parse_inputs()))
