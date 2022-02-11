"""LAB 6 Calendar
"""

import calendar as kalendar
import datetime

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    names_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return names_of_week[number]

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    date = date.split(".")
    day, month_cur, year_cur = int(date[0]), int(date[1]), int(date[2])
    week_num = datetime.date(year_cur,month_cur,day).weekday()
    return week_num

def calendar(month_fun: int, year_fun: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    if 1 <= month_fun <= 12 and year_fun > 1583:
        pass
    else:
        raise AssertionError ("Wrong input")
    int_day = weekday("1." + str(month_fun) + "." + str(year_fun))
    current_date = 1
    num_days = kalendar.monthrange(year_fun, month_fun)[1]
    string = "mon tue wed thu fri sat sun\n" + "    " * int_day
    while current_date <= num_days:
        for _ in range(int_day, 7):
            if current_date > num_days:
                continue
            if int_day == 0:
                if current_date < 10:
                    # print(" ", current_date, end = "", sep = "")
                    string = string + "  " + str(current_date)
                else:
                    # print(current_date, end = "", sep = "")
                    string = string + " " + str(current_date)
            else:
                if current_date == 1:
                    # print(" ", current_date, end = "", sep = "")
                    string = string + "  " + str(current_date)
                elif current_date < 10:
                    # print("  ", current_date, end = "", sep = "")
                    string = string + "   " + str(current_date)
                else:
                    # print(" ", current_date, end = "", sep = "")
                    string = string + "  " + str(current_date)
            current_date += 1
            if int_day == 6:
                # print()
                string = string + "\n"
                int_day = 0
            else:
                int_day += 1
    # print("\n\"\"\"")
    if string[len(string)-1:] == "\n":
        string = string[:-1]
    return string



def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    lines = calendar.split("\n")
    lines_list = []
    for elem in lines:
        days = elem.split()
        lines_list.append(days)
    count = len(lines_list)
    output = ""
    delay = 0
    for weekday_range in range(7):
        row = str(lines_list[0][weekday_range])
        for column in range(1, count):
            if 7 - len(lines_list[column]) > weekday_range and column == 1:
                row = row + "  "
                delay += 1
                continue

            status_length = False
            for num in lines_list[column]:
                if len(num) == 2:
                    status_length = True

                    continue
            if status_length is False:
                if column == 1:
                    row = row + " " + lines_list[column][weekday_range - delay]
                    #     if len(lines_list[column][weekday - delay]) == 1:
                    # except IndexError:
                    #     row = row + " " + lines_list[column][weekday - delay]
                else:
                    if len(lines_list[column][weekday_range]) == 1:
                        row = row + " " + lines_list[column][weekday_range]
                    else:
                        row = row + " " + lines_list[column][weekday_range]

            else:
                try:
                    if len(lines_list[column][weekday_range]) == 1:
                        row = row + " " + lines_list[column][weekday_range]
                    else:
                        row = row + " " + lines_list[column][weekday_range]
                except IndexError:
                    pass
        output = output + row + "\n"
    output = output[:-1]
    return output

print(calendar(4, 2021))

if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)

