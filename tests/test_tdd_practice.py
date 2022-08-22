import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from tdd_practice import find3

import pytest

def test_passed_number():
    with pytest.raises(TypeError):
        find3(5)


def test_list_with_no_runs():
    assert find3(['a','a','v','b']) == []


def test_list_with_single_run():
    assert find3([2,1,1,1,2,3,3]) == [1]


def test_list_with_multiple_runs():
    assert find3([1,2,2,2,3,3,3,4]) == [1,4]


def test_list_with_intertwined_runs():
    assert find3([1,3,3,3,3]) == [1,2]


def test_passed_string():
    assert find3('aaacccbs') == [0,3]


def test_wrapping_run():
    assert find3([1,1,2,3,4,5,1]) == [-1]