# test_aoc_day_21.py

import pytest

import solution.aoc_day_21 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "#", "#", "#", ".", "#", "."],
            [".", "#", "#", "#", ".", "#", "#", ".", ".", "#", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", "#", "#", ".", ".", "S", "#", "#", "#", "#", "."],
            [".", "#", "#", ".", ".", "#", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "#", ".", "."],
            [".", "#", "#", ".", "#", ".", "#", "#", "#", "#", "."],
            [".", "#", "#", ".", ".", "#", "#", ".", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ],
        11,
        11,
        5,
        5,
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1(6) == 16


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2(6) is 16


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 3_598


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 601_441_063_166_538
