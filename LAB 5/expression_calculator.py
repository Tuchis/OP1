""" Expression calculator

Returns:
    int or float: The result ofthe expression
"""

def calculate_expression(expression):
    """ The main function of the calculator

    Args:
        expression (str): The input of the user (the expression)

    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    def expression_check(expression ,word_number):
        """Function to check the words of the expression

        Args:
            expression (str): The word, which is checked
            word_number (int): Word's number

        Returns:
            str: the next math sign
        """
        if expression[word_number] == "додати" or expression[word_number] == "плюс":
            return "+"
        elif expression[word_number] == "відняти" or expression[word_number] == "мінус":
            return "-"
        elif expression[word_number] == "помножити" and expression[word_number + 1]== "на":
            return "*"
        elif expression[word_number] == "поділити" and expression[word_number + 1] == "на":
            return "/"
        elif expression[word_number] == "на":
            pass
        else:
            return "Неправильний вираз!"
    result = ""
    expression = expression[13:len(expression) - 1].split()
    number = 0
    num_status = 0
    sign_status = 0
    for expr in expression:
        result = str(result)
        if expr.isalpha() is True:
            num_status = False
            if expression_check(expression, number) == "Неправильний вираз!":
                return "Неправильний вираз!"
            if expression[number] == "на":
                pass
            else:
                if sign_status is True:
                    return "Неправильний вираз!"
                result = result + " " + expression_check(expression, number)
                sign_status = True
        else:
            if num_status is True:
                return "Неправильний вираз!"
            result = result + expr
            num_status = True
            sign_status = False
            try:
                result = eval(result)
            except:
                return "Неправильний вираз!"
        number += 1
    if number % 1 == 0:
        return int(result)
    return result
print(calculate_expression('Скільки буде 10 додати додати 9?'))
