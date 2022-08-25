"""EXA Command Structure
* A simple means of storing and converting commands into a usable form
- I'm thinking a class object that:
    * Stores the command as a string
    * Can convert the string into a perferred tuple format
    * Allows the user to modify the command as needed in parts
        > Action
        > Arguments

EXA Bot Object:
R = Register(Value)
N = Number
Needs-
    * Registers X and T to store numbers
    * Register F to store ?Files? (Put placeholder for now)
    - Methods to place values into a Register:
        * Copy Method to take either a R/N and place it into a Register
        * ADDI Method to add 2 (R/N)'s and place the result in a Register
        * SUBI Method to subtract 2 (R/N)'s and place the result in a Register
        * MULI Method to multiply 2 (R/N)'s and place the result in a Register
        * DIVI Method to floor divide 2 (R/N)'s and place the result in a Register
        * MODI Method to modulus 2 (R/N)'s and place the result in a Register
    * Method to process commands into the afformentioned methods
        > For Ease of Use
    * Method to process a file of commands
    * Method to execute a file of commands
"""


class ExaCommand:
    """Object to store and convert Exa command strings 
    to more usable formats
    """
    def __init__(self, command:str):
        if type(command) == str:
            self.command = command
        else:
            raise TypeError("Invalid Command, must be of type str")

    @property
    def Action(self)->str:
        """Getter for action to use other values in
        
        :rtype: str
        """
        return self.command.split()[0]
    @Action.setter
    def Action(self,value:str):
        """Setter for action to use other values in
        
        :param value: command action to use
        :type value: str)
        """
        tmp = self.command.split()
        tmp[0] = str(value)
        self.command = " ".join(tmp)
    

    @property
    def Arguments(self)->list:
        """Getter for arguments to use in action
        
        :rtype: list
        """
        tmp = self.command.split()[1:]
        for i, value in enumerate(tmp):
            if value.strip('-').isdigit():
                tmp[i] = int(value)
            elif value.isalpha():
                pass
            elif len(value) != 1:
                raise ValueError("invalid value: %s"%(value))
        return tmp
    @Arguments.setter
    def Arguments(self,value:list):
        """Setter for arguments to use in action
        
        :param value: all arguments for the desired action
        :type value: list)
        """
        value = [str(v) for v in value]
        tmp = self.command.split()
        self.command = tmp[0] + " " + " ".join(value)
    

    def command_structure(self) -> tuple:
        """Formats the command in a easier to use structure

        :return: Action: Arguments structure
        :rtype: tuple
        """
        return self.Action, self.Arguments


RegisterError = "Target(%s) is not a valid Register"


class ExaBot:
    def __init__(self):
        self.X = 0
        self.T = 0
        self.F = 0


    @property
    def X(self) -> int:
        """Getter for register X
        
        :rtype: int
        """
        return int(self._x)
    @X.setter
    def X(self,value:int):
        """Setter for register X
        
        :param value: number to store in register X
        :type value: int)
        """
        if type(value) == int:
            self._x = value
    

    @property
    def T(self) -> int:
        """Getter for register T
        
        :rtype: int
        """
        return int(self._t)
    @T.setter
    def T(self,value:int):
        """Setter for register T
        
        :param value: number to store in register T
        :type value: int)
        """
        if type(value) == int:
            self._t = value


    def show_registers(self):
        """Prints out all the register values
        """
        for reg in ('X','T','F'):
            print("%s: %s"%(reg, self.get_register_value(reg)),end=",")
        print()
    

    def get_value(self, reg_or_num) -> int:
        """Either gets a value from a register

        :param reg_or_num: _description_
        :type reg_or_num: _type_
        :return: _description_
        :rtype: int
        """
        if self.is_register(reg_or_num):
            value = self.get_register_value(reg_or_num)
        else:
            value = reg_or_num
        return value


    def _copy(self, value:int, target:str):
        """Performs a Copy operation on the value
        then stores it in the target register

        :param value: a number
        :type value: int
        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        if self.is_register(target):
            setattr(self, target, self.get_value(value))
        else:
            raise ValueError(RegisterError%str(target))


    def _addi(self, value:int, value2:int, target:str):
        """Performs a Addition operation on the values
        then stores the result in the target register

        :param value: a number
        :type value: int
        :param value2: a number
        :type value2: int
        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        if self.is_register(target):
            value = self.get_value(value)
            value2 = self.get_value(value2)
            setattr(self, target, value+value2)
        else:
            raise ValueError(RegisterError%str(target))


    def _subi(self, value:int, value2:int, target:str):
        """Performs a Subtraction operation on the values
        then stores the result in the target register

        :param value: a number
        :type value: int
        :param value2: a number
        :type value2: int
        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        if self.is_register(target):
            value = self.get_value(value)
            value2 = self.get_value(value2)
            setattr(self, target, value-value2)
        else:
            raise ValueError(RegisterError%str(target))
    

    def _muli(self, value:int, value2:int, target:str):
        """Performs a Multiplication operation on the values
        then stores the result in the target register

        :param value: a number
        :type value: int
        :param value2: a number
        :type value2: int
        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        if self.is_register(target):
            value = self.get_value(value)
            value2 = self.get_value(value2)
            setattr(self, target, value*value2)
        else:
            raise ValueError(RegisterError%str(target))
    

    def _divi(self, value:int, value2:int, target:str):
        """Performs a Floor Division operation on the values
        then stores the result in the target register

        :param value: a number
        :type value: int
        :param value2: a number
        :type value2: int
        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        if self.is_register(target):
            value = self.get_value(value)
            value2 = self.get_value(value2)
            setattr(self, target, value//value2)
        else:
            raise ValueError(RegisterError%str(target))
    

    def _modi(self, value:int, value2:int, target:str):
        """Performs a Modulus operation on the values
        then stores the result in the target register

        :param value: a number
        :type value: int
        :param value2: a number
        :type value2: int
        :param target: a register to store result in
        :type target: str
        :raises ValueError: When target isn't a defined register
        """
        if self.is_register(target):
            value = self.get_value(value)
            value2 = self.get_value(value2)
            setattr(self, target, value%value2)
        else:
            raise ValueError(RegisterError%str(target))


    @property
    def operations(self) -> dict:
        """Easy to use lookup table for different commands
        Note: Did this to limit user to only these methods

        :return: Exa Command: Implemented Method
        :rtype: dict
        """
        ops = {
            'COPY': self._copy,
            'ADDI': self._addi,
            'SUBI': self._subi,
            'MULI': self._muli,
            'DIVI': self._divi,
            'MODI': self._modi
        }
        return ops


    def is_register(self, item:object) -> bool:
        """Checks if the object passed is one of the defined registers

        :param item: object to check
        :type item: object
        :return: if object is a listed register
        :rtype: bool
        """
        #Chose not to do hasattr() since that could return false positives
        return item in ('X','T','F')


    def get_register_value(self, register:str) -> int:
        """Gets a registers value if the passed object is a register

        :param register: register to get value from or int
        :type register: str
        :return: value stored in a register or the passed int
        :rtype: int
        """
        if self.is_register(register):
            return getattr(self, register)


    def process_command(self, exaCommand:ExaCommand, debug:bool=False):
        """Performs an operation based on the command passed

        :param exaCommand: ExaCommand instance
        :type exaCommand: ExaCommand
        :param debug: show register values after operation is performed, default to False
        :type debug: bool, optional
        :raises ValueError: If the value passed is not a register or int
        """
        if exaCommand.Action in self.operations:
            operation = self.operations[exaCommand.Action]
            conditions = exaCommand.Arguments
            operation(*conditions)
            if debug:
                self.show_registers()
        else:
            raise ValueError("%s is an invalid command"%(exaCommand.Action))


    def process_file(self, file_path:str) -> list:
        """Converts each line in a file to an ExaCommand object

        :param file_path: Absolute File Path to .exa file
        :type file_path: str
        :return: all commands as ExaCommand objects
        :rtype: list
        """
        commands = []
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line.split()) > 1:
                    commands.append(ExaCommand(line))
        return commands


    def execute_file(self, file_path:str, debug=False):
        """Performs all commands in the passed file

        :param file_path: Absolute File Path to .exa file
        :type file_path: str
        :param debug: show commands as performed, defaults to False
        :type debug: bool, optional
        """
        commands = self.process_file(file_path)
        for command in commands:
            if debug:
                print(ExaCommand.command_structure(command))
            self.process_command(command, debug)


if __name__ == "__main__":
    bot1 = ExaBot()
    # bot1.execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program1.exa", debug=True)
    bot1.execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program2.exa", debug=True)
    # commands = bot1.process_file(r"C:\Users\mdupont\Downloads\reskill_temp\program1.exa")
    # for command in commands:
    #     print(command.command_structure())