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

from .EXA_Part1 import ExaBot, ExaCommand
import operator

class ExaBot2(ExaBot):
    def _test(self, value:int, comparitor:str, value2:int):
        pass