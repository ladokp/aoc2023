# aoc_day_01.py
import re

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        p1 = []
        p2 = []
        for line in puzzle_input.split("\n"):
            p1_digits = []
            p2_digits = []
            for index, character in enumerate(line):
                if character.isdigit():
                    p1_digits.append(character)
                    p2_digits.append(character)
                for digit, value in enumerate(
                    (
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                    )
                ):
                    if line[index:].startswith(value):
                        p2_digits.append(str(digit + 1))
            p1.append(int(p1_digits[0] + p1_digits[-1]))
            p2.append(int(p2_digits[0] + p2_digits[-1]))
        return p1, p2

    DAY = 1

    def part1(self):
        """Solve part 1"""
        return sum(self.data[0])

    def part2(self):
        """Solve part 2"""
        return sum(self.data[1])


if __name__ == "__main__":
    AocSolution().print_solution()
