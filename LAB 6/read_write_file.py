"""Lab 6 5
"""
from typing import List
import urllib.request

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/ma\
ster/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/ma\
ster/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', \
'197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """

    with urllib.request.urlopen(url) as webpage:
        lists = []
        output_list = []
        for line in webpage:
            if len(lists) < number:
                line = line.strip()
                line = line.decode( 'utf-8' )
                if "РK" in line:
                    output_list = []
                if line[0].isnumeric() is True:
                    line_arg = line.split("\t")
                    output_list.append(line_arg[0])
                    output_list.append(line_arg[1])
                    output_list.append("+")
                    output_list.append(line_arg[3])
                elif "Середній бал документа про освіту" in line:
                    grade = line[34:]
                    output_list.append(grade)
                    lists.append(output_list)
        return lists

def write_csv_file(url: str):
    """Writes txt file into csv
    """
    file_op = open("total.csv", "w")
    file_op.write("№,ПІБ,Д,Заг.бал,С.б.док.осв.\n")
    outputs = read_input_file(url, 200)
    for elem in outputs:
        counter = 0
        for word in elem:
            if counter == 4:
                file_op.write(word)
                file_op.write("\n")
            else:
                file_op.write(word)
                file_op.write(",")
            counter += 1
    file_op.close()
write_csv_file("https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt")
