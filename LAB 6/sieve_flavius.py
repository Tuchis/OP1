""" The program to maek sieve flavius """

from typing import List

def sieve_flavius(names: int) -> List[int]:
    """ The main function of the module

    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    """
    start_list = range(1, names+1)
    start_list = list(start_list)
    copy_list = start_list.copy()
    try:
        for names in copy_list:
            if names == 1:
                continue
            if names in start_list:
                try:
                    counter = 0
                    for j in range(1, len(start_list)):
                        del start_list[names * j - 1 - counter]
                        counter += 1
                except IndexError:
                    continue
    except IndexError:
        pass
    return start_list
