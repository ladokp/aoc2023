# aoc_day_09.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        lines = puzzle_input.split("\n")
        return tuple(list(map(int, line.split())) for line in lines)

    DAY = 9

    @staticmethod
    def extrapolate(sequence, *, part2=False):
        sequences, sequence_1 = [sequence], sequence.copy()
        while len(list(filter(lambda x: x != 0, sequence_1))) > 0:
            sequence_2 = [
                sequence_1[index + 1] - sequence_1[index]
                for index in range(len(sequence_1) - 1)
            ]
            sequences.append(sequence_2.copy())
            sequence_1 = sequence_2

        sequences[-1].append(0)
        for index in range(len(sequences) - 1, 0, -1):
            if part2:
                sequences[index - 1].insert(
                    0, sequences[index - 1][0] - sequences[index][0]
                )
            else:
                sequences[index - 1].append(
                    sequences[index][-1] + sequences[index - 1][-1]
                )
        return sequences[0][0 if part2 else -1]

    def part1(self):
        """Solve part 1"""
        return sum(self.extrapolate(line) for line in self.data)

    def part2(self):
        """Solve part 2"""
        return sum(self.extrapolate(line, part2=True) for line in self.data)


if __name__ == "__main__":
    AocSolution().print_solution()
