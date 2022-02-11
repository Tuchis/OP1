""" Lab 6 3
"""

def happy_number(number: int) -> bool:
    """Checks if the number is happy

    >>> happy_number(43211234)
    True
    >>> happy_number(12345)
    False
    >>> happy_number(191234)
    True
    """
    while len(str(number)) < 8:
        number = "0" + str(number)
    first_part = 0
    second_part = 0
    for onenum in str(number)[0:4]:
        first_part += int(onenum)
    for onenum in str(number)[4:8]:
        second_part += int(onenum)
    if first_part == second_part:
        return True
    else:
        return False

def count_happy_numbers(num: int) -> bool:
    """Counts happy numbers

    >>> count_happy_numbers(150000)
    840
    """
    count = 0
    for number in range(num):
        if happy_number(number) is True:
            count += 1
    return count

def happy_numbers(start: int, finish: int) -> list:
    """Counts happy numbers in certain range

    >>> happy_numbers(150000, 800000)
    15912
    """
    count = 0
    for number in range(start, finish):
        if happy_number(number) is True:
            count += 1
    return count
