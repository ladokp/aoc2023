# aoc_day_06.py - v2 idea from: gahjelle
import math
import re

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        list_1, list_2 = [], []
        for line in puzzle_input.split("\n"):
            numbers = re.findall(r"\d+", line)
            list_1.append(tuple(map(int, numbers)))
            list_2.append(numbers)
        return tuple(zip(*list_1)), (
            int("".join(number for number in list_2[0])),
            int("".join(number for number in list_2[1])),
        )

    DAY = 6

    @staticmethod
    def ways_to_beat_record(time, distance):
        hold_time = 0
        for hold_time in range(distance // time, time):
            if hold_time * (time - hold_time) > distance:
                break
        return (time + 1) - 2 * hold_time

    def part1(self):
        """Solve part 1"""
        return math.prod(
            self.ways_to_beat_record(time, distance) for time, distance in self.data[0]
        )

    def part2(self):
        """Solve part 2"""
        time, distance = self.data[1]
        return self.ways_to_beat_record(time, distance)


if __name__ == "__main__":
    AocSolution().print_solution()
