from ..EXA.EXA_Part1 import ExaCommand, ExaBot
import pytest


## Test ExaCommand Object



## Test ExaBot Object
def test_EB_subtracts_into_negative_result():
    bot = ExaBot()
    bot.process_command(ExaCommand("SUBI 5 10 T"))
    assert bot.T == -5


def test_EB_subtracts_negative_number():
    bot = ExaBot()
    bot.process_command(ExaCommand("SUBI 5 -10 T"))
    assert bot.T == 15


def test_EB_passed_too_many_args_to_any_operations():
    bot = ExaBot()
    with pytest.raises(TypeError):
        bot.process_command(ExaCommand("COPY 5 -10 7 T"))
        bot.process_command(ExaCommand("ADDI 5 -10 7 T"))
        bot.process_command(ExaCommand("SUBI 5 -10 7 T"))
        bot.process_command(ExaCommand("MULI 5 -10 7 T"))
        bot.process_command(ExaCommand("DIVI 5 -10 7 T"))
        bot.process_command(ExaCommand("MODI 5 -10 7 T"))


def test_EB_passed_invalid_action():
    bot = ExaBot()
    with pytest.raises(ValueError):
        # bot.process_command(ExaCommand("SUPER 4 5 T").command_structure())
        bot.process_command(ExaCommand("SUPER 4 5 T"))