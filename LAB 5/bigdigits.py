""" Program to print numbers using numbers
"""
import sys


def return_digits(digits):
    r""" Function that returns the lines

    >>> return_digits('192837465') #doctest: +ELLIPSIS
     1  9999 222  888  333 77777...
    >>> return_digits('123') #doctest: +ELLIPSIS
     1  222  333...
    """
    try:
        result = ""
        digits = str(digits)
        digits = digits.rstrip()
        row = 0
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                for i in digit[row]:
                    for j in i:
                        if j == " ":
                            line += " "
                        else:
                            line += str(number)
                column += 1
            result = result + line + "\n"
            row += 1
        result = result[:len(result)-1]
        print(result)
        return result

    except ValueError as err:
        print(err, "in", digits)



Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
try:
    arg = sys.argv[1]
    return_digits(arg)
except IndexError:
    pass
