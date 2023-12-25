# aoc_day_25.py
import itertools
from collections import defaultdict

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        adjacency_list = defaultdict(set)

        for line in puzzle_input.split("\n"):
            source, targets = line.split(": ")
            for target in targets.split():
                adjacency_list[source].add(target)
                adjacency_list[target].add(source)
        return adjacency_list

    def augment(self, node, remaining_flow, target, capacities, valid):
        if node == target:
            return remaining_flow
        used, neighbors = 0, valid[node]
        while neighbors and used < remaining_flow:
            neighbor = neighbors.pop()
            capacity = capacities[node][neighbor]
            flow = self.augment(
                neighbor,
                min(remaining_flow - used, capacity),
                target,
                capacities,
                valid,
            )
            used += flow
            capacities[node][neighbor] -= flow
            capacities[neighbor][node] += flow
            if 0 < flow < capacity:
                neighbors.append(neighbor)
        return used

    def dinics_max_flow(self, graph, source, target):
        assert source != target
        num_nodes = len(graph)
        residual_capacities = [defaultdict(int, adjacent) for adjacent in graph]

        max_flow = 0
        while True:
            valid_neighbors = [[] for _ in range(num_nodes)]
            node_levels = [-1] * num_nodes
            node_levels[source], bfs_queue = 0, [source]

            for current_node in bfs_queue:
                if current_node == target:
                    break
                for neighbor, capacity in residual_capacities[current_node].items():
                    if node_levels[neighbor] == -1 and capacity:
                        node_levels[neighbor] = node_levels[current_node] + 1
                        bfs_queue.append(neighbor)
                    if (
                        node_levels[current_node] + 1 == node_levels[neighbor]
                        and capacity
                    ):
                        valid_neighbors[current_node].append(neighbor)
            else:
                return max_flow, residual_capacities

            max_flow += self.augment(
                source,
                float("inf"),
                target,
                residual_capacities,
                valid_neighbors,
            )

    DAY = 25

    def part1(self):
        """Solve part 1"""
        result = 0
        adjacency_list = self.data

        all_nodes = set(adjacency_list)
        for neighbors in adjacency_list.values():
            all_nodes |= neighbors

        node_indices = {node: index for index, node in enumerate(all_nodes)}
        graph = [defaultdict(int) for _ in range(len(all_nodes))]
        for node, neighbors in adjacency_list.items():
            for neighbor in neighbors:
                graph[node_indices[node]][node_indices[neighbor]] = 1

        for node_a, node_b in itertools.combinations(all_nodes, 2):
            if node_a == node_b:
                continue

            flow, capacities = self.dinics_max_flow(
                graph, node_indices[node_a], node_indices[node_b]
            )
            if flow == 3:
                queue = [node_indices[node_a]]
                seen = set(queue)
                for node in queue:
                    for neighbor, capacity in capacities[node].items():
                        if capacity > 0 and neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)

                result = len(queue) * (len(all_nodes) - len(queue))
                break
        return result

    def part2(self):
        """Solve part 2"""


if __name__ == "__main__":
    AocSolution().print_solution()
