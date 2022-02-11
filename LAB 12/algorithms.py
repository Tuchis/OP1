"""
LAB 12 Algorithms
"""
def linear_search(list_of_values, value):
    """
    Realisation of linear search
    @param list_of_values:
    @param value:
    >>> linear_search([6,3,7,1,234,45,21,65,21,765,1,6,8,23,54,87], 345)
    -1
    """
    for valuab in range(len(list_of_values)):
        if list_of_values[valuab] == value:
            return valuab
    return -1


def merge_sort(lst):
    """
    Realisation of merge sort
    @param lst:
    """
    if len(lst)>1:
        lister = []
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        left = merge_sort(left)
        right = merge_sort(right)

        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lister.append(left[left_index])
                left_index += 1
            else:
                lister.append(right[right_index])
                right_index += 1

        if left_index != len(left):
            lister += left[left_index:]
        else:
            lister += right[right_index:]
        return lister
    else:
        return lst


def binary_search(list_of_values, value, low = 0, up = None):
    """
    Realisation of binary search
    @param list_of_values:
    @param value:
    """
    if up == None:
        up = len(list_of_values)
    middle = (up + low) // 2
    if low == up:
        if list_of_values[middle] == value:
            return middle
        else:
            return -1
    try:
        if list_of_values[middle] > value:
            return binary_search(list_of_values,value,low,middle)
        elif list_of_values[middle] < value:
            return binary_search(list_of_values,value,middle + 1,up)
        else:
            return middle
    except IndexError:
        return -1


def selection_sort(lst, index = 0):
    """
    Realisation of selection sort
    @param lst:
    """
    minimum = index
    for count in range(len(lst) - index):
        if lst[minimum] > lst[count + index]:
            minimum = count + index
    try:
        lst[index], lst[minimum] = lst[minimum], lst[index]
    except IndexError:
        return lst
    if len(lst) > index + 1:
        return selection_sort(lst, index + 1)
    else:
        return lst


def quick_sort(lst):
    """
    Realisation of quick sort
    @param lst:
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    breaker = -1
    for index in range(len(lst)):
        if lst[index] < pivot:
            breaker += 1
            lst[index], lst[breaker] = lst[breaker], lst[index]
        else:
            pass
    lst[-1], lst[breaker + 1] = lst[breaker + 1], lst[-1]
    lst[:breaker + 1] = quick_sort(lst[:breaker + 1])
    lst[breaker + 2:] = quick_sort(lst[breaker + 2:])
    return lst

# listing = [6,3,7,1,234,45,21,65,21,765,1,6,8,23,54,87]
# print(linear_search(listing, 6500))
# print(merge_sort(listing))
# print(binary_search(merge_sort(listing), 89))
# print(selection_sort(listing))
# print(quick_sort(listing))
print(binary_search([10, 40, 68, 100, 194, 274, 550, 4000], 10))
# print(selection_sort([]))
