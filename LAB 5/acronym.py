""" Program for creating acronyms
"""

def create_acronym(message):
    r""" Function of the program, that receives the phrases
    separated by a newline as an argument, and returns acronyms
    of that phrases.

    Args:
        message (str): The input
    >>> create_acronym("As soon as possible \n Hello world")
    'ASAP - As soon as possible \nHW -  Hello world'
    >>> create_acronym("Дискретна математика \n Основи програмування")
    'ДМ - Дискретна математика \nОП -  Основи програмування'
    """
    result = ""
    acronyms = []
    words = message.split("\n")
    for phrase in words:
        letters_word = phrase.split()
        acronym = ""
        for i in letters_word:
            acronym_letter = i[0].upper()
            acronym += acronym_letter
        acronyms.append(acronym)
        if words[len(words) - 1] == phrase:
            result = result + acronym + " - " + phrase
        else:
            result = result + acronym + " - " + phrase + "\n"
    return result
print(create_acronym("Дискретна математика \n Основи програмування"))
