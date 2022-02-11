"""Program to create calendar in txt or in html formats

Returns:
str: Calendar in one of 2 formats (html or txt)
"""
import calendar
def semester_calendar(output_type, year, first_month, last_month):
    r"""Program to create calendar in txt or in html formats

    Args:
        output_type (str): Format of output
        year (int): Year of a calendar
        first_month (int): First month of the calendar
        last_month (int): Last month of the calendar

    Returns:
        str: Calendar in one of two formats (txt or html)

    >>> semester_calendar("txt", 2021, 10, 10) #doctest: +ELLIPSIS
    '    October 2021...'
    >>> semester_calendar("html", 2021, 10, 10) #doctest: +ELLIPSIS
    '<table border="0" cellpadding="0" cellspacing="0"...'
    """
    output = ""
    if output_type == "txt":
        if last_month < first_month:
            for month in range(first_month, 13):
                output += calendar.month(year, month)
            year += 1
            for month in range(1, last_month + 1):
                output += calendar.month(year, month)
        else:
            for month in range(first_month,last_month + 1):
                output += calendar.month(year, month)
        return output
    else:
        if last_month < first_month:
            for month in range(first_month, 13):
                output += calendar.HTMLCalendar(firstweekday=0).\
                    formatmonth(year, month)
            year += 1
            for month in range(1, last_month + 1):
                output += calendar.HTMLCalendar(firstweekday=0).\
                    formatmonth(year, month)
        else:
            for month in range(first_month,last_month + 1):
                output += calendar.HTMLCalendar(firstweekday=0).\
                    formatmonth(year, month)
        return output
