import re


def parse_input():
    with open("./day_4.txt", "r") as f:
        return [line.replace("\n", " ") for line in f.read().split("\n\n")]


def solution_1():
    pattern = re.compile("(byr|iyr|eyr|hgt|hcl|ecl|pid|cid)+")

    valid = 0
    for line in parse_input():
        print(line)
        fields = pattern.findall(line)
        delta = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}.difference(set(fields))
        if len(delta.difference(["cid"])) == 0:
            valid += 1

    return valid

if __name__ == "__main__":
    print(solution_1())
