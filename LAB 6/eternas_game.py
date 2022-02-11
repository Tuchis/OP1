"""LAB 6 6
"""
from typing import List
import random

def board_generation() -> List[list]:
    """
    Generates a game board of 16 x 4 size, i.e. two dimensional list (array) o\
f 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    game_board = []
    def set_pick():
        set_signs = ["0", "g", "w"]
        sets = []
        for _ in range(4):
            var = random.randrange(0,3)
            if len(sets) < 4:
                if var == 0:
                    while len(sets) < 4:
                        sets.insert(0, 0)
                else:
                    sets.insert(0, set_signs[var])
        return sets
    for _ in range(16):
        game_board.append(set_pick())
    return game_board


def winning_combination(board: List[list]) -> bool:
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions if there is winning\
 combination or False if not.

    >>> winning_combination([[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'], [0, 0, 'g\
', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'],\
 [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], ['w', 'g', 'w', 'w'], [0,\
 'g', 'w', 'g'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', '\
g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], [\
'g', 'g', 'g', 'w'], [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], ['w',\
 'g', 'g', 'g'], ['w', 'w', 'g', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0,\
 0, 0, 0], [0, 0, 0, 0], [0, 'g', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 'w', 'g'\
]])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w',\
 'g'], ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0,\
 0, 0, 0], [0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, '\
g'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0,\
 0, 0, 'g'], ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], ['w', 'g'\
, 'w', 'g'], [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0\
, 0, 0], [0, 0, 0, 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'], ['g', 'g', \
'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g',\
 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [\
0, 0, 0, 0], [0, 0, 0, 0], ['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g'\
]])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([[0, 0, 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [\
0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'g', 'g'], ['w', 'w', 'g\
', 'g'], ['w', 'g', 'g', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, '\
g'], [0, 0, 0, 'g'], [0, 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, \
'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'],\
 [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0\
, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'g', '\
w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15), (3, 0), (3, 1\
)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    """
    winning_combinations = []
    for line in board:
        first_letter = line[0]
        status = True
        if first_letter == 0:
            status = False
            continue
        else:
            for elem in line:
                if elem == first_letter:
                    pass
                else:
                    status = False
                    continue
            if status is True:
                winning_combinations.append(line)
    for line in range(4):
        for column in range(16):
            line_out = []
            first_letter = board[column][line]
            line_out.append((line, column))
            status = True
            if first_letter == 0:
                status = False
                continue
            else:
                for dif in range(1,4):
                    nice = 0
                    if column + dif >= 16:
                        nice = 16
                    if board[column + dif - nice][line] == first_letter:
                        line_out.append((line, column + dif - nice))
                    else:
                        status = False
                        continue
                if status is True:
                    winning_combinations.append(line_out)
    for column in range(16):
        line = 0
        first_letter = board[column][line]
        if first_letter == 0:
            continue
        else:
            status_one = True
            status_two = True
            line_out_one = [(0, column)]
            line_out_two = [(0, column)]
            for dif in range(1,4):
                if column + dif >= 16:
                    nice = 16
                else:
                    nice = 0
                if board[column + dif - nice][line + dif] == first_letter:
                    line_out_one.append((dif, column + dif - nice))
                else:
                    status_one = False
            if status_one is True:
                winning_combinations.append(line_out_one)
            for dif in range(1,4):
                if column - dif < 0:
                    nice = 16
                else:
                    nice = 0
                if board[column - dif + nice][line + dif] == first_letter:
                    line_out_two.append((dif, column - dif + nice))
                else:
                    status_two = False
            if status_two is True:
                winning_combinations.append(sorted(line_out_two, reverse=True))
    if len(winning_combinations) == 0:
        return False
    else:
        return True, winning_combinations
