# aoc_day_11.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return [list(row) for row in puzzle_input.split("\n")]

    DAY = 11

    def calculate_distances(self, *, part2):
        grid = self.data
        row_length = len(grid)
        column_length = len(grid[0])
        empty_row = []
        row = 0
        while row < row_length:
            empty = True
            for column in range(column_length):
                if grid[row][column] == "#":
                    empty = False
            if empty:
                empty_row.append(row)
            row += 1
        empty_column = []
        column = 0
        while column < column_length:
            empty = True
            for row in range(row_length):
                if grid[row][column] == "#":
                    empty = False
            if empty:
                empty_column.append(column)
            column += 1

        galaxies = []
        for row in range(row_length):
            for column in range(column_length):
                if grid[row][column] == "#":
                    galaxies.append((row, column))

        expansion_factor, result = 10**6 - 1 if part2 else 2 - 1, 0
        for index1, (row, column) in enumerate(galaxies):
            for index2 in range(index1, len(galaxies)):
                row2, column2 = galaxies[index2]
                distance_i_j = abs(row2 - row) + abs(column2 - column)
                for current in empty_row:
                    if min(row, row2) <= current <= max(row, row2):
                        distance_i_j += expansion_factor
                for ec in empty_column:
                    if min(column, column2) <= ec <= max(column, column2):
                        distance_i_j += expansion_factor
                result += distance_i_j
        return result

    def part1(self):
        """Solve part 1"""
        return self.calculate_distances(part2=False)

    def part2(self):
        """Solve part 2"""
        return self.calculate_distances(part2=True)


if __name__ == "__main__":
    AocSolution().print_solution()
