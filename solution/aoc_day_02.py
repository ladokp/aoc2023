# aoc_day_02.py
from collections import defaultdict
from functools import reduce

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        part_1, part_2 = 0, 0
        condition_dict = {"red": 12, "green": 13, "blue": 14}
        for line in puzzle_input.split("\n"):
            game_set_dict = defaultdict(int)
            ok = True
            id_, line = line.split(":")
            for game_set in line.split(";"):
                for balls in game_set.split(","):
                    count_, color = balls.split()
                    count_ = int(count_)
                    game_set_dict[color] = max(game_set_dict[color], count_)
                    if int(count_) > condition_dict.get(color, 0):
                        ok = False
            part_1 += int(id_.split()[-1]) if ok else 0
            part_2 += reduce(lambda x, y: x * y, game_set_dict.values())
        return part_1, part_2

    DAY = 2

    def part1(self):
        """Solve part 1"""
        return self.data[0]

    def part2(self):
        """Solve part 2"""
        return self.data[1]


if __name__ == "__main__":
    AocSolution().print_solution()
