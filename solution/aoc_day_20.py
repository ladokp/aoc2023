# aoc_day_20.py
from collections import defaultdict, deque

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        modules, receive_from = {}, defaultdict(dict)
        for line in puzzle_input.split("\n"):
            label, out = line.split(" -> ")
            typ = 0
            if label[0] == "%":
                typ = 1
                label = label[1:]
            elif label[0] == "&":
                typ = 2
                label = label[1:]
            modules[label] = (typ, out.split(", "))
            for out_n in out.split(", "):
                receive_from[out_n][label] = False
        return modules, receive_from

    DAY = 20

    def solve_(self, part2=False):
        modules, receive_from = self.data
        lows, highs, buttons, flip_stat, high_buttons, conjunction_state = (
            0,
            0,
            0,
            defaultdict(lambda: False),
            defaultdict(int),
            {
                label: {label_1: False for label_1 in receive_from[label]}
                for label in modules
            },
        )
        while buttons < 5000:
            buttons += 1
            queue = deque()
            queue.append(("broadcaster", False, "button"))
            while queue:
                label, pulse, from_lbl = queue.popleft()
                highs += pulse
                lows += not pulse
                if pulse:
                    high_buttons[from_lbl] = buttons
                if label not in modules:
                    continue
                type_, send_to = modules[label]
                if type_ == 0:
                    for elt in send_to:
                        queue.append((elt, pulse, label))
                elif type_ == 1:
                    if pulse:
                        continue
                    flip_stat[label] = not flip_stat[label]
                    for elt in send_to:
                        queue.append((elt, flip_stat[label], label))
                elif type_ == 2:
                    conjunction_state[label][from_lbl] = pulse
                    for elt in send_to:
                        queue.append(
                            (
                                elt,
                                not all(conjunction_state[label].values()),
                                label,
                            )
                        )
            if all(
                (
                    not part2,
                    buttons == 1000,
                )
            ):
                return lows * highs

        if part2:
            result = 1
            for label in receive_from[list(receive_from["rx"])[0]]:
                result *= high_buttons[label]
            return result

    def part1(self):
        """Solve part 1"""
        return self.solve_()

    def part2(self):
        """Solve part 2"""
        return self.solve_(True)


if __name__ == "__main__":
    AocSolution().print_solution()
