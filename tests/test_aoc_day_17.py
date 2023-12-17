# test_aoc_day_17.py

import pytest

import solution.aoc_day_17 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        ["2", "4", "1", "3", "4", "3", "2", "3", "1", "1", "3", "2", "3"],
        ["3", "2", "1", "5", "4", "5", "3", "5", "3", "5", "6", "2", "3"],
        ["3", "2", "5", "5", "2", "4", "5", "6", "5", "4", "2", "5", "4"],
        ["3", "4", "4", "6", "5", "8", "5", "8", "4", "5", "4", "5", "2"],
        ["4", "5", "4", "6", "6", "5", "7", "8", "6", "7", "5", "3", "6"],
        ["1", "4", "3", "8", "5", "9", "8", "7", "9", "8", "4", "5", "4"],
        ["4", "4", "5", "7", "8", "7", "6", "9", "8", "7", "7", "6", "6"],
        ["3", "6", "3", "7", "8", "7", "7", "9", "7", "9", "6", "5", "3"],
        ["4", "6", "5", "4", "9", "6", "7", "9", "8", "6", "8", "8", "7"],
        ["4", "5", "6", "4", "6", "7", "9", "9", "8", "6", "4", "5", "3"],
        ["1", "2", "2", "4", "6", "8", "6", "8", "6", "5", "5", "6", "3"],
        ["2", "5", "4", "6", "5", "4", "8", "8", "8", "7", "7", "3", "5"],
        ["4", "3", "2", "2", "6", "7", "4", "6", "5", "5", "5", "3", "3"],
    ]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 102


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 94


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 970


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 1_149
