"""
This module is used to work with children
names
"""


def quick_sort(lst):
    """
    Sorts an array recursively
    by splitting it into
    two subarrays by the medium number
    >>> quick_sort([[1,1],[2,3],[7,9],[11,1]])
    [[1, 1], [11, 1], [2, 3], [7, 9]]
    >>> quick_sort([1])
    [1]
    >>> quick_sort([])
    []
    """
    if not lst:
        return []
    left = quick_sort([i for i in lst[1:] if i[1] < lst[0][1]])
    right = quick_sort([i for i in lst[1:] if i[1] >= lst[0][1]])
    return left + [lst[0]] + right


def find_names(file_path):
    """
    Reads a file and returns a set that
    consists of the most popular names,
    the number of names that only appear
    once in the list, the names that only appear one time
    and a set which consists of the count most popular
    names, the most popular letter and the number of
    times it appears in names.
    """
    names = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            line[-1] = int(line[-1].replace('(', '').replace(')', ''))
            names.append(line)
    names.pop(0)
    names_sorted = quick_sort(names)
    most_popular = set()
    one_time = set()
    one_time_count = 0
    for i in range(1, 4):
        most_popular.add(names_sorted[-i][0])
    children_dict = {}
    for i in names_sorted:
        if i[1] == 1:
            one_time_count += 1
            one_time.add(i[0])
        if i[0][0] not in children_dict:
            children_dict[i[0][0]] = [0, 0]
        children_dict[i[0][0]][0] += 1
        children_dict[i[0][0]][1] += i[1]
    all_children = []
    for name in children_dict:
        all_children.append((name, children_dict[name][0], children_dict[name][1]))
    sort_children = quick_sort(all_children)
    return most_popular, (one_time_count, one_time), sort_children[-1]
print(find_names("girl_names"))