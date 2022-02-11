"""
Target Ua (laboratory 6 9)
I'm sad, waiting for success of that program
"""

import random


def generate_grid():
    """
    Generates list of letters - i.e. grid for the game.
    e.g. ['т', 'р', 'с', 'в', 'а']
    """
    alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', \
    'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', \
    'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    square = []
    while len(square) < 5:
        letter = random.choice(alphabet)
        if letter not in square:
            square.append(letter)
    return square


def get_words(file, letters):
    r"""
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words("base.lst", ['ю', 'щ', 'й', 'и', 'ь']) #doctest: +ELLIPSIS
    [('ирій', 'noun'), ('ирод', 'noun'), ('йняти', 'verb')...
    """
    word_bank = []
    letters_const = letters.copy()
    try:
        with open(file) as file_open:
            for line in file_open:
                status = False
                line_list = line.strip().lower().split()
                word = line_list[0]
                if len(word) > 5:
                    continue
                for let in letters_const:
                    if let in word[0]:
                        status = True
                if status is True:
                    pass
                else:
                    continue
                if "/n" in line_list[1][:2] or "noun" in line_list[1][:4]:
                    word_bank.append((word, "noun"))
                if "/v" in line_list[1][:2] or "v" in line_list[1][:1]:
                    word_bank.append((word, "verb"))
                if "/adj" in line_list[1][:4] or "adj" in line_list[1][:4]:
                    word_bank.append((word, "adjective"))
                if "adv" in line_list[1][:3] or "/adv" in line_list[1][:4]:
                    word_bank.append((word, "adverb"))
    except FileNotFoundError:
        return None, True
    return word_bank


def check_user_words(user_words, language_part, letters, dict_of_words):
    """Checks user words, if they are correct.
    >>> check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb",\
['ю', 'щ', 'я', 'ц', 'г'], get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']))
    ['ю', 'щ', 'я', 'ц', 'г']
    (['гаяти', 'гнати'], ['гнити', 'гнути', 'гоїти', 'грати', 'гріти', 'густи', 'юшити',\
 'явити', 'яріти', 'ячати'])
    """
    print(letters)
    word_bank = []
    lost = []
    for word in user_words:
        for words in dict_of_words:
            if word == words[0] and language_part == words[1]:
                word_bank.append(word)
    for right_word in dict_of_words:
        if right_word[0] not in word_bank and right_word[1] == language_part:
            lost.append(right_word[0])
    return word_bank, lost


def game(file, language_part):
    """
    Starts game
    """
    letters = generate_grid()
    user_input = input().lower().split()
    word_list = get_words(file, letters)
    word_right, lost = check_user_words(user_input, language_part, letters, word_list)
    print((x) for x in word_right)
    print(lost)
print(generate_grid())
