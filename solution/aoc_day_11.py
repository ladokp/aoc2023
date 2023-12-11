# aoc_day_11.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return [list(row) for row in puzzle_input.split("\n")]

    DAY = 11

    def calculate_distances(self, *, part2):
        grid = self.data
        expansion_factor, result = 1e6 - 1 if part2 else 1, 0
        empty_row, row, empty_column, column = [], 0, [], 0
        galaxies = []
        for row, columns in enumerate(grid):
            if all(value == "." for value in columns):
                empty_row.append(row)
        for column, _ in enumerate(grid[0]):
            empty = True
            for row, _ in enumerate(grid):
                if grid[row][column] == "#":
                    galaxies.append((row, column))
                    empty = False
            if empty:
                empty_column.append(column)

        for index1, (row1, column1) in enumerate(galaxies):
            for index2 in range(index1, len(galaxies)):
                row2, column2 = galaxies[index2]
                distance = abs(row2 - row1) + abs(column2 - column1)
                for current in empty_row:
                    if min(row1, row2) <= current <= max(row1, row2):
                        distance += expansion_factor
                for ec in empty_column:
                    if min(column1, column2) <= ec <= max(column1, column2):
                        distance += expansion_factor
                result += distance
        return result

    def part1(self):
        """Solve part 1"""
        return self.calculate_distances(part2=False)

    def part2(self):
        """Solve part 2"""
        return self.calculate_distances(part2=True)


if __name__ == "__main__":
    AocSolution().print_solution()
