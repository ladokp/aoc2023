# test_aoc_day_25.py

import pytest

import solution.aoc_day_25 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert dict(test_solution.data) == {
        "bvb": {"rhn", "ntq", "cmg", "xhk", "hfx"},
        "cmg": {"rzs", "nvd", "bvb", "lhk", "qnr"},
        "frs": {"lsr", "qnr", "rsh", "lhk"},
        "hfx": {"rhn", "bvb", "ntq", "xhk", "pzl"},
        "jqt": {"rhn", "nvd", "xhk", "ntq"},
        "lhk": {"frs", "nvd", "cmg", "lsr"},
        "lsr": {"frs", "rzs", "lhk", "rsh", "pzl"},
        "ntq": {"bvb", "hfx", "xhk", "jqt"},
        "nvd": {"jqt", "cmg", "lhk", "qnr", "pzl"},
        "pzl": {"hfx", "nvd", "rsh", "lsr"},
        "qnr": {"rzs", "nvd", "cmg", "frs"},
        "rhn": {"bvb", "hfx", "xhk", "jqt"},
        "rsh": {"frs", "lsr", "rzs", "pzl"},
        "rzs": {"cmg", "qnr", "rsh", "lsr"},
        "xhk": {"rhn", "jqt", "bvb", "ntq", "hfx"},
    }


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 54


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() is None


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 555_856


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == None
