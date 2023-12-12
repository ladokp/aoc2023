# aoc_day_12.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return puzzle_input.split("\n")

    DAY = 12
    SCORES = {}

    def expand(self, dots, blocks, index, block_index, current):
        score = 0
        if (key := (index, block_index, current)) in self.SCORES:
            return self.SCORES[key]
        if index == len(dots):
            if block_index == len(blocks) and current == 0:
                return 1
            if block_index == len(blocks) - 1 and blocks[block_index] == current:
                return 1
            return 0
        for character in [".", "#"]:
            if dots[index] == character or dots[index] == "?":
                if character == "." and current == 0:
                    score += self.expand(dots, blocks, index + 1, block_index, 0)
                elif (
                    character == "."
                    and current > 0
                    and block_index < len(blocks)
                    and blocks[block_index] == current
                ):
                    score += self.expand(dots, blocks, index + 1, block_index + 1, 0)
                elif character == "#":
                    score += self.expand(
                        dots, blocks, index + 1, block_index, current + 1
                    )
        self.SCORES[key] = score
        return self.SCORES[key]

    def part1(self):
        """Solve part 1"""
        answer = 0
        for line in self.data:
            self.SCORES.clear()
            dots, blocks = line.split()
            blocks = [int(x) for x in blocks.split(",")]
            score = self.expand(dots, blocks, 0, 0, 0)
            answer += score
        return answer

    def part2(self):
        """Solve part 2"""
        answer = 0
        for line in self.data:
            self.SCORES.clear()
            dots, blocks = line.split()
            dots = "?".join([dots, dots, dots, dots, dots])
            blocks = [int(x) for x in ",".join([blocks] * 5).split(",")]
            score = self.expand(dots, blocks, 0, 0, 0)
            answer += score
        return answer


if __name__ == "__main__":
    AocSolution().print_solution()
