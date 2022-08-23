# import sys, os
# parent_dir = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(parent_dir)
# from tdd_practice import summer

from ..tdd_practice import summer
import pytest

def test_empty():
    assert summer([],1) == []


def test_single_solution():
    assert summer([1,2,4,5], 3) == [(1,2)]


def test_multi_solution():
    assert summer([1,2,3,4,5],6) == [(1,5),(2,4),(1,2,3)]


def test_passed_list_with_strings():
    with pytest.raises(TypeError):
        summer([1,2,'c',4,'e'],6)