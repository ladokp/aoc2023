# aoc_day_22.py
from queue import PriorityQueue

from solution.aoc_base import AocBaseClass


class Brick:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.floor = min(self.start[2], self.end[2])
        self.height = abs(self.start[2] - self.end[2])
        self.support = []
        self.supporting = []

    def __lt__(self, other):
        return self.floor < other.floor


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        bricks = PriorityQueue()
        lowest_level = None
        for line, row in [d.split("~") for d in puzzle_input.split("\n")]:
            brick = Brick(
                [int(v) for v in line.split(",")],
                [int(v) for v in row.split(",")],
            )
            bricks.put(brick)
            if lowest_level is None or lowest_level > brick.floor:
                lowest_level = brick.floor
        return self.solve_(bricks, lowest_level)

    DAY = 22

    @staticmethod
    def solve_(bricks, floor_level):
        stable_bricks = []
        while not bricks.empty():
            brick = bricks.get()
            if brick.floor == floor_level:
                stable_bricks.append(brick)
            else:
                support, support_level = [], 0
                for stable_brick in stable_bricks:
                    if (
                        stable_brick.start[0] <= brick.end[0]
                        and brick.start[0] <= stable_brick.end[0]
                        and stable_brick.start[1] <= brick.end[1]
                        and brick.start[1] <= stable_brick.end[1]
                    ):
                        stable_brick_top = sum(
                            (stable_brick.floor, stable_brick.height)
                        )
                        if stable_brick_top > support_level:
                            support, support_level = [], stable_brick_top
                        if stable_brick_top == support_level:
                            support.append(stable_brick)
                brick.support = support
                brick.floor = support_level + 1
                stable_bricks.append(brick)

                for supported_brick in support:
                    supported_brick.supporting.append(brick)

        counter_p1 = 0
        for stable_brick in stable_bricks:
            if len(stable_brick.supporting) > 0:
                if sum(
                    1
                    for supporting in stable_brick.supporting
                    if len(supporting.support) > 1
                ) == len(stable_brick.supporting):
                    counter_p1 += 1
            else:
                counter_p1 += 1

        counter_p2 = 0
        for stable_brick in stable_bricks:
            fall_stack = [
                supporting
                for supporting in stable_brick.supporting
                if len(supporting.support) == 1
            ]
            fallen = set()
            while len(fall_stack) > 0:
                falling_brick = fall_stack.pop(0)
                fallen.add(falling_brick)
                fall_stack.extend(
                    [
                        supporting
                        for supporting in falling_brick.supporting
                        if len(set(supporting.support).difference(fallen)) == 0
                    ]
                )
            counter_p2 += len(fallen)

        return counter_p1, counter_p2

    def part1(self):
        """Solve part 1"""
        part_1, _ = self.data
        return part_1

    def part2(self):
        """Solve part 2"""
        _, part_2 = self.data
        return part_2


if __name__ == "__main__":
    AocSolution().print_solution()
