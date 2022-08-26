from ..EXA import ExaCommand, ExaBot
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
        bot.process_command(ExaCommand("SUPER 4 5 T"))

## Invalidated due to moving the execute_file method from bot to EXA_Commander.py

# def test_EB_passed_error1_program():
#     bot = ExaBot()
#     with pytest.raises(ValueError):
#         bot.execute_file(r".\tests\error1.exa")


# def test_EB_passed_error2_program():
#     bot = ExaBot()
#     with pytest.raises(ValueError):
#         bot.execute_file(r".\tests\error2.exa")


# def test_EB_passed_error3_program():
#     bot = ExaBot()
#     with pytest.raises(ValueError):
#         bot.execute_file(r".\tests\error3.exa")

