# aoc_day_19.py
import math
from collections import defaultdict
import re

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        first_block, second_block = puzzle_input.split("\n\n")
        workflows = defaultdict(list)

        for line in first_block.split("\n"):
            name, remaining = line[:-1].split("{")
            rules = remaining.split(",")
            for rule in rules:
                if ":" in rule:
                    workflows[name].append(tuple(rule.split(":")))
                else:
                    workflows[name].append((None, rule))

        return dict(workflows), second_block.split("\n")

    DAY = 19

    @staticmethod
    def process_workflow(wf, x, m, a, s):
        key_ = "in"
        index = 0

        while key_ not in {"A", "R"}:
            rule, next_ = wf[key_][index]

            if rule is None:
                key_, index = next_, 0
                continue

            result = eval(rule)

            if result:
                key_, index = next_, 0
            else:
                index += 1

        return x + m + a + s if key_ == "A" else 0

    def process_workflow_2(self, _key, wf, ranges):
        if _key == "R":
            return 0

        if _key == "A":
            return math.prod(upper - lower + 1 for lower, upper in ranges.values())

        total = 0
        for rule, _next in wf[_key]:
            temp_ranges = ranges.copy()

            if rule is None:
                total += self.process_workflow_2(_next, wf, ranges)
            else:
                key_, operator, value = rule[0], rule[1], int(rule[2:])

                if (
                    operator == ">"
                    and ranges[key_] is not None
                    and value < ranges[key_][1]
                ):
                    temp_ranges[key_] = (
                        max(value + 1, ranges[key_][0]),
                        ranges[key_][1],
                    )
                    total += self.process_workflow_2(_next, wf, temp_ranges)
                    ranges[key_] = (
                        (ranges[key_][0], value) if ranges[key_][0] <= value else None
                    )

                elif (
                    operator == "<"
                    and ranges[key_] is not None
                    and value > ranges[key_][0]
                ):
                    temp_ranges[key_] = (
                        ranges[key_][0],
                        min(value - 1, ranges[key_][1]),
                    )
                    total += self.process_workflow_2(_next, wf, temp_ranges)
                    ranges[key_] = (
                        (value, ranges[key_][1]) if value <= ranges[key_][1] else None
                    )

        return total

    def part1(self):
        """Solve part 1"""
        workflow, part_ratings = self.data
        result = 0

        for part in part_ratings:
            result += self.process_workflow(
                workflow, *(int(x) for x in re.findall(r"\d+", part))
            )

        return result

    def part2(self):
        """Solve part 2"""
        return self.process_workflow_2(
            "in",
            self.data[0],
            {
                "x": (1, 4000),
                "m": (1, 4000),
                "a": (1, 4000),
                "s": (1, 4000),
            },
        )


if __name__ == "__main__":
    AocSolution().print_solution()
