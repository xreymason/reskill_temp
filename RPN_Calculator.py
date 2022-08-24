#!/C/Anaconda3/python.exe
"""
Convert string of numbers and symbols to list with:
    * String is split by spaces
    * All numbers converted to floats
    * Leave all symbols
Convert strings of digits to floats
Process each operation by index
    Ex:
    '2 3 + 2 /'#should equal 1;
    [2] -> [2,3] -> [5] -> [5,2] -> [2.5]
    (2+3)/2
"""


def correct_symbol_to_number_ratio(rpn_list:list) -> bool:
    """Checks if there is 1 less symbol than numbers

    :param rpn_list: converted rpn list with numbers and symbols
    :type rpn_list: list
    :return: if there is 1 less symbol than numbers
    :rtype: bool
    """
    which_are_nums = [type(item) in (float, int) for item in rpn_list]
    num_count = which_are_nums.count(True)
    symbol_count = which_are_nums.count(False)
    if num_count-1 == symbol_count:
        return True
    else:
        return False


def convert_rpn_string(rpn:str) -> list:
    """Converts an rpn string that's seperated by spaces
    to a list with all numbers converted to floats

    :param rpn: string of math where numbers are followed by math operation symbols
    :type rpn: str
    :raises TypeError: raised if rpn is not a string
    :return: numbers and symbols are all kept in place as their coresponding types
    :rtype: list
    """
    if type(rpn) != str:
        raise TypeError("invalid rpn type, must be type string")
    formatted_rpn = []
    for item in rpn.split():
        if item.replace('.','',1).isdigit():
            item = float(item)
        formatted_rpn.append(item)
    if not correct_symbol_to_number_ratio(formatted_rpn):
        raise ArithmeticError("Incorrect number of symbols to numbers,\n there can only be 1 more number than the number of symbols")
    return formatted_rpn


def process_math_operation(symbol:str, a:float, b:float) -> float:
    """Performs the operation based on the math symbol passed

    :param symbol: math operation symbol (eg. +, -, *, /)
    :type symbol: str
    :param a: first number in operation
    :type a: float
    :param b: second number in operation
    :type b: float
    :raises TypeError: If arguments a or b aren't an int or float
    :raises ValueError: If symbol isn't supported
    :return: the calculated total
    :rtype: float
    """
    from operator import add, sub, mul, truediv

    arg_testing = {'a':a,'b':b}
    for k in arg_testing:
        if type(arg_testing[k]) not in (int, float):
            raise TypeError(f"Argument {k}: not of type int or float")
    total = a
    if symbol == '+':
        total = add(a, b)
    elif symbol == '-':
        total = sub(a, b)
    elif symbol == '*':
        total = mul(a, b)
    elif symbol == '/':
        total = truediv(a, b)
    else:
        raise ValueError("""%s is an invalid character,
    use the help function for valid characters.
    help(Execute_RPN_Calculation)"""%(symbol))
    return total


def Execute_RPN_Calculation(rpn_string:str, debug:bool=False) -> float:
    rpn_list = convert_rpn_string(rpn_string)
    tmp_rpn_list = rpn_list.copy()
    operation_stack = []
    for item in tmp_rpn_list:
        if type(item) in (float, int):
            operation_stack.append(item)
        else:
            if len(operation_stack) < 2:
                raise ArithmeticError("Not enough numbers before operator")
            op_total = process_math_operation(item, operation_stack.pop(-2), operation_stack.pop(-1))
            operation_stack.append(op_total)
        if debug:
            print(operation_stack)
    return operation_stack[0]


if __name__ == "__main__":
    inp = '2 3 + 2 /'#should equal 1; (2+3)/5
    inp = '2 3 + 6 2 - /'
    # inp = '9 4 3 6 + *'
    inp = '+ 9 4 3 -'
    print(Execute_RPN_Calculation(inp, debug=True))