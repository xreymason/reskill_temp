from ..EXA import ExaBot4, ExaCommand, EXA_Commander
import pytest


def test_passed_a_test():
    bot = ExaBot4()
    bot.process_command(ExaCommand("TEST 4 < 5"), debug=True)
    assert bot.T == 1


def test_passed_final_challenge():
    from ..EXA import file_system
    print("\nBot V4 Program5")
    bot = ExaBot4()
    EXA_Commander.execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program5.exa", bot, debug=True)
    assert file_system.files[400] == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]#Might not include 1