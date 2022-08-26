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
from EXA.EXA_Part1 import RegisterError
import file_system


class ExaBot4(ExaBot3):
    def __init__(self):
        self._f = 0
        super().__init__()

    @property
    def F(self)->int:
        """Getter for the current value on a line in a file
        
        :rtype: int
        """
        file_id = file_system.what_file_is_bot_using(self)
        value = file_system.read_file_line(file_id, self._f)
        self._seek()
        return value
    @F.setter
    def F(self,value:int):
        """Setter for the current value on a line in a file
        
        :param value: number to write or append into the current file
        :type value: int)
        """
        file_id = file_system.what_file_is_bot_using(self)
        file_system.write_file_line(file_id, self._f, int(value))
        self._seek()


    def is_register(self, item:object) -> bool:
        """Checks if the object passed is one of the defined registers

        :param item: object to check
        :type item: object
        :return: if object is a listed register
        :rtype: bool
        """
        #Chose not to do hasattr() since that could return false positives
        return item in ('X','T','F','_f')


    def show_registers(self):
        """Prints out all the register values
        """
        for reg in ('X','T','_f'):
            print("%s: %s"%(reg, self.get_register_value(reg)),end=",\t")
        print()


    def _grab(self, file_name:str):
        """Tells file system to link/lock this bot to a file,
        also resets F pointer to 0

        :param file_name: file to link
        :type file_name: str
        """
        file_system.bot_open_file(file_name,self)
        self._f = 0

    
    def _drop(self):
        """Tell's the file system to unlink/unlock this bot
        from it's corresponding file
        """
        file_system.bot_close_file(self)


    def _file(self, target:str):
        """Stores the file name of the file that's linked to this bot
        in the target register

        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        file = file_system.what_file_is_bot_using(self)
        if self.is_register(target):
            setattr(self, target, self.get_value(file))
        else:
            raise ValueError(RegisterError%str(target))


    def _void(self):
        """Tells the file system to remove the currently 
        selected line from the file linked to this bot
        """
        file_id = file_system.what_file_is_bot_using(self)
        file_system.delete_file_line(file_id, self._f)


    def _seek(self, amount=1):
        """Moves the pointer forward(positive) or backward(negative)
        and limits the pointer to 0 or the length of the file

        :param amount: how much to move, defaults to 1
        :type amount: int, optional
        """
        file_id = file_system.what_file_is_bot_using(self)
        f_len = file_system.get_file_length(file_id)
        self._f += amount

        if self._f > f_len:
            self._f = self._f-1
        if self._f <= 0:
            self._f = 0

    
    def _test(self, value: object, comparitor: str=None, value2: int=None):
        """Checks if a condition is True or False

        :param value: number to compare to value2 or 'EOF'
        :type value: object
        :param comparitor: operator, defaults to None
        :type comparitor: str, optional
        :param value2: number to compare to value, defaults to None
        :type value2: int, optional
        :raises ValueError: When comparitor isn't one of the defined ones
        """
        if str(value) == 'EOF':
            file_id = file_system.what_file_is_bot_using(self)
            f_len = file_system.get_file_length(file_id)
            self.T = 1 if self._f >= f_len-1 else 0
        else:
            super()._test(value, comparitor, value2)


    @property
    def operations(self) -> dict:
        """Easy to use lookup table for different commands
        Updated Operation dictionary:
        'GRAB', 'FILE', 'SEEK', 'VOID', 'DROP'

        :return: All operations available in a single lookup table
        :rtype: dict
        """
        ops = super().operations
        new_ops = {
            'GRAB': self._grab,
            'FILE': self._file,
            'SEEK': self._seek,
            'VOID': self._void,
            'DROP': self._drop
        }
        ops.update(new_ops)
        return ops


if __name__ == "__main__":
    bot = ExaBot4()
    commands = [
        'GRAB 100',
        'MARK FILE_READ',
        'ADDI F X X',
        'TEST EOF',
        'FJMP FILE_READ',
        'DROP',
        'GRAB 200',
        'COPY X F',
        'DROP'
    ]

    bot.command_ptr = 0
    while bot.command_ptr < len(commands):
        command = commands[bot.command_ptr]
        print(ExaCommand(command).command_structure())
        bot.process_command(ExaCommand(command), debug=True)
        bot.command_ptr +=1

    command = "TEST 4 < 5"
    print(ExaCommand(command).command_structure())
    bot.process_command(ExaCommand(command), debug=True)

    print(file_system.files)