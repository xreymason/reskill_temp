from ..EXA.EXA_Part3 import ExaBot3, ExaCommand
import pytest


## Test ExaBot3 Object
def test_EB3_MARK_a_POSITION():
    bot = ExaBot3()
    bot.process_command(ExaCommand("MARK ACE"))
    assert "ACE" in bot._labels and bot._labels["ACE"] == bot.command_ptr


def test_EB3_JUMP():
    bot = ExaBot3()
    bot.command_ptr = 0
    bot.process_command(ExaCommand("MARK ACE"))
    bot.command_ptr = 10
    bot.process_command(ExaCommand("JUMP ACE"))
    assert bot.command_ptr == 0


def test_EB3_TJMP():
    bot = ExaBot3()
    bot.command_ptr = 3
    bot.process_command(ExaCommand("MARK ACE"))#should store 3
    bot.command_ptr = 10
    bot.process_command(ExaCommand("TEST 3 < 5"))
    bot.process_command(ExaCommand("TJMP ACE"))
    assert bot.command_ptr == 3


def test_EB3_FJMP():
    bot = ExaBot3()
    bot.command_ptr = 5
    bot.process_command(ExaCommand("MARK ACE"))#should store 5
    bot.command_ptr = 10
    bot.process_command(ExaCommand("TEST 3 > 5"))
    bot.process_command(ExaCommand("FJMP ACE"))
    assert bot.command_ptr == 5