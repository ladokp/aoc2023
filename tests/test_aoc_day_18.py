# test_aoc_day_18.py

import pytest

import solution.aoc_day_18 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        ("R", 6, "R", 461937),
        ("D", 5, "D", 56407),
        ("L", 2, "R", 356671),
        ("D", 2, "D", 863240),
        ("R", 2, "R", 367720),
        ("D", 2, "D", 266681),
        ("L", 5, "L", 577262),
        ("U", 2, "U", 829975),
        ("L", 1, "L", 112010),
        ("U", 2, "D", 829975),
        ("R", 2, "L", 491645),
        ("U", 3, "U", 686074),
        ("L", 2, "L", 5411),
        ("U", 2, "U", 500254),
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 62


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 952_408_144_115


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 62_500


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 122_109_860_712_709
