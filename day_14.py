import itertools
import re


def parse_inputs():
    with open("./day_14.txt", "r") as f:
        lines = f.read().replace("mask", "\nmask").split("\n\n")
        return [line.strip().split("\n") for line in lines]


def solution_1():
    mask_re = re.compile("mask = ([01X]+)")
    inst_re = re.compile(r"mem\[(\d+)\] = (\d+)")

    addresses = {}
    for mask_, *instructions_ in parse_inputs():
        mask = mask_re.match(mask_)[1]
        instructions = [inst_re.match(instruction).groups() for instruction in instructions_]

        for address, bits in instructions:
            unpadded = list(bin(int(bits)))[2:]
            bit_str= ["0" for _ in range(len(mask) - len(unpadded))] + unpadded
            masked = "".join(
                b if m == "X" else m
                for m, b in zip(mask, bit_str)
            )

            addresses[address] = int(masked, 2)

    return sum(addresses.values())


def calculate_floating(floating):
    l = floating.count("X")
    for f in itertools.product("01", repeat=l):
        yield floating.replace("X", "{}").format(*f)


def solution_2():
    mask_re = re.compile("mask = ([01X]+)")
    inst_re = re.compile(r"mem\[(\d+)\] = (\d+)")

    addresses = {}
    for mask_, *instructions_ in parse_inputs():
        mask = mask_re.match(mask_)[1]
        instructions = [inst_re.match(instruction).groups() for instruction in instructions_]

        for address, bits in instructions:
            unpadded = list(bin(int(address)))[2:]
            bit_str= ["0" for _ in range(len(mask) - len(unpadded))] + unpadded
            floating = "".join(
                b if m == "0" else
                m if m == "1" else
                "X"
                for m, b in zip(mask, bit_str)
            )

            for filled in calculate_floating(floating):
                addresses[int(filled, 2)] = int(bits)

    return sum(addresses.values())


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
