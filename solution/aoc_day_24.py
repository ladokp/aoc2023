# aoc_day_24.py
import itertools
import re
from z3 import z3

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        hailstones = []
        for line in puzzle_input.split("\n"):
            match = re.search(
                r"^(-?\d+),"
                r"\s*(-?\d+),"
                r"\s*(-?\d+)"
                r"\s*@"
                r"\s*(-?\d+),"
                r"\s*(-?\d+),"
                r"\s*(-?\d+)$",
                line,
            )
            px, py, pz, vx, vy, vz = map(int, match.groups())
            hailstones.append(((px, py, pz), (vx, vy, vz)))
        return hailstones

    DAY = 24

    @staticmethod
    def calculate_2d_intersection_point(position1, velocity1, position2, velocity2):
        slope1 = velocity1[1] / velocity1[0]
        intercept1 = -slope1 * position1[0] + position1[1]
        slope2 = velocity2[1] / velocity2[0]
        intercept2 = -slope2 * position2[0] + position2[1]

        try:
            x_intersection = (intercept2 - intercept1) / (slope1 - slope2)
        except ZeroDivisionError:
            return None

        y_intersection = slope1 * x_intersection + intercept1
        time1 = (x_intersection - position1[0]) / velocity1[0]
        time2 = (x_intersection - position2[0]) / velocity2[0]

        if time1 < 0 or time2 < 0:
            return None

        return x_intersection, y_intersection

    def part1(self, is_test=False):
        """Solve part 1"""
        test_area = (7, 27) if is_test else (2 * 1e14, 4 * 1e14)
        intersections = 0
        for (pos1, vel1), (pos2, vel2) in itertools.combinations(self.data, 2):
            intersection_point = self.calculate_2d_intersection_point(
                pos1, vel1, pos2, vel2
            )
            if intersection_point and all(
                test_area[0] <= p <= test_area[1] for p in intersection_point
            ):
                intersections += 1
        return intersections

    def part2(self):
        """Solve part 2"""
        initial_data = self.data[:3]
        time_variable = z3.IntVector("time", len(initial_data))
        position_variable = z3.IntVector("position", 3)
        velocity_variable = z3.IntVector("velocity", 3)
        solver = z3.Solver()
        for time_index, (initial_position, initial_velocity) in zip(
            time_variable, initial_data
        ):
            for pos_var, vel_var, pos, vel in zip(
                position_variable, velocity_variable, initial_position, initial_velocity
            ):
                solver.add(pos_var + vel_var * time_index == pos + vel * time_index)
        if solver.check() == z3.sat:
            model = solver.model()
            return sum(model[pos_var].as_long() for pos_var in position_variable)


if __name__ == "__main__":
    AocSolution().print_solution()
