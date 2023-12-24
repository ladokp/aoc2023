# test_aoc_day_24.py

import pytest

import solution.aoc_day_24 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        ((19, 13, 30), (-2, 1, -2)),
        ((18, 19, 22), (-1, -1, -2)),
        ((20, 25, 34), (-2, -2, -4)),
        ((12, 31, 28), (-1, -2, -1)),
        ((20, 19, 15), (1, -5, -3)),
    ]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1(True) == 2


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() is 47


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 16_502


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 673_641_951_253_289
