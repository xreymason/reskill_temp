import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from EXA import ExaBot, ExaCommand

def process_file(file_path:str) -> list:
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


def execute_file(file_path:str, bot:ExaBot, debug=False):
    """Performs all commands in the passed file

    :param file_path: Absolute File Path to .exa file
    :type file_path: str
    :param debug: show commands as performed, defaults to False
    :type debug: bool, optional
    """
    commands = bot.process_file(file_path)
    for command in commands:
        if debug:
            print(ExaCommand.command_structure(command))
        bot.process_command(command, debug)


if __name__ == "__main__":
    from EXA import ExaBot2, ExaBot3

    print("Basic Bot V1 Program2")
    bot1 = ExaBot()
    execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program2.exa", bot1, debug=True)

    print("\nBot V2 Program3")
    bot2 = ExaBot2()
    execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program3.exa", bot2, debug=True)

    print("\nBot V3 Program4")
    bot3 = ExaBot3()
    execute_file(r"C:\Users\mdupont\Downloads\reskill_temp\EXA\program4.exa", bot3, debug=True)