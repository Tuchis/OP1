# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    """
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """

    for i in range(len(sequence) // 2):
        seq = sequence[0:i+1]
        if type(sequence) == list:
            timed_sequence = sequence.copy()
        else:
            timed_sequence = sequence
        variable = True
        counter = 0
        while len(timed_sequence) > 0:
            if variable == False:
                break
            count = 0
            variable = 0
            for j in seq:
                if j == timed_sequence[count]:
                    count += 1
                    variable = True
                    pass
                else:
                    variable = False
                    break
            if variable == True:
                for _ in range(len(seq)):
                    if type(sequence) == list:
                        timed_sequence.pop(0)
                    else:
                        timed_sequence = timed_sequence[1:]
                counter += 1
            else:
                continue
        if len(timed_sequence) == 0:
            return seq, counter
    return None


print(pattern_number("111111"))
