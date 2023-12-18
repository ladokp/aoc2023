# aoc_day_18.py
from types import MappingProxyType
from shapely.geometry import Polygon

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        split_lines = (line.split() for line in puzzle_input.split("\n"))
        return tuple(
            (
                direction,
                int(distance),
                tuple(self.directions.items())[int(paint[7])][0],
                int(paint[2:7], 16),
            )
            for direction, distance, paint in split_lines
        )

    DAY = 18

    directions = MappingProxyType(
        {
            "R": (1, 0),
            "D": (0, -1),
            "L": (-1, 0),
            "U": (0, 1),
        }
    )

    def solve_(self, *, part2=False):
        coordinates = [(0, 0)]
        for parameters in self.data:
            direction, distance = parameters[2:] if part2 else parameters[:2]
            coordinates.append(
                (
                    coordinates[-1][0] + distance * self.directions[direction][0],
                    coordinates[-1][1] + distance * self.directions[direction][1],
                )
            )
        bounds = sum(
            abs(x2 - x1) + abs(y2 - y1)
            for (x1, y1), (x2, y2) in zip(coordinates[:-1], coordinates[1:])
        )
        return int(Polygon(coordinates).area - bounds / 2 + 1 + bounds)

    def part1(self):
        """Solve part 1"""
        return self.solve_()

    def part2(self):
        """Solve part 2"""
        return self.solve_(part2=True)


if __name__ == "__main__":
    AocSolution().print_solution()
