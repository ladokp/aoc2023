# aoc_day_21.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return [list(line) for line in puzzle_input.split("\n")]

    DAY = 21

    @staticmethod
    def is_valid_pos(layout, pos):
        return all(
            (pos[0] >= 0, pos[0] < len(layout), pos[1] >= 0, pos[1] < len(layout[0]))
        )

    @staticmethod
    def get_starting_point(layout):
        for y, _ in enumerate(layout):
            for x, _ in enumerate(layout[0]):
                if layout[y][x] == "S":
                    return y, x

    def take_one_step(self, layout, position):
        new_start_position = set()
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_position = (position[0] + direction[0], position[1] + direction[1])
            if (
                self.is_valid_pos(layout, new_position)
                and layout[new_position[0]][new_position[1]] != "#"
            ):
                new_start_position.add(new_position)

        return new_start_position

    def solve_(self, num_steps):
        start_position = self.get_starting_point(self.data)

        curr_positions = {start_position}
        for _ in range(num_steps):
            next_positions = set()
            for pos in curr_positions:
                out = self.take_one_step(self.data, pos)
                next_positions = next_positions.union(out)

            curr_positions = next_positions

        return len(curr_positions)

    def part1(self, steps=64):
        """Solve part 1"""
        return self.solve_(steps)

    def part2(self):
        """Solve part 2"""


if __name__ == "__main__":
    AocSolution().print_solution()
