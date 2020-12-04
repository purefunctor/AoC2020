import re


def parse_input():
    with open("./day_4.txt", "r") as f:
        return [line.replace("\n", " ") for line in f.read().split("\n\n")]


def solution_1():
    pattern = re.compile("(byr|iyr|eyr|hgt|hcl|ecl|pid|cid)+")

    valid = 0
    for line in parse_input():
        fields = pattern.findall(line)
        delta = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}.difference(set(fields))
        if len(delta.difference(["cid"])) == 0:
            valid += 1

    return valid


def solution_2():
    valid = 0
    for line in parse_input():
        field = re.search(r"byr:(\d{1,4})", line)
        if not (field and 1920 <= int(field[1]) <= 2002):
            continue
        field = re.search(r"iyr:(\d{1,4})", line)
        if not (field and 2010 <= int(field[1]) <= 2020):
            continue
        field = re.search(r"eyr:(\d{1,4})", line)
        if not (field and 2020 <= int(field[1]) <= 2030):
            continue
        field = re.search(r"hgt:(\d+)(cm|in)", line)
        if not (field and ((field[2] == "cm" and 150 <= int(field[1]) <= 193) or (field[2] == "in" and 59 <= int(field[1]) <= 76))):
            continue
        field = re.search(r"hcl:#[0-9a-f]{6}", line)
        if not field:
            continue
        field = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", line)
        if not field:
            continue
        field = re.search(r"pid:[0-9]{9}\b", line)
        if not field:
            continue
        valid += 1
    return valid


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
