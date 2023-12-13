# aoc_day_13.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return [
            list(row)
            for row in (line.split("\n") for line in puzzle_input.split("\n\n"))
        ]

    DAY = 13

    def find_reflection_score(self, part2=False):
        result = 0
        for grid in self.data:
            rows, columns = len(grid), len(grid[0])
            for column_index in range(columns - 1):
                badness = 0
                for column_index_2, _ in enumerate(grid[0]):
                    left = column_index - column_index_2
                    right = column_index + 1 + column_index_2
                    if 0 <= left < right < columns:
                        for row_index in range(rows):
                            increase_badness = (
                                grid[row_index][left] != grid[row_index][right]
                            )
                            badness += 1 if increase_badness else 0
                if badness == (1 if part2 else 0):
                    result += column_index + 1
            for row_index in range(rows - 1):
                badness = 0
                for row_index_2, _ in enumerate(grid):
                    down = row_index + 1 + row_index_2
                    up = row_index - row_index_2
                    if 0 <= up < down < rows:
                        for column_index in range(columns):
                            increase_badness = (
                                grid[up][column_index] != grid[down][column_index]
                            )
                            badness += 1 if increase_badness else 0
                if badness == (1 if part2 else 0):
                    result += 100 * (row_index + 1)
        return result

    def part1(self):
        """Solve part 1"""
        return self.find_reflection_score()

    def part2(self):
        """Solve part 2"""
        return self.find_reflection_score(True)


if __name__ == "__main__":
    AocSolution().print_solution()
