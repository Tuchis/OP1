"""Program to check amount of a certain character in 2 strings,
if it is in both strings
"""
def total_occurrences(string1, string2, character):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    return string1.count(character) + string2.count(character)
