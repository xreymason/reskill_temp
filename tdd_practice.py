

from typing import Iterable


def find3(indexable:Iterable) -> tuple:
    """Gets first index for each run of 3 of 
    the same object/values in an iterable,
    runs that wrap around will use a negative 
    index.

    :param indexable: indexable object with possible sets of 3
    :type indexable: Iterable
    :return: starting index for each set of 3
    :rtype: tuple
    """
    acceptable_types = (list, str, tuple)
    if type(indexable) not in acceptable_types:
        raise TypeError("passed value must be of type " + str(acceptable_types))
    indicies = []
    for i,v in enumerate(indexable):
        if type(indexable) in (str, tuple):
            indexable = list(indexable)

        if len(indexable) < (i+3):
            wrap_amount=(i+3) % len(indexable)
            wrapped_vals = indexable[i:] + indexable[:wrap_amount]
            if ([v]*3) == wrapped_vals:
                indicies.append(i-len(indexable))
        elif ([v]*3) == indexable[i:i+3]:
            indicies.append(i)
    return tuple(indicies)


def summer(numbers:list,num_to_sum_to:int) -> list:
    """Finds all combinations of numbers passed that 
    will sum to a certain number

    :param numbers: numbers to go through
    :type numbers: list
    :param num_to_sum_to: number to try to search for sums for
    :type num_to_sum_to: int/float
    :return: combinations of numbers that sum to desired value
    :rtype: list
    """
    from itertools import combinations
    
    all_combos = []
    for combo_length in range(len(numbers)):
        if combo_length == 0:
            continue
        for combo in combinations(numbers, combo_length):
            if sum(combo) == num_to_sum_to:
                all_combos.append(tuple(combo))
    return all_combos

# if __name__ == "__main__":
#     print(summer([1,2,4,5], 3))
#     print(summer([1,2,3,4,5],6))