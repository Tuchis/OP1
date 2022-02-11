""" Laboratory 6 Target game
"""
from typing import List
import string
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    square = []

    for _ in range(3):
        line = []
        for _ in range(3):
            rand_let = random.choice(string.ascii_lowercase)
            line.append(rand_let)
            print(rand_let.upper(), " ", end="")
        square.append(line)
        print()
    return square


def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt', [el for el in 'wumrovkif'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', \
'kori', 'miro', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    """
    word_bank = []
    letters_const = letters.copy()
    letters_list = []
    for _ in range(len(letters)):
        try:
            timed_letter = letters[len(letters) - 1]
            letters_list.append(tuple((timed_letter, letters.count(timed_letter))))
            while timed_letter in letters:
                letters.remove(timed_letter)
        except IndexError:
            continue
    for letter in letters:
        letters_list.append(tuple((letter, letters.count(letter))))
        while letter in letters:
            letters.remove(letter)
    try:
        with open(file) as file_open:
            for line in file_open:
                line = line.strip().lower()
                status = True
                center_status = False
                word = line
                line = sorted(line)
                letter_list = []
                for _ in range(len(line)):
                    try:
                        timed_letter = line[len(line) - 1]
                        letter_list.append(tuple((timed_letter, line.count(timed_letter))))
                        while timed_letter in line:
                            line.remove(timed_letter)
                    except IndexError:
                        continue
                for sets in letter_list:
                    if sets[0] == letters_const[4]:
                        center_status = True
                    if sets[0] in letters_const:
                        val = [(y) for x, y in letters_list if x == sets[0]]
                        val = val[0]
                        if val < sets[1]:
                            status = False
                            break
                        else:
                            continue
                    else:
                        status = False
                        break
                if status is True and center_status is True and len(word) > 3:
                    word_bank.append(word)
    except FileNotFoundError:
        return None
    return word_bank



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.

    """
    user_input = input().lower()
    user_words = user_input.split()
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str],
     words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    wrong_list = []

    letters_const = letters.copy()
    letters_list = []
    for _ in range(len(letters)):
        try:
            timed_letter = letters[len(letters) - 1]
            letters_list.append(tuple((timed_letter, letters.count(timed_letter))))
            while timed_letter in letters:
                letters.remove(timed_letter)
        except IndexError:
            continue
    for letter in letters:
        letters_list.append(tuple((letter, letters.count(letter))))
        while letter in letters:
            letters.remove(letter)
    for line in user_words:
        line = line.strip().lower()
        status = True
        center_status = False
        word = line
        line = sorted(line)
        letter_list = []
        for _ in range(len(line)):
            try:
                timed_letter = line[len(line) - 1]
                letter_list.append(tuple((timed_letter, line.count(timed_letter))))
                while timed_letter in line:
                    line.remove(timed_letter)
            except IndexError:
                continue
        for sets in letter_list:
            if sets[0] == letters_const[4]:
                center_status = True
            if sets[0] in letters_const:
                val = [(y) for x, y in letters_list if x == sets[0]]
                val = val[0]
                if val < sets[1]:
                    status = False
                    break
                else:
                    continue
            else:
                status = False
                break
        if status is True and center_status is True and len(word) > 3:
            wrong_list.append(word)
    counter = 0
    for variable in range(len(wrong_list)):
        if wrong_list[variable - counter] in words_from_dict:
            wrong_list.pop(variable - counter)
            counter += 1
        else:
            pass
    return wrong_list

def results():
    """Prints resulst and saves into file result.txt
    """
    sets_of_let = generate_grid()
    list_of_let = []
    for set_need in sets_of_let:
        for letter in set_need:
            list_of_let.append(letter)
    list_of_let_copy = list_of_let.copy()
    words_list = get_words("en.txt", list_of_let)
    user_words = get_user_words()
    wrong_words = get_pure_user_words(user_words, list_of_let_copy, words_list)
    correct_count = 0
    for elem in user_words:
        if elem in words_list:
            correct_count += 1
    print(correct_count)
    output_words_list = ""
    for wordes in words_list:
        output_words_list += wordes + " "
    print(output_words_list)
    missed_words = ""
    for wordes in words_list:
        if wordes not in user_words:
            missed_words += wordes + " "
    missed_words = missed_words[:-1]
    print(missed_words)
    wrong_spelled = ""
    for wrong in wrong_words:
        if wrong not in words_list:
            wrong_spelled += wrong + " "
    wrong_spelled = wrong_spelled[:-1]
    print(wrong_spelled)

    with open("result.txt", "w") as file_op:
        file_op.write(str(correct_count))
        file_op.write("\n")
        file_op.write(output_words_list)
        file_op.write("\n")
        file_op.write(missed_words)
        file_op.write("\n")
        file_op.write(wrong_spelled)
        file_op.write("\n")
        file_op.close()
print(get_words('en.txt', [el for el in 'wumrovkif']))