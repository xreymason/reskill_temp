import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from tdd_practice import find3

import pytest

def test_passed_number():
    with pytest.raises(TypeError):
        find3(5)


def test_passed_dict():
    with pytest.raises(TypeError):
        find3({'a':1,'b':1,'c':1,'d':1})


def test_passed_set():
    with pytest.raises(TypeError):
        find3(set([1,1,1,2,3,3,3]))


def test_passed_tuple():
    assert find3((1,1,1,2,3,3,1)) == (0,-1)


def test_passed_string():
    assert find3('aaacccbs') == (0,3)


def test_list_with_no_runs():
    assert find3(list('aavb')) == ()


def test_list_with_single_run():
    assert find3([2,1,1,1,2,3,3]) == (1,)


def test_list_with_multiple_runs():
    assert find3([1,2,2,2,3,3,3,4]) == (1,4)


def test_list_with_intertwined_runs():
    assert find3([1,3,3,3,3]) == (1,2)


def test_wrapping_run():
    assert find3([1,1,2,3,4,5,1]) == (-1,)