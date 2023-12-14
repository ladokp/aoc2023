# aoc_day_14.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        data = list(list(x) for x in puzzle_input.split("\n"))
        return data, len(data), len(data[0])

    DAY = 14

    @staticmethod
    def spin_north(data, m, n):
        new_data = [["."] * n for _ in range(m)]
        for j in range(n):
            to_place = 0
            for i in range(m):
                if data[i][j] == "#":
                    new_data[i][j] = "#"
                    to_place = i + 1
                elif data[i][j] == "O":
                    new_data[to_place][j] = "O"
                    to_place += 1
        return new_data

    @staticmethod
    def spin_west(data, m, n):
        new_data = [["."] * n for _ in range(m)]
        for i in range(m):
            to_place = 0
            for j in range(n):
                if data[i][j] == "#":
                    new_data[i][j] = "#"
                    to_place = j + 1
                elif data[i][j] == "O":
                    new_data[i][to_place] = "O"
                    to_place += 1
        return new_data

    @staticmethod
    def spin_south(data, m, n):
        new_data = [["."] * n for _ in range(m)]
        for j in range(n):
            to_place = m - 1
            for i in reversed(range(m)):
                if data[i][j] == "#":
                    new_data[i][j] = "#"
                    to_place = i - 1
                elif data[i][j] == "O":
                    new_data[to_place][j] = "O"
                    to_place -= 1
        return new_data

    @staticmethod
    def spin_east(data, m, n):
        new_data = [["."] * n for _ in range(m)]
        for i in range(m):
            to_place = n - 1
            for j in reversed(range(n)):
                if data[i][j] == "#":
                    new_data[i][j] = "#"
                    to_place = j - 1
                elif data[i][j] == "O":
                    new_data[i][to_place] = "O"
                    to_place -= 1
        return new_data

    def part1(self):
        """Solve part 1"""
        data, m, n = self.data
        new_data = self.spin_north(data, m, n)
        return sum((m - i) for i in range(m) for j in range(n) if new_data[i][j] == "O")

    def part2(self):
        """Solve part 2"""
        data, m, n = self.data
        times, new_data, recurring = 10**9, data[:], {}
        for x in range(times):
            new_data = self.spin_north(new_data, m, n)
            new_data = self.spin_west(new_data, m, n)
            new_data = self.spin_south(new_data, m, n)
            new_data = self.spin_east(new_data, m, n)

            tuple_ = tuple(tuple(x) for x in new_data)
            if tuple_ in recurring:
                diff = x - recurring[tuple_]
                times = (times - x) % diff - 1
                break
            recurring[tuple_] = x

        for x in range(times):
            new_data = self.spin_north(new_data, m, n)
            new_data = self.spin_west(new_data, m, n)
            new_data = self.spin_south(new_data, m, n)
            new_data = self.spin_east(new_data, m, n)

        return sum((m - i) for i in range(m) for j in range(n) if new_data[i][j] == "O")


if __name__ == "__main__":
    AocSolution().print_solution()
