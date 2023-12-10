# aoc_day_10.py
from __future__ import annotations

from solution.aoc_base import AocBaseClass

EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)
PIPE_DIRECTIONS = {
    "|": (NORTH, SOUTH),  # | is a vertical pipe connecting north and south.
    "-": (EAST, WEST),  # - is a horizontal pipe connecting east and west.
    "L": (NORTH, EAST),  # L is a 90-degree bend connecting north and east.
    "J": (NORTH, WEST),  # J is a 90-degree bend connecting north and west.
    "7": (SOUTH, WEST),  # 7 is a 90-degree bend connecting south and west.
    "F": (SOUTH, EAST),  # F is a 90-degree bend connecting south and east.
    ".": (),  # . is ground; there is no pipe in this tile.
    "S": (NORTH, EAST, WEST, SOUTH),
}


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return puzzle_input.split("\n")

    DAY = 10

    def get_elem(self, x, y):
        lines = self.data
        if x in range(len(lines)):
            if y in range(len(lines[0])):
                return lines[x][y]
        return "."

    def get_loop(self):
        lines = self.data
        conn = []
        for i in lines:
            conn.append([])
            for _ in i:
                conn[-1].append(set())
        for x, _ in enumerate(lines):
            for y, _ in enumerate(lines[0]):
                for dx, dy in PIPE_DIRECTIONS[lines[x][y]]:
                    if (-dx, -dy) in PIPE_DIRECTIONS[self.get_elem(x + dx, y + dy)]:
                        conn[x][y].add((dx, dy))
        start = None
        for x, _ in enumerate(lines):
            for y, _ in enumerate(lines[0]):
                if lines[x][y] == "S":
                    start = (x, y)
        loop = [start]
        prev = None
        while True:
            x, y = loop[-1]
            dx, dy = next(filter(lambda x: x != prev, conn[x][y]))
            prev = (-dx, -dy)
            cur = (x + dx, y + dy)
            loop.append(cur)
            if cur == start:
                break
        return conn, loop

    def part1(self):
        """Solve part 1"""
        s = 0
        _, loop = self.get_loop()
        if len(loop) % 2 == 1:
            s = (len(loop) - 1) // 2
        return s

    def part2(self):
        """Solve part 2"""
        s = 0
        conn, loop = self.get_loop()
        for x in range(len(self.data)):
            in_loop = False
            enter = 0
            for y in range(len(self.data[0])):
                if (x, y) in loop:
                    if enter == 0:
                        if EAST in conn[x][y]:
                            if NORTH in conn[x][y]:
                                enter = -1
                            elif SOUTH in conn[x][y]:
                                enter = 1
                        else:
                            in_loop = not in_loop
                    else:
                        if EAST in conn[x][y]:
                            pass
                        elif SOUTH in conn[x][y]:
                            if enter == -1:
                                in_loop = not in_loop
                            enter = 0
                        elif NORTH in conn[x][y]:
                            if enter == 1:
                                in_loop = not in_loop
                            enter = 0
                else:
                    if in_loop:
                        s += 1
        return s


if __name__ == "__main__":
    AocSolution().print_solution()
