

from typing import Iterable


def find3(iterable:Iterable) -> tuple:
    """Gets first index for each run of 3 of 
    the same object/values in an iterable,
    runs that wrap around will use a negative 
    index.

    :param iterable: object with possible sets of 3
    :type iterable: Iterable
    :return: starting index for each set of 3
    :rtype: tuple
    """
    if type(iterable) not in [list, str, tuple, set, dict]:
        raise TypeError("passed value must be iterable")
    indicies = []
    for i,v in enumerate(iterable):
        if type(iterable) == str:
            iterable = list(iterable)

        if len(iterable) < (i+3):
            wrap_amount=(i+3) % len(iterable)
            wrapped_vals = iterable[i:] + iterable[:wrap_amount]
            if ([v]*3) == wrapped_vals:
                indicies.append(i-len(iterable))
        elif ([v]*3) == iterable[i:i+3]:
            indicies.append(i)
    return tuple(indicies)