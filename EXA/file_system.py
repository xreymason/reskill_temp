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
    100:[-100, 5, 8, -3, 113],
    200:[],
    400:[]
    }


# File Modifiers
def _file_exists(file_id:int) -> bool:
    return file_id in files


def _get_file(file_id:int) -> list:
    if _file_exists(file_id):
        return files[file_id]
    else:
        raise FileNotFoundError("File(%r) doesn't exist in files"%(file_id))


def _valid_line_number(file_id:int, line_number:int) -> bool:
    file = _get_file(file_id)
    if line_number < len(file):
        return line_number
    elif line_number == len(file):
        return line_number
    else:
        raise ValueError("Invalid line number(%s)"%(line_number))


def get_file_length(file_id:int) -> int:
    return len(_get_file(file_id))


def create_file(file_id:int):
    if _file_exists(str(file_id)):
        raise FileExistsError()
    files.update({str(file_id):[]})


def read_file_line(file_id:int, line_number:int) -> int:
    file = _get_file(file_id)
    line_number = _valid_line_number(file_id, line_number)
    return file[line_number]


def write_file_line(file_id:int, line_number:int, new_value:int):
    file = _get_file(file_id)
    line_number = _valid_line_number(file_id, line_number)
    if line_number < get_file_length(file_id):
        file[line_number] = new_value
    else:
        file.append(new_value)    


def delete_file_line(file_id:int, line_number:int):
    line_number = _valid_line_number(file_id, line_number)
    files[file_id].pop(line_number)


# Bot Usage Managers
def _is_file_open(file_id:int) -> bool:
    return file_id in bot_manager.values()


def _is_bot_using_file(bot:ExaBot) -> bool:
    return bot in bot_manager.keys()


def bot_close_file(bot:ExaBot):
    bot_manager.pop(bot, None)


def bot_open_file(file_id:int, bot:ExaBot):
    if _is_bot_using_file(bot):
        raise ValueError("Bot has a File open")
    if _is_file_open(file_id):
        raise ValueError("File is open elsewhere")
    bot_manager.update({bot:file_id})


def what_file_is_bot_using(bot:ExaBot) -> int:
    return bot_manager.get(bot, None)