# aoc_day_08.py
from math import gcd

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        nodes = {}
        blocks = puzzle_input.split("\n\n")
        instructions = blocks[0]
        for line in blocks[1].split("\n"):
            nodes[line[:3]] = {"L": line[7:10], "R": line[12:15]}
        return instructions, nodes

    DAY = 8

    def count_steps(self, start_address="AAA", end_address="ZZZ"):
        def lcm(xs):
            ans = 1
            for x in xs:
                ans = (x * ans) // gcd(x, ans)
            return ans

        instructions, nodes = self.data
        instructions_length = len(instructions)
        nodes_list = []
        for node in nodes:
            if node.endswith(start_address):
                nodes_list.append(node)
        total_steps = {}
        steps = 0
        while True:
            next_nodes = []
            for index, current_node in enumerate(nodes_list):
                current_node = nodes[current_node][
                    instructions[steps % instructions_length]
                ]
                if current_node.endswith(end_address):
                    total_steps[index] = steps + 1
                    if len(total_steps) == len(nodes_list):
                        return lcm(total_steps.values())
                next_nodes.append(current_node)
            nodes_list = next_nodes
            steps += 1

    def part1(self):
        """Solve part 1"""
        return self.count_steps()

    def part2(self):
        """Solve part 2"""
        return self.count_steps("A", "Z")


if __name__ == "__main__":
    AocSolution().print_solution()
