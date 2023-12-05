# aoc_day_05.py
import re
from functools import reduce

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        entries = puzzle_input.split("\n\n")
        maps, seeds = [], tuple(map(int, re.findall(r"\d+", entries[0])))
        for block in entries[1:]:
            map_ = []
            for line in block.split("\n")[1:]:
                destination_range_start, source_range_start, range_length = map(
                    int, re.findall(r"\d+", line)
                )
                map_.append(
                    (
                        source_range_start,
                        source_range_start + range_length,
                        destination_range_start - source_range_start,
                    )
                )
            maps.append(tuple(sorted(map_)))
        return tuple(maps), seeds

    DAY = 5

    @staticmethod
    def lookup(seed, map_):
        for b, e, d in map_:
            if seed > e:
                continue
            if seed < b:
                return seed
            return seed + d
        return seed

    @staticmethod
    def lookup2(seed, target, map_):
        result = []
        for b, e, d in map_:
            if seed > e or target < b:
                continue
            if seed < b:
                result += [(seed, b - 1), (b + d, min(e, target) + d)]
            else:
                result += [(seed + d, min(e, target) + d)]
            if e > target:
                return result
            seed = e
        if not result:
            result = [(seed, target)]
        return result

    def part1(self):
        """Solve part 1"""
        maps, seeds = self.data
        return min(reduce(self.lookup, maps, seed) for seed in seeds)

    def part2(self):
        """Solve part 2"""

        def process2(seeds_):
            result, return_list = [], [(seeds_[0], sum(seeds_))]
            for map_ in self.data[0]:
                for seed, target in return_list:
                    result += self.lookup2(seed, target, map_)
                return_list = result
                result = []
            return min(return_list)[0]

        seeds = self.data[1]
        return min(
            process2((seeds[index : index + 2])) for index in range(0, len(seeds), 2)
        )


if __name__ == "__main__":
    AocSolution().print_solution()
