"""Exa Object (Part 2)
Needs-
    * Add TEST Method that acts like an if statement
        > Ex. TEST X = 4
    * TEST must accept the following conditional operands:
        *  = > <
    * TEST must store its output:
        * as 1 or 0
        * in T register
"""
import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from EXA.EXA_Part1 import ExaBot, ExaCommand


class ExaBot2(ExaBot):
    def _test(self, value:int, comparitor:str, value2:int):
        from operator import eq, gt, lt
        comparitors = {
            "=": eq,
            ">": gt,
            "<": lt
        }
        if comparitor not in comparitors:
            raise ValueError("Invalid comparitor, must be in: %s"%comparitors.keys())

        value = self.get_value(value)
        value2 = self.get_value(value2)
        self.T = 1 if comparitors[comparitor](value,value2) else 0


    @property
    def operations(self) -> dict:
        ops = super().operations
        ops.update({'TEST':self._test})
        return ops


if __name__ == "__main__":
    bot = ExaBot2()
    command = "TEST 4 < 5"
    print(ExaCommand(command).command_structure())
    bot.process_command(ExaCommand(command), debug=True)