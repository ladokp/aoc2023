# aoc_day_07.py
import functools
from collections import Counter

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        list_ = []
        for line in puzzle_input.split("\n"):
            list_.append(line)
        return list_

    DAY = 7

    @staticmethod
    def strength(hand, part2):
        hand = hand.replace("T", chr(ord("9") + 1))
        hand = hand.replace("J", chr(ord("2") - 1) if part2 else chr(ord("9") + 2))
        hand = hand.replace("Q", chr(ord("9") + 3))
        hand = hand.replace("K", chr(ord("9") + 4))
        hand = hand.replace("A", chr(ord("9") + 5))

        counter = Counter(hand)
        if part2:
            target = list(counter.keys())[0]
            for key in counter:
                if key != "1":
                    if counter[key] > counter[target] or target == "1":
                        target = key
            assert target != "1" or list(counter.keys()) == ["1"]
            if "1" in counter and target != "1":
                counter[target] += counter["1"]
                del counter["1"]
            assert "1" not in counter or list(counter.keys()) == ["1"], f"{counter} {hand}"

        if sorted(counter.values()) == [5]:
            return 10, hand
        if sorted(counter.values()) == [1, 4]:
            return 9, hand
        if sorted(counter.values()) == [2, 3]:
            return 8, hand
        if sorted(counter.values()) == [1, 1, 3]:
            return 7, hand
        if sorted(counter.values()) == [1, 2, 2]:
            return 6, hand
        if sorted(counter.values()) == [1, 1, 1, 2]:
            return 5, hand
        if sorted(counter.values()) == [1, 1, 1, 1, 1]:
            return 4, hand
        raise ValueError(f"{counter} {hand} {sorted(counter.values())}")

    def solve_part(self, part2=False):
        hands, answer = [], 0
        for line in self.data:
            hand, bid = line.split()
            hands.append((hand, bid))
        hands = sorted(hands, key=lambda current: self.strength(current[0], part2))
        for rank, (_, bid) in enumerate(hands):
            answer += (rank + 1) * int(bid)
        return answer

    def part1(self):
        """Solve part 1"""
        return self.solve_part()

    def part2(self):
        """Solve part 2"""
        return self.solve_part(True)


if __name__ == "__main__":
    AocSolution().print_solution()
