def find_max_1(f, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1("lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    list_of_results = []
    for x in points:
        if type(f) != str:
            list_of_results.append(f(x))
        else:
            list_of_results.append(eval(f))
    return max(list_of_results)


print(find_max_1('x ** 2 + x', [1, 2, 3, -1]))
print(find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1]))