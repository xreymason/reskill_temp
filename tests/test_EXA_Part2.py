from ..EXA.EXA_Part2 import ExaBot2
import pytest

def test_passed_gt_as_comparitor():
    bot = ExaBot2()
    assert bot._test(4, '>', 2) == True


def test_passed_lt_as_comparitor():
    bot = ExaBot2()
    assert bot._test(5, '<', 3) == False


def test_passed_eq_as_comparitor():
    bot = ExaBot2()
    assert bot._test(10, '=', 10) == True


def test_passed_invalid_comparitor():
    bot = ExaBot2()
    with pytest.raises(ValueError):
        bot._test(4, '+', 2)
