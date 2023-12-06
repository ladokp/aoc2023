# aoc_day_06.py
import re

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        lists = []
        for line in puzzle_input.split("\n"):
            lists.append(list(map(int, re.findall(r"\d+", line))))
        return lists

    DAY = 6

    @staticmethod
    def ways_to_beat_record(time, distance):
        ways = 0
        for hold_time in range(time):
            boat_speed = hold_time
            travel_time = time - hold_time
            total_distance = boat_speed * travel_time
            if total_distance > distance:
                ways += 1
        return ways

    @staticmethod
    def multiply_ways(records):
        result = 1
        for record in records:
            result *= record
        return result

    def calculate_winning_ways(self, times, distances):
        ways_records = [
            self.ways_to_beat_record(t, d) for t, d in zip(times, distances)
        ]
        result = 1
        for record in ways_records:
            result *= record
        return result

    def part1(self):
        """Solve part 1"""
        return self.calculate_winning_ways(*self.data)

    def part2(self):
        """Solve part 2"""
        times, distances = [str(number) for number in self.data[0]], [
            str(number) for number in self.data[1]
        ]
        times, distances = [int("".join(times))], [int("".join(distances))]
        return self.calculate_winning_ways(times, distances)


if __name__ == "__main__":
    AocSolution().print_solution()
