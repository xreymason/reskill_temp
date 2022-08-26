"""Acts as a file system of sorts
Needs -
    * Create_File Method
        - Creates an empty list in the file system(dictionary)
        - Accepts a file_name as an argument
    * Read_File Method
        - Reads from a specified file at a specified line(index)
        - Accepts a file_name and line_number as args
    * Write_File Method
        - Writes a value in a file on a line
        - Accepts a file_name, line_number, and new_value as args
    * Append_File Method
        - Appends a value at the end of a file
    * Bot file usage manager; bot_manager(dictionary)
        - Due to bots having no reference to what file they're working with
            we need this 'file system' to keep track of what files each bot 
            has, and make sure no 2 have the same file open.
"""
import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from EXA import ExaBot

bot_manager = {}
files = {
    '100':[-100, 5, 8, -3, 113],
    '200':[],
    '400':[]
    }


# File Modifiers
def _file_exists(file_name:str):
    return file_name in files


def _get_file(file_name:str):
    if _file_exists(file_name):
        return files[file_name]
    else:
        raise FileNotFoundError()


def create_file(file_name:str):
    if _file_exists(str(file_name)):
        raise FileExistsError()
    files.update({str(file_name):[]})


def read_file_line(file_name:str, line_number:int):
    file = _get_file(file_name)
    if line_number < len(file):
        return file[line_number]
    else:
        raise ValueError("Invalid line number(%s)"%(line_number))


def write_file_line(file_name:str, line_number:int, new_value:int):
    file = _get_file(file_name)
    if line_number < len(file):
        file[line_number] = new_value
    else:
        raise ValueError("Invalid line number(%s)"%(line_number))


# Bot Usage Managers
def _is_file_open(file_name:str):
    return file_name in bot_manager.values()


def _is_bot_using_file(bot:ExaBot):
    return bot in bot_manager.keys()


def bot_close_file(bot:ExaBot):
    bot_manager.pop(bot, None)


def bot_open_file(file_name:str, bot:ExaBot):
    if _is_bot_using_file(bot):
        raise ValueError("Bot has a File open")
    if _is_file_open(file_name):
        raise ValueError("File is open elsewhere")
    bot_manager.update({bot:file_name})


