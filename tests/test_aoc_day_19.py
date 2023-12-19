# test_aoc_day_19.py

import pytest

import solution.aoc_day_19 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        {
            "crn": [("x>2662", "A"), (None, "R")],
            "gd": [("a>3333", "R"), (None, "R")],
            "hdj": [("m>838", "A"), (None, "pv")],
            "in": [("s<1351", "px"), (None, "qqz")],
            "lnx": [("m>1548", "A"), (None, "A")],
            "pv": [("a>1716", "R"), (None, "A")],
            "px": [("a<2006", "qkq"), ("m>2090", "A"), (None, "rfg")],
            "qkq": [("x<1416", "A"), (None, "crn")],
            "qqz": [("s>2770", "qs"), ("m<1801", "hdj"), (None, "R")],
            "qs": [("s>3448", "A"), (None, "lnx")],
            "rfg": [("s<537", "gd"), ("x>2440", "R"), (None, "A")],
        },
        [
            "{x=787,m=2655,a=1222,s=2876}",
            "{x=1679,m=44,a=2067,s=496}",
            "{x=2036,m=264,a=79,s=2244}",
            "{x=2461,m=1339,a=466,s=291}",
            "{x=2127,m=1623,a=2188,s=1013}",
        ],
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 19_114


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 167_409_079_868_000


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 386_787


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 131_029_523_269_531
