# aoc_day_15.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        return puzzle_input.split(",")

    DAY = 15

    @staticmethod
    def hash_(characters):
        hash_value = 0
        for character in characters:
            ascii_value = ord(character)
            hash_value += ascii_value
            hash_value *= 17
            hash_value %= 256
        return hash_value

    def part1(self):
        """Solve part 1"""
        return sum(self.hash_(characters) for characters in self.data)

    def part2(self):
        """Solve part 2"""
        boxes = [[] for _ in range(256)]
        for command in self.data:
            if command[-1] == "-":
                name = command[:-1]
                hashed_value = self.hash_(name)
                boxes[hashed_value] = [
                    (label, focal_length)
                    for (label, focal_length) in boxes[hashed_value]
                    if label != name
                ]
            elif command[-2] == "=":
                name, length = command[:-2], int(command[-1])
                hashed_value = self.hash_(name)
                if name in [n for (n, v) in boxes[hashed_value]]:
                    boxes[hashed_value] = [
                        (label, length if name == label else focal_length)
                        for label, focal_length in boxes[hashed_value]
                    ]
                else:
                    boxes[hashed_value].append([name, length])

        return sum(
            (index_1 + 1) * (index_2 + 1) * focal_length
            for index_1, box in enumerate(boxes)
            for index_2, (_, focal_length) in enumerate(box)
        )


if __name__ == "__main__":
    AocSolution().print_solution()
