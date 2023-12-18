# aoc_day_17.py
from shapely.geometry import Polygon

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return puzzle_input.split("\n")

    DAY = 18

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    def part1(self):
        """Solve part 1"""
        coords = [(0, 0)]
        for line in self.data:
            direction, distance, _ = line.split()
            coords.append(
                (
                    coords[-1][0] + int(distance) * self.directions[direction][0],
                    coords[-1][1] + int(distance) * self.directions[direction][1],
                )
            )
        bounds = sum(
            abs(x2 - x1) + abs(y2 - y1)
            for (x1, y1), (x2, y2) in zip(coords[:-1], coords[1:])
        )
        return int(Polygon(coords).area - bounds / 2 + 1 + bounds)

    def part2(self):
        """Solve part 2"""
        coordinates = [(0, 0)]
        for line in self.data:
            _, _, paint = line.split()
            distance = int(paint[2:7], 16)
            direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[paint[7]]
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


if __name__ == "__main__":
    AocSolution().print_solution()
