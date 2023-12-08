# test_aoc_day_08.py

import pytest

import solution.aoc_day_08 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        "LR",
        2,
        {
            "11A": {"L": "11B", "R": "XXX"},
            "11B": {"L": "XXX", "R": "11Z"},
            "11Z": {"L": "11B", "R": "XXX"},
            "22A": {"L": "22B", "R": "XXX"},
            "22B": {"L": "22C", "R": "22C"},
            "22C": {"L": "22Z", "R": "22Z"},
            "22Z": {"L": "22B", "R": "22B"},
            "AAA": {"L": "BBB", "R": "BBB"},
            "BBB": {"L": "AAA", "R": "ZZZ"},
            "XXX": {"L": "XXX", "R": "XXX"},
            "ZZZ": {"L": "ZZZ", "R": "ZZZ"},
        },
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 2


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 6


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 11_911


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 10_151_663_816_849
