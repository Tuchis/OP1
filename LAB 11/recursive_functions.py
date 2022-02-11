"""
LAB 11 Module 1
"""
def create_table(leng, row, lists = None):
    """
    Creates table of numbers
    @rtype: object
    >>> create_table(4,6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    if lists == None:
        lists = []
    listing = []
    for i in range(row):
        try:
            var = lists[len(lists) - 1][i] + listing[-1]
        except IndexError:
            var = 1
        listing.append(var)
    lists.append(listing)
    if len(lists) == leng:
        return lists
    return create_table(leng, row, lists)
print(create_table(7,3))

def flatten(lst, lister = None):
    """
    Returns unpacked lists
    @param lst:
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten([1, [[[[[]], 4.0], "Hello"], [[3]]], True])
    [1, 4.0, 'Hello', 3, True]
    """
    if lister == None:
        lister = []
    try:
        for i in lst:
            if type(i) == list:
                flatten(i, lister)
            else:
                lister.append(i)
    except TypeError:
        return lst
    return lister
