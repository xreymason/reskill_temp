"""Exa Object (Part 4)
Needs-
    * Add F pointer Register
        * F pointer increments each time you Read(get) or Write(set)
    * Add GRAB Method
        > Grab a file with the specified ID. (Accepts R/N)
    * Add FILE Method
        > Copy the ID of the file into the specified register. (Accepts R)
    * Add SEEK Method
        > Move the file cursor forward (positive) or backwards (negative) 
            by the specified number of values. If SEEK would move the file cursor 
            past the beginning or end of the file it will instead be clamped. 
            Thus, you can use values of -9999 or 9999 to reliably move to the 
            beginning or end of a file. (Accepts R/N)
    * Add VOID Method
        > Remove the value highlighted by the file cursor from the currently held file.
         -> Delete the value F is pointing to, from the file (Can only target F)
    * Add DROP Method
        > Drop the currently held file.
    * Add TEST EOF
        > If the file pointer is currently at the end of the held file, 
        set the T register to 1, otherwise set the T register to 0.
Implementation Plan-
    * Make F property 
    * Make _test method's 'comparitor' and 'value2' arguments optional
    * Make _is_end_of_file method to check if at the end of the currently held file
"""
import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from EXA import ExaBot3, ExaCommand
import file_system


class ExaBot4(ExaBot3):
    def __init__(self):
        super().__init__()

    @property
    def F(self)->int:
        """Getter for the current value on a line in a file
        
        :rtype: int
        """
        return int(self._f)
    @F.setter
    def F(self,value:int):
        """Setter for the current value on a line in a file
        
        :param value: number to write or append into the current file
        :type value: int)
        """
        self._f = value


    def _grab(self, file_name:str):
        pass

    
    def _drop(self):
        pass


    def _file(self, target:str):
        pass
    

    def _void(self):
        pass


    def _seek(self, value:int):
        pass

    
    def _test(self, value: int, comparitor: str=None, value2: int=None):
        return super()._test(value, comparitor, value2)


if __name__ == "__main__":
    bot = ExaBot4()
    commands = [
        "COPY 7 T",
        "COPY 1 X",
        "MARK LOOP",
        "MULI X T X",
        "SUBI T 1 T",
        "TJMP LOOP"
    ]# Replace Commands With new ones

    bot.command_ptr = 0
    while bot.command_ptr < len(commands):
        command = commands[bot.command_ptr]
        print(ExaCommand(command).command_structure())
        bot.process_command(ExaCommand(command), debug=True)
        bot.command_ptr +=1

    command = "TEST 4 < 5"
    print(ExaCommand(command).command_structure())
    bot.process_command(ExaCommand(command), debug=True)