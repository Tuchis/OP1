"""
LAB 12 Names
"""

def quick_sort_list(lst):
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
    lst[:breaker + 1] = quick_sort_list(lst[:breaker + 1])
    lst[breaker + 2:] = quick_sort_list(lst[breaker + 2:])
    return lst

def find_names(file_path):
    """
    Function to find names in the file
    @param file_path:
    @return:
    >>> find_names("girl_names") #doctest: +ELLIPSIS
    ({...
    """

    with open(file_path) as file:
        one_count = 0
        oners = set()
        counter = 0
        counts = {}
        letters = {}
        most = set()
        for line in file:
            try:
                name, times = line.split("\t")
                name = name[:-1]
                times = int(times[1:-2])
                counts[times] = name
            except ValueError:
                continue
            if times == 1:
                oners.add(name)
                one_count += 1
            try:
                valer = letters[name[0]]
                valer = [valer[0] + 1, valer[1] + times]
                letters[name[0]] = valer
                if valer[0] + 1 > counter:
                    counter = valer[0] + 1
                    max_letter = name[0]
            except KeyError:
                letters[name[0]] = [1, times]
        keys = list(counts.keys())
        keys = quick_sort_list(keys)[-3:]
        for elem in keys:
            most.add(counts.get(elem))

        return (most, (one_count, oners), (max_letter, letters[max_letter][0],\
                                            letters[max_letter][1]))
print(find_names("boy_names"))