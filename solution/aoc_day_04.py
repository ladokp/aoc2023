# aoc_day_04.py
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        data = puzzle_input.split("\n")
        part1, copies = 0, [0 for _ in data]
        for index, card in enumerate(data):
            winning, own_numbers = (
                part.split(" ") for part in card.split(": ")[1].split(" | ")
            )
            if count := sum(
                number.isdigit() and number in winning for number in own_numbers
            ):
                part1 += 1 << (count - 1)
                if index != len(data) - 1:
                    while count > 0:
                        for copy_index in range(index + 1, len(data)):
                            copies[copy_index] += 1 + copies[index]
                            if not (count := count - 1):
                                break

        return part1, sum(copies) + len(data)

    DAY = 4

    def part1(self):
        """Solve part 1"""
        return self.data[0]

    def part2(self):
        """Solve part 2"""
        return self.data[1]


if __name__ == "__main__":
    AocSolution().print_solution()
