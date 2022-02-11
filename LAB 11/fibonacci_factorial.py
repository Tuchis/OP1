"""
LAB 11 Module 2
"""

import time

def numbers_time_test(function=0, realisation=0, verbose=False):
    """
    Function to find time tests
    @param function:
    @param realisation:
    @param verbose:
    """
    if verbose:
        functions = ['factorial_recursive(5, verbose)', 'fibonacci_recursive(5, verbose)',\
                     'factorial_iterative(5, verbose)', 'fibonacci_iterative(5, verbose)']
    else:
        functions = ['factorial_recursive(5, verbose)', 'fibonacci_recursive(5, verbose)',\
                     'factorial_iterative(5, verbose)', 'fibonacci_iterative(5, verbose)']
    index = function * 1 + realisation * 2
    start = time.time()
    print(eval(functions[index]))
    finish = time.time()
    return finish - start

def factorial_recursive(attempt, printer = False, result = 1):
    """
    Returns factorial recursively
    @param attempt:
    @return:
    >>> factorial_recursive(6)
    720
    """
    if printer:
        print(result)
    if attempt == 1:
        return 1
    result *= attempt
    if attempt == 2:
        return result
    return factorial_recursive(attempt - 1, printer,  result)

def factorial_iterative(attempt, printer=False):
    """
    Returns factorial iteratively
    @param attempt:
    @return:
    >>> factorial_iterative(6)
    720
    """
    res = 1
    for i in range(attempt):
        if printer:
            print(res)
        res *= (i + 1)
    return res

def fibonacci_recursive(attempt, printer=False):
    """
    Returns fibonacci recursively
    @rtype: object
    >>> fibonacci_recursive(6)
    13
    """
    if attempt == 0 or attempt == 1:
        return 1
    if printer:
        print(fibonacci_recursive(attempt - 1))
    return fibonacci_recursive(attempt - 1) + fibonacci_recursive(attempt - 2)

def fibonacci_iterative(attempt, printer=False):
    """
    Returns fibonacci iteratively
    @rtype: object
    >>> print(fibonacci_iterative(6))
    13
    """
    fib_1, fib_2 = 1, 1
    for _ in range(attempt - 1):
        if printer:
            print(fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2
