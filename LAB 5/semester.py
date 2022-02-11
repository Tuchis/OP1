""" Program to create calendar in txt or in html formats

Returns:
    str: Calendar in one of 2 formats (html or txt)
"""

import datetime
import calendar
from calendar import monthrange

def semester_calendar(output_type, year, first_month, last_month):

    string = ""

    """ Program to create calendar in txt or in html formats

    Args:
        output_type (str): Format of output
        year (int): Year of a calendar
        first_month (int): First month of the calendar
        last_month (int): Last month of the calendar

    Returns:
        str: Calendar in one of two formats (txt or html)
    """
    if 1 <= first_month <= 12 and 1 <= last_month <= 12:
        pass
    else:
        return None
    int_day = datetime.date(year=year, month=first_month, day=1).weekday()

    def month_txt(current_month, int_day, string):
        """ Printing of a certain month in a calendar in txt format

        Args:
            current_month (int): Month, which has to showed
            int_day (int): The day of the week, that month has to start

        Returns:
            int: The last weekday of the calendar
        """
        # print("\"\"\"    ", calendar.month_name[current_month], year)
        # print("Mo Tu We Th Fr Sa Su")
        # print("   " * int_day, end = "", sep = "")
        string = string + ("    " +
         str(calendar.month_name[current_month])+ " " + str(year) + "\n")
        string = string + "Mo Tu We Th Fr Sa Su\n"
        string = string + "   " * int_day
        current_date = 1
        num_days = monthrange(year, current_month)[1]
        while current_date <= num_days:
            for _ in range(int_day, 7):
                if current_date > num_days:
                    continue
                if int_day == 0:
                    if current_date < 10:
                        # print(" ", current_date, end = "", sep = "")
                        string = string + " " + str(current_date)
                    else:
                        # print(current_date, end = "", sep = "")
                        string = string + str(current_date)
                else:
                    if current_date == 1:
                        # print(" ", current_date, end = "", sep = "")
                        string = string + " " + str(current_date)
                    elif current_date < 10:
                        # print("  ", current_date, end = "", sep = "")
                        string = string + "  " + str(current_date)
                    else:
                        # print(" ", current_date, end = "", sep = "")
                        string = string + " " + str(current_date)
                current_date += 1
                if int_day == 6:
                    # print()
                    string = string + "\n"
                    int_day = 0
                else:
                    int_day += 1
        # print("\n\"\"\"")
        string = string + "\n"
        return int_day, string


    def month_html(current_month, int_day, string):
        """ Printing of a certain month in a calendar in html format

        Args:
            current_month (int): Month, which has to showed
            int_day (int): The day of the week, that month has to start

        Returns:
            int: The last weekday of the calendar
        """
#         print("<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" \
# class=\"month\">\n<tr><th colspan=\"7\" class=\"month\">",\
# calendar.month_name[current_month], " ", year, " </th></tr>", sep = "")
        string = string + "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" \
class=\"month\">\n<tr><th colspan=\"7\" class=\"month\">" + \
str(calendar.month_name[current_month]) + " " + str(year) + " </th></tr>\n\n"
#         print("<tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th \
# class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><\
# th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr>")
        string = string + "<tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th \
class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><\
th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr>" + "\n\n"
        current_date = 1
        num_days = monthrange(year, current_month)[1]
        while current_date <= num_days:
            weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
            date = 0
            # print("<tr>", end = "")
            string = string + "<tr>"
            for _ in range(int_day, 7):
                if current_date > num_days:
                    # print("<td class=\"noday\">&nbsp;</td>", end = "", sep = "")
                    string = string + "<td class=\"noday\">&nbsp;</td>"
                    continue
                if date < int_day:
                    for _ in range(int_day - date):
                        # print("<td class=\"noday\">&nbsp;</td>", end = "", sep = "")
                        string = string + "<td class=\"noday\">&nbsp;</td>"
                    date = int_day
                # print("</td><td class=\"", weekdays[int_day], "\">",
                #  current_date ,"</td>", end = "", sep = "")
                string = string + "</td><td class=\"" + weekdays[int_day] + "\">" +\
                  str(current_date) + "</td>"
                current_date += 1
                if int_day == 6:
                    # print()
                    string = string + "\n"
                    int_day = 0
                    date = 0
                else:
                    int_day += 1
                    date += 1
            # print()
            string = string + "\n"
        # print()
        string = string + "\n"
        return int_day, string

    if output_type == "txt":
        if last_month < first_month:
            for i in range(first_month, 13):
                int_day, string = month_txt(i, int_day, string)
            year += 1
            for i in range(1, last_month + 1):
                int_day, string = month_txt(i, int_day, string)
        else:
            for i in range(first_month, last_month + 1):
                int_day, string = month_txt(i, int_day, string)
        string = string[:len(string) - 1]

    if output_type == "html":
        if last_month < first_month:
            for i in range(first_month, 13):
                int_day, string = month_html(i, int_day, string)
            year += 1
            for i in range(1, last_month + 1):
                int_day, string = month_html(i, int_day, string)
        else:
            for i in range(first_month, last_month + 1):
                int_day, string = month_html(i, int_day, string)
        string = string[:len(string) - 2]
    return string
                
print(semester_calendar("html", 2016, 2, 3))
