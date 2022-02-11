"""LAB 6 7
"""
def generate_pascal_triangle(number):
    """ Pascal triangle function
    >>> print(generate_pascal_triangle(5))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    list_out = []
    if number < 1 or type(number) != int:
        return []
    for i in range(number):
        row = [1]
        counter = 0
        while len(row) <= i:
            try:
                summa = list_out[len(list_out) - 1][counter] + \
                    list_out[len(list_out) - 1][counter + 1]
                row.append(summa)
                counter += 1
            except IndexError:
                try:
                    summa = list_out[len(list_out) - 1][counter]
                    row.append(summa)
                except IndexError:
                    summa = 1
        list_out.append(row)
    return list_out
