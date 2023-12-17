# aoc_day_17.py
import heapq

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return [list(line) for line in puzzle_input.split("\n")]

    DAY = 17

    def find_min_path(self, part2=False):
        grid = self.data
        rows, columns = len(grid), len(grid[0])
        current = [(0, 0, 0, -1, -1)]
        cache = {}
        while current:
            dist, row, column, direction, in_direction = heapq.heappop(current)
            if (row, column, direction, in_direction) in cache:
                continue
            cache[(row, column, direction, in_direction)] = dist
            for index, (delta_row, delta_column) in enumerate(
                ([-1, 0], [0, 1], [1, 0], [0, -1])
            ):
                new_row = row + delta_row
                new_column = column + delta_column
                new_direction = index
                new_in_direction = 1 if new_direction != direction else in_direction + 1

                is_not_reverse = (new_direction + 2) % 4 != direction

                isvalid_part1 = new_in_direction <= 3
                isvalid_part2 = new_in_direction <= 10 and (
                    new_direction == direction
                    or in_direction >= 4
                    or in_direction == -1
                )
                is_valid = isvalid_part2 if part2 else isvalid_part1

                if (
                    0 <= new_row < rows
                    and 0 <= new_column < columns
                    and is_not_reverse
                    and is_valid
                ):
                    heapq.heappush(
                        current,
                        (
                            dist + int(grid[new_row][new_column]),
                            new_row,
                            new_column,
                            new_direction,
                            new_in_direction,
                        ),
                    )

        return min(
            value
            for (row, column, direction, in_direction), value in cache.items()
            if row == rows - 1 and column == columns - 1
        )

    def part1(self):
        """Solve part 1"""
        return self.find_min_path()

    def part2(self):
        """Solve part 2"""
        return self.find_min_path(True)


if __name__ == "__main__":
    AocSolution().print_solution()
