# aoc_day_23.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return puzzle_input.split("\n")

    DAY = 23

    @staticmethod
    def find_longest_hike(edges, rows, cols, part1=True):
        queue = [(0, 1, 0)]
        visited = set()
        longest_hike = 0

        while queue:
            current_row, current_col, distance = queue.pop()

            if distance == -1:
                visited.remove((current_row, current_col))
                continue

            if (current_row, current_col) == (rows - 1, cols - 2):
                longest_hike = max(longest_hike, distance)
                continue

            if (current_row, current_col) in visited:
                continue

            visited.add((current_row, current_col))
            queue.append((current_row, current_col, -1))

            if part1:
                for adjacent_row, adjacent_col in edges[(current_row, current_col)]:
                    queue.append((adjacent_row, adjacent_col, distance + 1))
            else:
                for adjacent_row, adjacent_col, length in edges[
                    (current_row, current_col)
                ]:
                    queue.append((adjacent_row, adjacent_col, distance + length))

        return longest_hike

    def part1(self):
        """Solve part 1"""
        edges = {}
        for row, line in enumerate(self.data):
            for col, value in enumerate(line):
                if value == ".":
                    for d_row, d_col in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                        adjacent_row, adjacent_col = row + d_row, col + d_col
                        if not (
                            0 <= adjacent_row < len(self.data)
                            and 0 <= adjacent_col < len(line)
                        ):
                            continue
                        if self.data[adjacent_row][adjacent_col] == ".":
                            edges.setdefault((row, col), set()).add(
                                (adjacent_row, adjacent_col)
                            )
                            edges.setdefault((adjacent_row, adjacent_col), set()).add(
                                (row, col)
                            )
                if value == ">":
                    edges.setdefault((row, col), set()).add((row, col + 1))
                    edges.setdefault((row, col - 1), set()).add((row, col))
                if value == "v":
                    edges.setdefault((row, col), set()).add((row + 1, col))
                    edges.setdefault((row - 1, col), set()).add((row, col))

        return self.find_longest_hike(edges, len(self.data), len(self.data[0]))

    def part2(self):
        """Solve part 2"""
        data = self.data
        edges = {}

        for row, line in enumerate(data):
            for col, value in enumerate(line):
                if value in ".>v":
                    for d_row, d_col in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                        adjacent_row, adjacent_col = row + d_row, col + d_col
                        if not (
                            0 <= adjacent_row < len(data)
                            and 0 <= adjacent_col < len(line)
                        ):
                            continue
                        if data[adjacent_row][adjacent_col] in ".>v":
                            edges.setdefault((row, col), set()).add(
                                (adjacent_row, adjacent_col, 1)
                            )
                            edges.setdefault((adjacent_row, adjacent_col), set()).add(
                                (row, col, 1)
                            )

        while True:
            for node, edge_set in edges.items():
                if len(edge_set) == 2:
                    edge_a, edge_b = edge_set
                    edges[edge_a[:2]].remove(node + (edge_a[2],))
                    edges[edge_b[:2]].remove(node + (edge_b[2],))
                    edges[edge_a[:2]].add((edge_b[0], edge_b[1], edge_a[2] + edge_b[2]))
                    edges[edge_b[:2]].add((edge_a[0], edge_a[1], edge_a[2] + edge_b[2]))
                    del edges[node]
                    break
            else:
                break

        return self.find_longest_hike(edges, len(self.data), len(self.data[0]), False)


if __name__ == "__main__":
    AocSolution().print_solution()
