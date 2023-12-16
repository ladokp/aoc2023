# aoc_day_16.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return [list(line) for line in puzzle_input.split("\n")]

    DAY = 16

    @staticmethod
    def one_laser_step(grid, row, column, delta_row, delta_column):
        cell = grid[row][column]
        if cell == "\\":
            delta_row, delta_column = delta_column, delta_row
        elif cell == "/":
            delta_row, delta_column = -delta_column, -delta_row
        elif cell == "|":
            if delta_column != 0:
                return [(row - 1, column, -1, 0), (row + 1, column, 1, 0)]
        elif cell == "-":
            if delta_row != 0:
                return [(row, column - 1, 0, -1), (row, column + 1, 0, 1)]
        return [(row + delta_row, column + delta_column, delta_row, delta_column)]

    def evaluate(self, grid, start):
        lasers, seen, heated = [start], set(), set()
        while len(lasers) > 0:
            row, column, delta_row, delta_column = lasers.pop()
            if (
                not (0 <= row < len(grid) and 0 <= column < len(grid[row]))
                or (row, column, delta_row, delta_column) in seen
            ):
                continue
            seen.add((row, column, delta_row, delta_column))
            heated.add((row, column))
            lasers.extend(
                self.one_laser_step(grid, row, column, delta_row, delta_column)
            )
        return heated

    def part1(self):
        """Solve part 1"""
        heated = self.evaluate(self.data, (0, 0, 0, 1))
        return len(heated)

    def part2(self):
        """Solve part 2"""
        grid = self.data
        possible_starts = [
            *((row, 0, 0, 1) for row in range(len(grid))),
            *((row, len(grid[row]) - 1, 0, -1) for row in range(len(grid))),
            *((0, column, 1, 0) for column in range(len(grid[0]))),
            *((len(grid) - 1, column, -1, 0) for column in range(len(grid[-1]))),
        ]

        return max(len(self.evaluate(grid, start)) for start in possible_starts)


if __name__ == "__main__":
    AocSolution().print_solution()
