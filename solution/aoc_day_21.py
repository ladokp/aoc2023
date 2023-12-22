# aoc_day_21.py
from collections import deque

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        lines = [list(line) for line in puzzle_input.split("\n")]
        start_row, start_column = 0, 0

        for row_index in range(len(lines)):
            for column_index in range(len(lines[0])):
                if lines[row_index][column_index] == "S":
                    start_row, start_column = row_index, column_index

        return lines, len(lines), len(lines[0]), start_row, start_column

    DAY = 21

    SOLVE = {}

    def find_d(self, row, column):
        grid, rows, columns, start_row, start_column = self.data
        set_ = {}
        queue = deque([(0, 0, start_row, start_column, 0)])
        while queue:
            t_row, t_column, row, column, d = queue.popleft()
            if row < 0:
                t_row -= 1
                row += rows
            if row >= rows:
                t_row += 1
                row -= rows
            if column < 0:
                t_column -= 1
                column += columns
            if column >= columns:
                t_column += 1
                column -= columns
            if not (
                0 <= row < rows and 0 <= column < columns and grid[row][column] != "#"
            ):
                continue
            if (t_row, t_column, row, column) in set_:
                continue
            if abs(t_row) > 4 or abs(t_column) > 4:
                continue
            set_[(t_row, t_column, row, column)] = d
            for delta_row, delta_column in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                queue.append(
                    (t_row, t_column, row + delta_row, column + delta_column, d + 1)
                )
        return set_

    def solve_(self, d, v, length):
        grid, rows, columns, _, _ = self.data
        amount = (length - d) // rows
        if (d, v, length) in self.SOLVE:
            return self.SOLVE[(d, v, length)]
        result = 0
        for x in range(1, amount + 1):
            if d + rows * x <= length and (d + rows * x) % 2 == (length % 2):
                result += (x + 1) if v == 2 else 1
        self.SOLVE[(d, v, length)] = result
        return result

    def solve21(self, part1, steps=6):
        grid, rows, columns, start_row, start_column = self.data
        set_ = self.find_d(start_row, start_column)
        length = steps
        answer = 0
        for row in range(rows):
            for column in range(columns):
                if (0, 0, row, column) in set_:
                    options = [-3, -2, -1, 0, 1, 2, 3]
                    for t_row in options:
                        for t_column in options:
                            if part1 and (t_row != 0 or t_column != 0):
                                continue
                            d = set_[(t_row, t_column, row, column)]
                            if d % 2 == length % 2 and d <= length:
                                answer += 1
                            if t_row in [min(options), max(options)] and t_column in [
                                min(options),
                                max(options),
                            ]:
                                answer += self.solve_(d, 2, length)
                            elif t_row in [min(options), max(options)] or t_column in [
                                min(options),
                                max(options),
                            ]:
                                answer += self.solve_(d, 1, length)
        return answer

    def part1(self, steps=64):
        """Solve part 1"""
        return self.solve21(True, steps)

    def part2(self, steps=26_501_365):
        """Solve part 2"""
        return self.solve21(False, steps)


if __name__ == "__main__":
    AocSolution().print_solution()
