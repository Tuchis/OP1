"""
Docstring for LAB 9 Module 2
"""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def find_max_1(functional, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    list_of_results = []
    if type(functional) == str:
        f_diff = functional
        functional = lambda x: eval(f_diff)
    for variabal in points:
        list_of_results.append(functional(variabal))
    return max(list_of_results)

def find_max_2(functional, points):
    """
    (function or str, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    dict_of_res = {}
    if type(functional) == str:
        f_diff = functional
        functional = lambda x: eval(f_diff)
    for variabs in points:
        val = functional(variabs)
        try:
            value = dict_of_res[val].copy()
            value.append(variabs)
            dict_of_res[val] = value
        except (TypeError, IndexError, KeyError):
            dict_of_res[val] = [variabs]
    keys = dict_of_res.keys()
    max_key = max(keys)

    return dict_of_res[max_key]
print(find_max_2('x ** 2 - 2', [2, -2]))

def compute_limit(seq):
    """
    (function or str) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []  # the list sequence elements
    if type(seq) == str:
        f_diff = seq
        seq = lambda n: eval(f_diff)
    a_n = seq  # the sequence formula

    i = 0


    while True:
        variabal = 10 ** i  # the number of element
        lst.append(seq(variabal))

        # check the difference between elements
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return round(lst[i], 2)
        i += 1
print(compute_limit('(n ** 2 + n) / n ** 2'))
print(compute_limit(lambda x: (x ** 2 + x) / x ** 2))

def compute_derivative(functional, x_0):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    aprox = []

    i = 0

    while True:
        x_diiff = 10 ** -i

        if type(functional) == str:
            functio_x = functional
            functional = lambda x: eval(functio_x)

        variab_x = x_0 + x_diiff
        differ_f = functional(variab_x)  # dF = f(x_0 + dx)

        variab_x = x_0
        differ_f -= functional(variab_x)  # dF = f(x_0 + dx) - f(x_0)

        der = differ_f / x_diiff  # der = (f(x_0 + dx) - f(x_0))/ dx

        aprox.append(der)

        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return round(aprox[i], 2)
        i += 1
compute_derivative('x ** 2 + x', 2)
compute_derivative(lambda x: x ** 2 + x, 2)

def get_tangent(functional, x_0):
    """
    (function or str, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    devia = compute_derivative(functional, x_0)
    if type(functional) == str:
        function_x = functional
        functional = lambda x: eval(function_x)
    differ = functional(x_0) - devia * x_0
    if abs(devia) != devia:
        devia = "- " + str(abs(devia))
    else:
        devia = str(abs(devia))
    if abs(differ) != differ:
        differ = "- " + str(abs(differ))
    else:
        differ = "+ " + str(abs(differ))
    return str(devia) + " * x " + str(differ)

print(get_tangent('x ** 2 + x', 2))
print(get_tangent('- x ** 2 + x', 2))
print(get_tangent(lambda x: x ** 2 + x, 2))

def get_root(functional, first_var, second_var):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    if type(functional) == str:
        diff_f = functional
        functional = lambda x: eval(diff_f)

    if first_var > second_var:
        first_var, second_var = second_var, first_var

    varabla = float(first_var)

    while varabla < second_var:
        if round(functional(varabla), 2) == 0:
            if round(varabla,2) == -0.0:
                return 0.0
            return round(varabla,2)
        else:
            varabla += 0.001
print(get_root(lambda x: x**2 - 7, -4, 1))
