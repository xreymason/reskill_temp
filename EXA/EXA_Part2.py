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
    @property
    def _operators(self):
        """Easy to use lookup table for different test methods
        Note: Did this to limit user to only these methods

        :return: Conditional methods
        :rtype: dict
        """
        from operator import eq, gt, lt
        comparitors = {
            "=": eq,
            ">": gt,
            "<": lt
        }
        return comparitors


    def _test(self, value:int, comparitor:str, value2:int):
        """Checks if a condition is True or False

        :param value: number to compare to value2
        :type value: int
        :param comparitor: operator
        :type comparitor: str
        :param value2: number to compare to value
        :type value2: int
        :raises ValueError: When comparitor isn't one of the defined ones
        """
        if comparitor not in self._operators:
            raise ValueError("Invalid comparitor, must be in: %s"%self._operators.keys())

        value = self.get_value(value)
        value2 = self.get_value(value2)
        self.T = 1 if self._operators[comparitor](value,value2) else 0


    @property
    def operations(self) -> dict:
        """Easy to use lookup table for different commands
        Updated Operation dictionary:
        'TEST'

        :return: All operations available in a single lookup table
        :rtype: dict
        """
        ops = super().operations
        ops.update({'TEST':self._test})
        return ops


if __name__ == "__main__":
    bot = ExaBot2()
    command = "TEST 4 < 5"
    print(ExaCommand(command).command_structure())
    bot.process_command(ExaCommand(command), debug=True)