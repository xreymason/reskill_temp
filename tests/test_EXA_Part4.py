from ..EXA import ExaBot4, ExaCommand
import pytest


def test_passed_a_test():
    bot = ExaBot4()
    bot.process_command(ExaCommand("TEST 4 < 5"), debug=True)
    assert bot.T == 1