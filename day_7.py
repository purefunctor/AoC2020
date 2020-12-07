from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import ClassVar, Dict, List


def parse_inputs():
    with open("./day_7.txt", "r") as f:
        return f.read().splitlines()


class Bag:
    name: str
    rules: List[Rule]

    bags = {}

    def __new__(cls, name: str) -> Bag:
        if name not in cls.bags:
            self = super().__new__(cls)
            cls.bags[name] = self

            self.name = name
            self.rules = []

        else:
            self = cls.bags[name]
        return self

    def check_for(self, bag: Bag) -> bool:
        for rule in self.rules:
            if rule.bag == bag:
                return True
            if rule.check_for(bag):
                return True
        return False

    def add_rules(self, *rules: Rule) -> Bag:
        self.rules.extend(rules)
        return self

    def __eq__(self, other):
        return self.name == other.name and self.rules == other.rules

    def __repr__(self):
        return f"Bag(name={self.name}, rules={self.rules})"


@dataclass(eq=True)
class Rule:
    bag: Bag
    count: int

    def check_for(self, bag: Bag) -> bool:
        return self.bag.check_for(bag)


def solution_1():
    bag_name = re.compile(r"(\w+ \w+) bags contain")
    bag_rules = re.compile(r"(\d) (\w+ \w+)")

    bags = []
    for line in parse_inputs():
        rules = [Rule(Bag(name), int(count)) for count, name in bag_rules.findall(line)]
        bag = Bag(bag_name.match(line).group(1)).add_rules(*rules)
        bags.append(bag)

    return sum(bag.check_for(Bag("shiny gold")) for bag in bags)


if __name__ == "__main__":
    print(solution_1())
