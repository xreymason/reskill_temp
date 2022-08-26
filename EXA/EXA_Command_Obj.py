
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
            # elif value.isalpha():
            #     pass
            # elif len(value) != 1:
            #     raise ValueError("invalid value: %s"%(value))
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
