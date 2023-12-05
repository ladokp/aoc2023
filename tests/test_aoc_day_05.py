# test_aoc_day_05.py

import pytest

import solution.aoc_day_05 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        (
            ((50, 98, 2), (98, 100, -48)),
            ((0, 15, 39), (15, 52, -15), (52, 54, -15)),
            ((0, 7, 42), (7, 11, 50), (11, 53, -11), (53, 61, -4)),
            ((18, 25, 70), (25, 95, -7)),
            ((45, 64, 36), (64, 77, 4), (77, 100, -32)),
            ((0, 69, 1), (69, 70, -69)),
            ((56, 93, 4), (93, 97, -37)),
        ),
        (79, 14, 55, 13),
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 35


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 46


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 324724204


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 104070862
