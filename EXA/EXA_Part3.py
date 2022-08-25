"""Exa Object (Part 3)
Needs-
    * Add MARK command
        - used to label a location to go in a program when using the following commands
    * Add JUMP command
        - used to go to a labeled location in a program
    * Add TJMP command
        - Jumps to a labeled location if the T register is not equal to 0
    * Add FJMP command
        - Jumps to a labeled location if the T register is equal to 0
Implementation Plan-
    * Whenever a MARK command is found, store its index in a dictionary with the label as it's key
    * Whenever a JUMP command is found, look up the label in the dictionary MARK stores values in
        then change the current command index to the label value
    * TJMP will check if register T is not equal to 0, if True it will run the JUMP command
    * FJMP will check if register T is equal to 0, if True it will run the JUMP command 
"""
import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from EXA.EXA_Part2 import ExaBot2, ExaCommand


class ExaBot3(ExaBot2):
    def __init__(self):
        super().__init__()
        self._ptr = 0
        self._labels = {}


    @property
    def command_ptr(self)->int:
        """Getter for the command pointer
        
        :rtype: int
        """
        return int(self._ptr)
    @command_ptr.setter
    def command_ptr(self,value:int):
        """Setter for the command pointer
        
        :param value: pointer index
        :type value: int)
        """
        self._ptr = int(value)
    

    def _mark(self, label:str):
        self._labels.update({label:self.command_ptr})

    
    def _jump(self, label:str):
        if label in self._labels:
            self.command_ptr = self._labels[label]
        else:
            raise ValueError("Label(%s) not defined"%label)

    
    def _tjmp(self, label:str):
        if self.T != 0:
            self._jump(label)


    def _fjmp(self, label:str):
        if self.T == 0:
            self._jump(label)


    @property
    def operations(self) -> dict:
        ops = super().operations
        new_ops = {
            'MARK':self._mark,
            'JUMP':self._jump,
            'TJMP':self._tjmp,
            'FJMP':self._fjmp
            }
        ops.update(new_ops)
        return ops


    def execute_file(self, file_path:str, debug=False):
        """Performs all commands in the passed file

        :param file_path: Absolute File Path to .exa file
        :type file_path: str
        :param debug: show commands as performed, defaults to False
        :type debug: bool, optional
        """
        commands = self.process_file(file_path)
        self.command_ptr = 0
        while self.command_ptr < len(commands):
            command = commands[self.command_ptr]
            if debug:
                print(ExaCommand.command_structure(command))
            self.process_command(command, debug)
            self.command_ptr +=1


if __name__ == "__main__":
    bot1 = ExaBot3()
    # bot1.execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program1.exa", debug=True)
    bot1.execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program4.exa", debug=True)