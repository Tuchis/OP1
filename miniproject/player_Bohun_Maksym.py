#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""
import sys
from logging import ERROR, debug, getLogger
import time
getLogger().setLevel(ERROR)


def dist(x1, y1, x2, y2):
    """
    >>> dist(1,1,3,3)
    2.8284271247461903
    Measure the distance between two points
    :param x1: X coordinate of the opponent's figure
    :param y1: Y coordinate of the opponent's figure
    :param x2: X coordinate of the newly placed figure
    :param y2: Y coordinate of the newly placed figure
    :return: distance between two points
    """
    return ((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2) ** 0.5


def dominance(plateau, player, i, j):
    """
    Get as close as possible to the opponent.
    Measures the distance from the newly placed figure
    to the closest opponent's figure.
    :param plateau: The plateau with the newly placed figure
    :param i: X coordinate of the newly placed figure
    :param player: Number of player
    :param j: Y coordinate of the newly placed figure
    :return: distance from the newly placed figure to the
    closest opponent's figure.
    """
    distances = []
    opponent = ("O" if player == 2 else "X")
    for string in range(len(plateau)):  # Measure the distance to each uncovered opponent's piece
        for elem in range(len(plateau[string])):
            if plateau[string][elem] == opponent:
                try:
                    if plateau[string - 1][elem] == opponent \
                            and plateau[string][elem - 1] == opponent \
                            and plateau[string][elem + 1] == opponent \
                            and plateau[string + 1][elem] == opponent:
                        continue
                    else:
                        distances.append(dist(int(i), int(j), string, elem))
                except IndexError:
                    distances.append(dist(int(i), int(j), string, elem))
    return min(distances)


def check_available_moves(plateau: list, figure: list, player: int, height: int):
    """
    This function returns all of the possible ways to place a figure on a plateau
    :param plateau: The current game plateau
    :param figure: The figure we have to place
    :param player: Number of player
    :param height: Height of the plateau
    :return: A list of possible moves and the number
    of player's figures on the field
    """
    del plateau[0]
    for i in range(len(plateau)):
        plateau[i] = plateau[i].replace('x', 'X').replace('o', 'O')  # Ignore the newly placed figures
        plateau[i] = plateau[i][4:]
    working_len = 0
    for i in range(len(figure)):
        for j in range(len(figure[0])):
            if figure[i][j] == '*':
                if working_len < j:
                    working_len = j
    possible = []
    for i in range(-len(figure), height + 2 - len(figure)):
        for j in range(-len(figure[0]), len(plateau[1]) - working_len):
            total_o = 0
            total_x = 0
            for fi, line in enumerate(figure):
                for fj, char in enumerate(line):
                    if char == '*':
                        if j + fj < len(plateau[0]):
                            if plateau[i + fi - 1][j + fj] == 'X':
                                total_x += 1
                            elif plateau[i + fi - 1][j + fj] == 'O':
                                total_o += 1
            good = False
            if player == 1:
                if total_o == 1 and total_x == 0:
                    good = True
            if player == 2:
                if total_o == 0 and total_x == 1:
                    good = True
            if good:
                distance = dominance(plateau, player, i - 1, j)  # distance from the figure we can place to the opponent
                possible.append(tuple(((i - 1, j), distance)))
    return possible


def parse_field_info():
    """
    Parse the info about the field.

    The input may look like this:

    Plateau 15 17:
    """
    info = input()
    width = info[:-1].split()[-1]
    height = info.split()[-2]
    debug(f"Description of the field: {info}")
    return height, width


def parse_field(height):
    """
    Parse the field.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param height: The height of the field
    """
    plateau = []
    for i in range(height + 1):
        line = input()
        plateau.append(line)
    return plateau


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure and then reads it.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    line = input()
    debug(f"Piece: {line}")
    fig_height = int(line.split()[-2])
    figure = []
    for _ in range(fig_height):
        line = input()
        figure.append(line)
        debug(f"Piece: {line}")
    return figure


def step(player: int):
    """
    Perform one step of the game.
    The strategy is simple:
    1. If the top of the plateau isn't yet filled with out figures, we move towards it.
    2. If the top is filled, we move towards the floor.
    3. If the top and the floor is filled, which means we already cut off a piece
    of the field from our opponent, we move as close to him as possible.

    :param player: Represents whether we're the first or second player
    """
    height, width = parse_field_info()
    plateau = parse_field(int(height))
    figure = parse_figure()
    available_moves = check_available_moves(plateau, figure, player, int(height))
    debug(available_moves)
    available_moves.sort(key=lambda x: x[1])
    if len(available_moves) == 0:
        print('I give up! Kolya the best!')
        sys.exit()
    best_move = available_moves[0][0]
    return best_move


def play(player: int):
    """
    Main game loop.

    :param player: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
