""" Laboratory work """

import string


def get_number():
    """ Function to make necessary tests"""
    number = 88
    return number


# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Problem 1
# ****************************************
def get_position(character):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter
    function should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """
    character = str(character)
    if len(character) > 1:
        return None
    if character in string.ascii_uppercase or character \
            in string.ascii_lowercase:
        count = 1
        character = character.lower()
        while character != string.ascii_lowercase[count - 1]:
            count += 1
        return count
    return None


# ****************************************
# Problem 3
# ****************************************
def compare_str(string1, string2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is
    larger than string s2 and False otherwise. If arguments aren't
    string or function have different length function should return
    None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    string1 = str(string1)
    string2 = str(string2)
    for i in string1:
        if i.isalpha() is False:
            return None
    for i in string2:
        if i.isalpha() is False:
            return None
    if len(string1) == len(string2):
        pass
    else:
        return None
    return bool(string1 <= string2)


# ****************************************
# Problem 4
# ****************************************


def type_by_angles(aangle, bangle, cangle):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return
    type as string ("right angled triangle", "obutuse triangle",
    "acute triangle"). If there is no triangle with such angles, then
    function should return None.

    >>> type_by_angles(60, 60, 60)
    acute triangle
    >>> type_by_angles(90, 30, 60)
    right angled triangle
    >>> type_by_angles(2015, 2015, 2015)

    """
    if aangle + bangle + cangle != 180 or aangle < 0 or bangle < 0 or \
            cangle < 0 or aangle > 180 or bangle > 180 or cangle > 180:
        return None
    if aangle == 90 or bangle == 90 or cangle == 90:
        return "right angled triangle"
    elif aangle > 90 or bangle > 90 or cangle > 90:
        return "obutuse triangle"
    return "acute triangle"


# ****************************************
# Problem 5
# ****************************************


def type_by_sides(aside, bside, cside):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If
    there is no triangle with such sides, then function should return
    None.
    >>> type_by_sides(3, 3, 3)
    "acute triangle"
    >>> type_by_sides(3, 4, 5)
    "right angled triangle"
    >>> type_by_sides(3, 3, 2015)
    """
    sorter = [aside, bside, cside]
    sorter.sort()
    aside, bside, cside = sorter[0], sorter[1], sorter[2]
    if cside > aside + bside:
        return None
    if cside ^ 2 == aside ^ 2 + bside ^ 2:
        return "right angled triangle"
    elif cside ^ 2 >= aside ^ 2 + bside ^ 2:
        return "obutuse triangle"
    return "acute triangle"


# ****************************************
# Problem 6
# ****************************************
def remove_spaces(stringspace):
    """
    str -> str
    Remove all additional spaces in string and return a new string
    without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    I'll make him an offer he can't refuse.
    >>> remove_spaces
    ("Great    men     are    not born great, they grow great...")
    Great men are not born great, they grow great...
    >>> remove_spaces(2015)

    """
    delay = 0
    status = 0
    count = 0
    try:
        massive = list(stringspace)
    except TypeError:
        return None
    length = len(massive)
    for i in range(length):
        if i < len(massive):
            if massive[i - delay] == " ":
                if status is True:
                    massive.pop(count)
                    count -= 1
                    delay += 1
                status = True
            else:
                status = False
            count += 1
    stringspace = "".join(massive)
    return stringspace


# ****************************************
# Problem 7
# ****************************************


def convert_to_column(stringlong):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print_column
    ("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column
    ("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print_column(2015)
    """
    try:
        for i in stringlong:
            if i.isnumeric() is True:
                return None
    except TypeError:
        return None
    stringlong = stringlong.lower()
    stringer = ""
    massive = stringlong.split()
    start = True
    for i in massive:
        for j in i:
            if j not in string.ascii_letters:
                i = i.replace(j, "")
        if start is True:
            stringer = "" + i
            start = False
        else:
            stringer = stringer + "\n" + i
    return stringer


# ****************************************
# Problem 10
# ****************************************
def encrypt_message(stringcode):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet.
    If argument is not a string function should return None.

    >>> encrypt_message
    ("Revenge is a dish that tastes best when served cold.")
    Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.
    >>> encrypt_message
    ("Never hate your enemies. It affects your judgment.")
    Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.
    >>> encrypt_message(2015)

    """
    stringer = ""
    try:
        for i in stringcode:
            if i.isnumeric() is True:
                return None
            num = ord(i)
            if num in (90, 122):
                num -= 25
            if (65 <= num <= 89) or (97 <= num <= 121):
                num += 1
            letter = chr(num)
            stringer = stringer + letter
    except TypeError:
        return None
    return stringer

# ****************************************
# Problem 13
# ****************************************


def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument
    isn't list of 26 positive integer numbers function should return
    None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 4]])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    output = ""
    count = 0
    if len(lst) != 26:
        return None
    for i in lst:
        if i > 0:
            for _ in range(i):
                output = output + chr(count + 97)
        count += 1

    return output

# ****************************************
# Problem 24
# ****************************************


def numbers_Ulam(position_num):
    """
    Function to search n's Ulam number

    Args:
        n ([int]): [Sequence umber of desirabel Ulam number]

    Returns:
        [int]: [n's Ulam number]
    """
    ulan_numbers = [1, 2]
    for _ in range(position_num-2):
        timed_list = []
        for element1 in ulan_numbers:
            position = int(ulan_numbers.index(element1))
            for element2 in ulan_numbers[position + 1:len(ulan_numbers)]:
                new_element = element1 + element2
                timed_list.append(new_element)
        timed_list.sort()
        delete_list = []
        for number in timed_list:
            try:
                if number == timed_list[timed_list.index(number) + 1]:
                    delete_list.append(number)
            except IndexError:
                pass
        for delete_element in delete_list:
            while delete_element in timed_list:
                timed_list.remove(delete_element)
        for ellement in timed_list:
            if ellement > ulan_numbers[len(ulan_numbers) - 1]:
                ulan_numbers.append(ellement)
                break
    return ulan_numbers[0:position_num]

# ****************************************
# Problem 25
# ****************************************


def happy_number(number):
    """Finds, if the number is "happy"

    Args:
        number (int): the number

    Returns:
        bool: True, if the number is happy,
        False, if the number isn't happy
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    sequence = [number]
    for _ in range(100):
        summa = 0
        number_timed = sequence[len(sequence) - 1]
        number_timed = str(number_timed)
        for num in number_timed:
            num = int(num)
            summa = summa + num ** 2
        sequence.append(summa)
        print(sequence)
        if sequence[len(sequence) - 1] == 1:
            return True
    return False


# ****************************************
# Problem 26
# ****************************************


def sum_of_divisors(divis_num, lst):
    """ Find and return sum of all odd numbers in the list,
    that are divisible by n.

    Args:
        divis_num (int): the number to divide by
        lst (list): the list of numbers, we want to divide

    Returns:
        int: sum of divisors

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    summa = 0
    for element in lst:
        if element % 2 == 1:
            if element % divis_num == 0:
                summa += element
    return summa


# ****************************************
# Problem 27
# ****************************************
def turn_over(turn_num, lst):
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    Args:
        turn_num (int): number of turns
        lst (list): list of items

    Returns:
        list: turned list

    >>> reverse(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> reverse(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> reverse(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> reverse(-5, [])
    []
    """
    if turn_num > len(lst):
        return None
    delay = 0
    for _ in range(turn_num//2):
        lst[delay], lst[turn_num - 1 -
                        delay] = lst[turn_num - 1 - delay], lst[delay]
        delay += 1
    return lst


# if __name__ == "__main__":
#   import doctest
#   print(doctest.testmod())
