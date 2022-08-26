from ..EXA import ExaBot2, ExaCommand
import pytest


def test_passed_gt_as_comparitor():
    bot = ExaBot2()
    bot._test(4, '>', 2)
    assert bot.T == True


def test_passed_lt_as_comparitor():
    bot = ExaBot2()
    bot._test(5, '<', 3)
    assert bot.T == False


def test_passed_eq_as_comparitor():
    bot = ExaBot2()
    bot._test(10, '=', 10)
    assert bot.T == True


def test_passed_invalid_comparitor():
    bot = ExaBot2()
    with pytest.raises(ValueError):
        bot._test(4, '+', 2)


def test_passed_a_test():
    bot = ExaBot2()
    bot.process_command(ExaCommand("TEST 4 < 5"), debug=True)
    assert bot.T == 1